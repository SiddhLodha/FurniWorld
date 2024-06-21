import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("Furniworld\\furniworldweb-firebase-adminsdk-sejnc-dd538ddedb.json")
firebase_admin.initialize_app(cred)
