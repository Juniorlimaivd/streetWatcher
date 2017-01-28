import pyrebase
import picamera

def connectBluetooth():



def getLocation():

camera = picamera.PiCamera()

config = {
	"apiKey" : "apiKey",
	"authDomain" : "projectId.firebaseapp.com",
	"databaseURL": "https://databaseName.firebaseio.com",
	"storageBucket" : "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)

database = firebase.database()

connectBluetooth()

led.blink("green")

while True:
	
	actualLocation = getLocation()

	if notIn(actualLocation, picturedLocations()):
		led.blink("blue")
    	camera.take_picture("imagem.jpg")
    	reference = sendtoStorage("imagem.jpg")

    	createDatabaseReference(reference,actualLocation)
    	led.blink("green")

    sleep(1)

