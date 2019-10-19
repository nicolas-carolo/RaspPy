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



class RGBLed:
    def __init__(self, red_port, green_port, blue_port):
        self.red_port = red_port
        self.green_port = green_port
        self.blue_port = blue_port
        

    def turn_off(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        print("LED off")
        GPIO.setup(self.red_port, GPIO.OUT)
        GPIO.output(self.red_port, 0)
        GPIO.setup(self.green_port, GPIO.OUT)
        GPIO.output(self.green_port, 0)
        GPIO.setup(self.blue_port, GPIO.OUT)
        GPIO.output(self.blue_port, 0)


    def turn_on(self, red_value, green_value, blue_value):
        if red_value == 0 and green_value == 0 and blue_value == 0:
            self.turn_off()
        elif red_value in range(0, 256) and green_value in range(0, 256) and blue_value in range(0, 256): 
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            led_status = "LED on: RGB(" + str(red_value) + "," + str(green_value) + "," + str(blue_value) + ")"
            print(led_status)
            GPIO.setup(self.red_port, GPIO.OUT)
            GPIO.output(self.red_port, red_value)
            GPIO.setup(self.green_port, GPIO.OUT)
            GPIO.output(self.green_port, green_value)
            GPIO.setup(self.blue_port, GPIO.OUT)
            GPIO.output(self.blue_port, blue_value)
        else:
            print("ERROR: Incorrect RGB values!")
            self.turn_off

    
    def isOn(self):
        if red_value == 0 and green_value == 0 and blue_value == 0:
            return False
        else:
            return True