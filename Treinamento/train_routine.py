
import base64
# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
from common.suspect_info import *
from Treinamento.train import *
# ---------------------------------


def create_photos(suspect_data):
	for suspectInterator in suspect_data:
		# transformando o base64 em uma imagem de fato no computador
		img_data = base64.b64decode(suspectInterator.face_blob.split(',')[1])
		file_name = 'train_photos/' + (str)(suspectInterator.suspect_id) +\
			 '.'+suspectInterator.img_type()
		img_output = open(file_name, 'wb')
		img_output.write(img_data)
		img_output.close()
	# ----------------------------------------------------------


def main():
	print('INCIANDO O TREINAMENTO COM AS FOTOS DO BANCO DE SUSPEITOS')
	table_db = Suspectdb()
	# busca todas as imagens disponiveis no banco de dados
	query = table_db.table.select()
	suspect_data = []
	# cada linha encontrada se tornara um tupla, que sera representada por id e o blob da imagem
	for row in query:
		current_suspect = Suspect(suspect_id = row['suspeitoid'], face_blob= row['blobface'], name= row['nome'])
		suspect_data.append(current_suspect)

	# criacao das imagens em um diretorio local para o treinamento
	create_photos(suspect_data)
	# criacao do arquivo de treino
	classifier = training("./train_photos", model_save_path="./trained_knn_model.clf", n_neighbors=2)
	print('FINALIZADO O TREINAMENTO, O BANCO DE SUSPEITOS ACABA DE SER PROCESSADO')


if __name__ == '__main__':
	main()
