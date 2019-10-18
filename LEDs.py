import RPi.GPIO as GPIO


class RedLed:
    def __init__(self, GPIO_port):
        self.GPIO_port = GPIO_port

    def turn_on(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.GPIO_port,GPIO.OUT)
        print("LED on")
        GPIO.output(self.GPIO_port,GPIO.HIGH)

    def turn_off(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.GPIO_port,GPIO.OUT)
        print("LED off")
        GPIO.output(self.GPIO_port,GPIO.LOW)

    def print_GPIO_port(self):
        print("The LED's GPIO port is", self.GPIO_port)

    def isOn(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.GPIO_port, GPIO.IN) 
        return GPIO.input(self.GPIO_port)