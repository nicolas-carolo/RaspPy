# Electronic Connections

## Red LED

### Minimum requirements
- RPi.GPIO (`$ pip install RPi.GPIO`)

### Materials
- 1 Red LED
- 1 330 Ohm resistor
- 1 red cable connected to GPIO18 (pin 11) and to the long leg of the LED
- 1 black cable connected to the GND and to the short leg of the LED (+ 330 Ohm resistor)


## RGB LED

### Minimum requirements
- RPi.GPIO (`$ pip install RPi.GPIO`)

### Materials
- 1 RGB LED
- 3 330 Ohm resistor
- From left to right
    - 1 red cable connected to GPIO04 (pin 7) and to the exteral leg of the LED on the left (+ 330 Ohm resistor)
    - 1 black cable connected to the GND and to the internal long leg of the LED
    - 1 blue cable connected to GPIO17 (pin 11) and to the internal leg of the LED on the right (+ 330 Ohm resistor)
    - 1 green cable connected to GPIO27 (pin 13) and to the external leg of the LED on the right (+ 330 Ohm resistor)
