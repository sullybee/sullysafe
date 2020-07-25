import datetime
import threading
from time import sleep

from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials

<<<<<<< HEAD

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="sullybee.json"

db = firestore.Client()


coord1 = [42.098700,-75.912540]
coord2 = [40.728226,-73.794853]
lst = [coord1,coord2]
while(1):
	i =1
	for coord in lst: 
		data1 = {

        		u'point': "angel"+str(i),
			u'lat': coord[0],
        		u'lon': coord[1]
    		}

		db.collection(u'data').document(u'datafile').set(data1)
		sleep(10)
		i = i + 1
	i =1 
=======
cred = credentials.Certificate("./sullybee.json")
firebase_admin.initialize_app(cred)

db = firestore.Client()
# [START add_data_types]
data = {
		u'longitude': 40.999999,
		u'altitude': 73.77777,

}

db.collection(u'data').document(u'datafile').set(data)
>>>>>>> ad28ebebb35f7610f73445b804c6effd80f36242
