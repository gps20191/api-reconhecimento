from peewee import *

class AlerteRequest():
	def __init__(self, alerted= False,processed = False,match = False,id_request = 0,id_photo = 0,url_photo = '',
				location = [],date_request = '',num_onibus = 0,blob_img = ''):
		self.alerted = alerted
		self.processed = processed
		self.match = match
		self.id_request = id_request
		self.id_photo = id_photo
		self.url_photo = url_photo
		self.location = location
		self.date_request = date_request
		self.num_onibus = num_onibus
		self.blob_img = blob_img
	def img_type(self):
		img_string = self.blob_img[11:]
		extension = ''
		for interator in img_string:
			if(interator != ';'):
				extension = extension + interator
			else:
				break
		return extension

class AlertDb():
	def __init__(self):
		alerts = Table('alertrequest',('requestid','processed','match','alerted','urlphoto','blobimg','latitude','longitude','requestdate','idphoto','numbus'))
		database =  PostgresqlDatabase('dirvxher',user='dirvxher',password='lW4EmcVPA7buBIVqObKquyXlSQwbm8JF',host='motty.db.elephantsql.com', port=5432) 
		alerts.bind(database)
		self.table = alerts