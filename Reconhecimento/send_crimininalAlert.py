#import requests 
import urllib
from json import dumps

def criminal_alert_sender(data_informations, suspect_id):
	alerted = False
	information_pack = {    
		'dataHoraRegistro': data_informations.date_request,
		'estado': 'Aberto',
		'numeroOnibus': data_informations.num_onibus,
		'latitude': data_informations.location[0],
		'longitude': data_informations.location[1],
		'suspeitoId': suspect_id,
		'urlFoto':data_informations.url_photo,	
		'capturado': False
						}
	# montagem da requisicao para a o sistema web de alertas
	url_post = 'https://alerta-api.azurewebsites.net/api/alertas'
	post_request = urllib.request.Request(url_post)
	post_request.add_header('Content-Type','application/json')
	post_data = dumps(information_pack,default=str)
	# ------------------------------------------------------
	try:
		with urllib.request.urlopen(post_request,post_data.encode('utf-8')) as response:
			alerted = True
	except Exception as err:
		print('Unable to send the request.\n Error: %s'%(type(err)))
		alerted = False
	finally:
		return alerted