import pyrebase

class FirebaseManager:

	firebase = None
	database = None
	storage = None

	def __init__ (self):
		config = {
			"apiKey" : "apiKey",
			"authDomain" : "projectId.firebaseapp.com",
			"databaseURL": "https://databaseName.firebaseio.com",
			"storageBucket" : "projectId.appspot.com"
		}

		self.firebase = pyrebase.initialize_app(config)

		self.database = self.firebase.database()

		self.storage = self.firebase.storage()





serverManager = FirebaseManager()