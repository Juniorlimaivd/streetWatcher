import os

class CameraManager:

	def __init__ (self):
		os.system("sudo chmod +x take_picture.sh")


	def take_picture(self):
		os.system("./take_picture.sh")



#camera = CameraManager()
#camera.take_picture()