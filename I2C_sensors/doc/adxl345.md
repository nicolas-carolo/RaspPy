# ADXL345: Accelerometer

## Hardware

### Requirements

* ADXL345 accelerometer
* 4 cable (I have chosen one red, one black, one blue, and one orange)

### Connection

* 1 red cable connected to the 3V3 power pin (pin 1) of the Raspberry and to the VCC of the accelerometer
* 1 black cable connected to the GND (for example pin 9) of the Raspberry and to the GND of the accelerometer
* 1 blue cable connected to the GPIO2 (pin 3) and to the **SDA** (**Serial Data** for transfering data)
* 1 orange cable connected to the GPIO3 (pin 5) and to the **SCL** (**Serial Clock** which is the signal clock and it is used for synchronizing all data transfered over the I2C bus)

## Software

### Requirements
* Python 3
* adafruit-circuitpython-adxl34x

### Get accelerometer's values using I2C interface

1. If I2C interface is disabled, enable it:
	1. Open `raspi-config`:
	```sh
	sudo raspi-config
	```
	2. Go to `Interfacing Options`
	3. Go to `P5 I2C`
	4. Reply 'Yes' to the request of enabling I2C
2. Check if the sensor is communicating properly over I2C:
	```sh
	pi@raspberry:~$ i2cdetect -y 1
     	0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
	00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
	10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	50: -- -- -- 53 -- -- -- -- -- -- -- -- -- -- -- -- 
	60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	70: -- -- -- -- -- -- -- --
	```
	From the output of this command we have got the I2C address, which in my case is 0x53.
3. Install `adafruit-circuitpython-adxl34x`:
	```sh
	pip install adafruit-circuitpython-adxl34x
	```

4. Run the code I stored in `test_adxl345.py`
