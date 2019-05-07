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
HALL_SENSOR_C1 = 19 # Phase-A
HALL_SENSOR_C2 = 26 # Phase-B

def setup():
  print ("SETUP")
  # using the BOARD numbering system
  GPIO.setmode(GPIO.BCM)
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
  #print ("Sensor PULSE " + repr(tStamp))

def mainLoop():
  global sensorCounter
  sensorCounter = 0
  print ("MAINLOOP")
  GPIO.add_event_detect(HALL_SENSOR_C1, GPIO.FALLING, callback=sensorCB)
  GPIO.add_event_detect(HALL_SENSOR_C2, GPIO.FALLING, callback=sensorCB)  
  while True :
    time.sleep(1)
    print ("Counter: " + repr(sensorCounter) + " REV: " + repr(sensorCounter/(22*90))) 

if __name__=="__main__":
  print ("Hall sensor Speedometer")
  setup()
  try:
    mainLoop()
  except KeyboardInterrupt:  # Ctrl-C 
    destroy()

