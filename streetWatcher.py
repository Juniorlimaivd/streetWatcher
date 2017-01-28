#import pyrebase
import cameraManager
import firebaseManager
#def connectBluetooth():

camera = cameraManager.CameraManager()

#def getLocation():

serverManager = firebaseManager.FirebaseManager()

config = {
	"apiKey" : "apiKey",
	"authDomain" : "projectId.firebaseapp.com",
	"databaseURL": "https://databaseName.firebaseio.com",
	"storageBucket" : "projectId.appspot.com"
}

#firebase = pyrebase.initialize_app(config)

#database = firebase.database()

#connectBluetooth()

#led.blink("green")

#while True:
	
#	actualLocation = getLocation()

#	if notIn(actualLocation, picturedLocations()):
#		led.blink("blue")
 #   	camera.take_picture("imagem.jpg")
 #   	reference = sendtoStorage("imagem.jpg")

  #  	createDatabaseReference(reference,actualLocation)
   # 	led.blink("green")

    #sleep(1)


