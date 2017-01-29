import RPi.GPIO as gpio
from time import sleep
class LedManager:
	redLedPin = 2
	greenLedPin = 3
	blueLedPin = 4

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

led.blinkLed('red')
led.blinkLed('blue')
led.blinkLed('green')