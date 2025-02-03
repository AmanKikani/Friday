import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("/Users/amankikani/PycharmProjects/Friday/luminai-1f820-firebase-adminsdk-qat14-ff1a16fa1a.json")
firebase_admin.initialize_app(cred)
