import pyrebase

class FirebaseManager:

	firebase = nil
	database = nil
	storage = nil

	def __init__ (self):
		config = {
			"apiKey" : "apiKey",
			"authDomain" : "projectId.firebaseapp.com",
			"databaseURL": "https://databaseName.firebaseio.com",
			"storageBucket" : "projectId.appspot.com"
		}

		self.firebase = pyrebase.initialize_app(config)

		self.database = firebase.database()

		self.storage = firebase.storage()





serverManager = FirebaseManager()