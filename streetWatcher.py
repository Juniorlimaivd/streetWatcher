import cameraManager
import firebaseManager
import socketManager
import ledManager
from time import sleep

def notIn (location, locations):

	if locations != None:
		for actual in locations :
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

    	serverManager.createImageData(reference,actualLocation)
    	ledController.blinkLed("green")

	else:
    	print("dont need to take photos")
	sleep(10)






