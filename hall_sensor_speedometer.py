#!/usr/bin/python

#--------------------------------------
#       Hall Effect Sensor Speedometer
#
# Author : Alex
# Date   : 29/04/2019
# Ref: https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/
#--------------------------------------

# Import required libraries
import RPi.GPIO as GPIO
import time
import datetime

# define constants
HALL_SENSOR_C1 = 17 # Phase-A
HALL_SENSOR_C2 = 27 # Phase-B

def setup():
  # using the BOARD numbering system
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  # Setup GPIO pins
  GPIO.setup(HALL_SENSOR_C1, GPIO.IN)
  GPIO.setup(HALL_SENSOR_C2, GPIO.IN)

def destroy():
  # Reset GPIO settings
  GPIO.cleanup()  

def sensorCB(channel):
  global sensorCounter
  sensorCounter += 1
  #t = time.time()
  #tStamp = datetime.datetime.fromtimestamp(t).strftime('%H:%M:%S')  
  #print "Sensor PULSE " + tStamp

def mainLoop():
  global sensorCounter
  sensorCounter = 0
  GPIO.add_event_detect(HALL_SENSOR_C1, GPIO.RISING, callback=sensorCB)
  GPIO.add_event_detect(HALL_SENSOR_C2, GPIO.RISING, callback=sensorCB)  
  while True :
    time.sleep(1)
    print "Sensor Counter: ", sensorCounter 

if __name__=="__main__":
  print "Hall sensor Speedometer\n"
	setup()
	try:
		mainLoop()
	except KeyboardInterrupt:  # When press control C child program will distroy
		destroy()
