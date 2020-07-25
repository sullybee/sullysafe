import datetime
import threading
from time import sleep

from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore


import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="sullybee.json"

db = firestore.Client()



coord2 = [40.728226,-73.794853]
coord1 = [40.7714030,-73.9195635]
#coord3 = [40.7081,73.9571]
#lst = [coord2,coord3,coord1]
lst = [coord2,coord1]
while(1):
	i =1
	for coord in lst: 
		data1 = {
        		u'point': "angel"+str(i),
			u'geo': firestore.GeoPoint(coord[0],coord[1])
    		}

		db.collection(u'data').document(u'datafile').set(data1)
		sleep(10)
		i = i + 1
	i =1 
'''
cred = credentials.Certificate("./sullybee.json")
firebase_admin.initialize_app(cred)

db = firestore.Client()
# [START add_data_types]
data = {
		u'longitude': 40.999999,
		u'altitude': 73.77777,

}

db.collection(u'data').document(u'datafile').set(data)
'''
