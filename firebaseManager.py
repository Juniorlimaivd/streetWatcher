from pyrebase import *

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
			"messagingSenderId": "1041897087083",
			"serviceAccount" : "calcada-34af9-firebase-adminsdk-44spg-2d4f905b92.json"			
		}

		self.firebase = pyrebase.initialize_app(self.config)

		self.database = self.firebase.database()

		self.storage = self.firebase.storage()

	def putTeste(self):
		data = {"name": "Mortimer 'Morty' Smith"}
		self.database.child("users").push(data)

	def saveImage(self,imagename):
		self.storage.child("images/image.jpg").put("/home/pi/Desktop/"+imagename)




serverManager = FirebaseManager()
#serverManager.putTeste()
serverManager.saveImage("image2.jpg")