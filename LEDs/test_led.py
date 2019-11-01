import time
from LEDs import RedLed

led1 = RedLed(18)
led1.print_GPIO_port()
if led1.isOn():
    led1.turn_off()
else:
    led1.turn_on()
