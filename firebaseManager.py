import pyrebase

class FirebaseManager:

	firebase = None
	database = None
	storage = None
	config = None
	def __init__ (self):
		self.config = {
			"apiKey" : "AIzaSyCdqFd6BOzCnx55lBezdzRq70kfmq8z5eY",
			"authDomain" : "calcada-34af9.firebaseapp.com",
			"databaseURL": "https://calcada-34af9.firebaseio.com",
			"storageBucket" : "calcada-34af9.appspot.com",
			"serviceAccount" : "calcada-34af9-firebase-adminsdk-44spg-2d4f905b92.json",
			"messagingSenderId": "1041897087083"
		}

		self.firebase = pyrebase.initialize_app(self.config)

		self.database = self.firebase.database()

		#self.storage = self.firebase.storage()

	def putTeste(self):
		data = {"name": "Mortimer 'Morty' Smith"}
		self.database.child("users").push(data)





serverManager = FirebaseManager()
serverManager.putTeste()