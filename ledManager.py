import RPi.GPIO as gpio
from time import sleep
class LedManager:
	redLedPin = 11
	greenLedPin = 13
	blueLedPin = 15

	def __init__(self):
		gpio.setmode(gpio.BOARD)
		gpio.setup(self.redLedPin, gpio.OUT)
		gpio.setup(self.greenLedPin, gpio.OUT)
		gpio.setup(self.blueLedPin, gpio.OUT)

	def blinkLed(self,led):
		if led == 'red':
			gpio.output(self.redLedPin, gpio.HIGH)
			gpio.output(self.blueLedPin, gpio.LOW)
			gpio.output(self.greenLedPin, gpio.LOW)
		elif led == 'blue':
			gpio.output(self.redLedPin, gpio.LOW)
			gpio.output(self.blueLedPin, gpio.HIGH)
			gpio.output(self.greenLedPin, gpio.LOW)
		else:
			gpio.output(self.redLedPin, gpio.LOW)
			gpio.output(self.blueLedPin, gpio.LOW)
			gpio.output(self.greenLedPin, gpio.HIGH)

	def finishLedManager(self):
		gpio.cleanup()



led = LedManager()

while True:
	print("acendendo pino 11")
	led.blinkLed('red')
	sleep(5)
	print("acendendo pino 13")
	led.blinkLed('blue')
	sleep(5)
	print("acendendo pino 15")
	led.blinkLed('green')
	sleep(5)

