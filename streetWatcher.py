import cameraManager
import firebaseManager
import socketManager
import ledManager
from time import sleep

def notIn (location, locations):
	#print(location)
	if locations != None:
		#print("here")
		for actual in locations :
			#print(actual["latitude"],actual["longitude"])
			if fabs(Float(actual["latitude"]) - Float(location[0])) < 0.50 and  fabs(Float(actual["latitude"]) - Float(location[1])) < 0.50: 
				return False
			else:
				return True
	else:
		return True

camera = cameraManager.CameraManager()

serverManager = firebaseManager.FirebaseManager()

gpsManager = socketManager.SocketManager()
ledController = ledManager.LedManager()

ledController.blinkLed("green")



while True:
	
	actualLocation = gpsManager.getLocation()

	presentLocations = serverManager.getLocationsInDatabase()

	if notIn(actualLocation, presentLocations):
		ledController.blinkLed("blue")
    	name = camera.take_picture()
    	reference = serverManager.saveImage(name)
    	nameWithoutExtension = name.split('.')

    	serverManager.createImageData(nameWithoutExtension[0],actualLocation)
    	ledController.blinkLed("green")
	
	print("im here")
	sleep(10)







