import cameraManager
import firebaseManager
import socketManager
import ledManager
from time import sleep
import math

def notIn (location, locations):
	print("here")
	if locations != None:
		print(location)
		for actual in locations :
			print actual
			#print(actual["latitude"],actual["longitude"])
			print(float(actual["latitude"]))
			print(math.fabs(float(actual["latitude"]) - float(location[0])))
			if math.fabs(float(actual["latitude"]) - float(location[0])) < 0.50 and  math.fabs(float(actual["latitude"]) - float(location[1])) < 0.50: 
				return False
			
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

    	serverManager.createImageData(nameWithoutExtension[0],reference,actualLocation)
    	ledController.blinkLed("green")
	
	print("im here")
	sleep(10)







