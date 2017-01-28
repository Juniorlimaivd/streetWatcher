import os

class CameraManager:

	def __init__ (self):
		os.system("sudo chmod +x takepicture.sh")
		os.system("raspberry")
		

    def takePicture(self):        
        os.system("./takepicture.sh")



camera = CameraManager()
camera.takepicture()