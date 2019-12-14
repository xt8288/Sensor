from time import sleep

import RPi.GPIO as GPIO
import smbus

import device

port = 1
bus = smbus.SMBus(port)
apds = device.APDS9960(bus)


try:
    apds.enableLightSensor()
    oval = -1
    while True:
        sleep(0.25)
    #        val = apds.readAmbientLight()
        val1 = apds.readRedLight()
        val2 = apds.readGreenLight()
        val3 = apds.readBlueLight()
        if val1 != oval:
            print("RedLight={}".format(val1))
    #            print("AmbientLight={}".format(val))
            oval = val1

finally:
    GPIO.cleanup()
    print ("Bye")
