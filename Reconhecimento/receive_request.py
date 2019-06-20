import base64
#used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
from common.alertrequest import *
from Reconhecimento.process_request import *
from Reconhecimento.send_crimininalAlert import *
#---------------------------------

def update_table(informations,database):
	alerts = database.table
	database.table.update(processed=informations.processed,match=informations.match,
	alerted=informations.alerted).where(alerts.requestid==informations.id_request).execute()
	print('ALERTA %s ATUALIZADO NO BANCO' %(informations.id_request))


def main():
	print('INICIANDO O PROCESSOR DE RECONHECIMENDO NOS PEDIDOS PENDENTES')
	table_db = AlertDb()
	query = table_db.table.select().where(table_db.table.processed == False)
	for row in query:
		request = AlerteRequest(id_request = row['requestid'], id_photo = row['idphoto'],
		url_photo = row['urlphoto'], location = [row['latitude'], row['longitude']], date_request = row['requestdate'], num_onibus = row['numbus'], blob_img = row['blobimg'])
		request.processed = True
		# transformando o base64 em uma imagem de fato no computador
		img_data = base64.b64decode(request.blob_img.split(',')[1])
		file_name = 'request_photos/request'+ (str)(request.id_request) +'.'+request.img_type()
		img_output = open(file_name,'wb')
		img_output.write(img_data)
		img_output.close()
		# ----------------------------------------------------------
		full_path_img = os.path.join(file_name)
		result_search = predict(full_path_img, model_path="trained_knn_model.clf")
		finded_persons = []
		for person, (top, right, bottom, left) in result_search:
			# caso pelo menos 1 pessoa seja encontrada na imagem a requisicao é lidada como match
			if(person != 'unknown'):
				request.match = True
				finded_persons.append(person)
		if(len(finded_persons) > 0):
				request.processed = True
				for person in finded_persons:
					request.alerted = True
					#caso pelo menos a presenca de um 1 suspeito seja informada a requisicao é lidada como alertada.
					if(criminal_alert_sender(request,person)):
							request.alerted = True
		update_table(request,table_db)


	print('PEDIDOS PROCESSADOS')

if __name__ == '__main__':
	main()