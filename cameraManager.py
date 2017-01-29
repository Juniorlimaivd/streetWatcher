import os
import time
class CameraManager:

	def __init__ (self):
		os.system("sudo chmod +x take_picture.sh")


	def take_picture(self):
		date = time.strftime("%Y-%m-%d_%H%M")
		os.system("./take_picture.sh" + date)

		return date + '.jpg'



camera = CameraManager()
name = camera.take_picture()
print(name)
