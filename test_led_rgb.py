import RPi.GPIO as GPIO
from LEDs import RGBLed

RED = 4
GREEN = 27
BLUE = 17

led1 = RGBLed(RED, GREEN, BLUE)
led1.turn_off()
red_value = int(input("Red (from 0 to 255): "))
green_value = int(input("Green (from 0 to 255): "))
blue_value = int(input("Blue (from 0 to 255): "))
led1.turn_on(red_value, green_value, blue_value)