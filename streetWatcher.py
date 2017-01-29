import cameraManager
import firebaseManager
import socketManager
import ledManager
from time import sleep
import math

def notIn (location, locations):
	print("here")
	out = True
	if locations != None:
		print(location)
		for actual in locations :
			print actual
			#print(actual["latitude"],actual["longitude"])
			print(float(actual["latitude"].encode('ascii')))
			print(float(location[0].encode('ascii')))
			print(float(actual["latitude"].encode('ascii')) - float(location[0].encode('ascii')))
			print(math.fabs(float(actual["longitude"].encode('ascii')) - float(location[1].encode('ascii'))) < 0.50)
			print(math.fabs(float(actual["longitude"].encode('ascii')) - float(location[1].encode('ascii'))))
			if math.fabs(float(actual["latitude"].encode('ascii')) - float(location[0].encode('ascii')) < 0.50 and math.fabs(float(actual["longitude"].encode('ascii')) - float(location[1].encode('ascii'))) < 0.50): 
				print("olar")
				out = False
				print out
				print '3'
				break
			print out
			print '2'
		print out 
		print '1'
	return out
	


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







