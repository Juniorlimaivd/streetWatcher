import RPi.GPIO as gpio
from time import sleep
class LedManager:
	redLedPin = 2
	greenLedPin = 3
	blueLedPin = 4

	def __init__(self):
		gpio.setmode(gpio.BOARD)
		gpio.setup(redLedPin, gpio.OUT)
		gpio.setup(greenLedPin, gpio.OUT)
		gpio.setup(blueLedPin, gpio.OUT)

	def blinkLed(self,led):
		if led == 'red':
			gpio.output(redLedPin, gpio.HIGH)
			gpio.output(blueLedPin, gpio.LOW)
			gpio.output(greenLedPin, gpio.LOW)
		elif led == 'blue':
			gpio.output(redLedPin, gpio.LOW)
			gpio.output(blueLedPin, gpio.HIGH)
			gpio.output(greenLedPin, gpio.LOW)
		else:
			gpio.output(redLedPin, gpio.LOW)
			gpio.output(blueLedPin, gpio.LOW)
			gpio.output(greenLedPin, gpio.HIGH)

	def finishLedManager(self):
		gpio.cleanup()



led = LedManager()

led.blinkLed('red')
led.blinkLed('blue')
led.blinkLed('green')