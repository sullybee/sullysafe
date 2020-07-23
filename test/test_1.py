import datetime
import threading
from time import sleep

from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("./sullybee.json")
firebase_admin.initialize_app(cred)

db = firestore.Client()
# [START add_data_types]
data = {
		u'longitude': 40.999999,
		u'altitude': 73.77777,

}

db.collection(u'data').document(u'datafile').set(data)
