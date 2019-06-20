from peewee import *


class Suspect:
    def __init__(self, suspect_id=0, face_blob='', name=''):
        self.suspect_id = suspect_id
        self.face_blob = face_blob
        self.name = name

    def img_type(self):
        img_string = self.face_blob[11:]
        extension = ''
        for interator in img_string:
            if(interator != ';'):
                extension = extension + interator
            else:
                break
        return extension


class Suspectdb():
    def __init__(self):
        suspect = Table('suspeitos', ('suspeitoid', 'nome', 'blobface'))
        database = PostgresqlDatabase(
            'mokhalbx', user='mokhalbx', password='2C4stD_eSZib6GiRMUCKiLgEvfur5eOZ', host='motty.db.elephantsql.com', port=5432)
        suspect.bind(database)
        self.table = suspect
