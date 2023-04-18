import RPi.GPIO as GPIO
import time
import logging
import threading
import os

class UltrasonicSensor :
    # Constructor
    def __init__(self,pin1,pin2) :
        self.__pin1 = pin1
        self.__pin2 = pin2

        # Set trigger pin in "out" mode (Sending) 
        GPIO.setup(self.__pin1,GPIO.OUT)

        # Set echo pin in "in" mode (Receiving)
        GPIO.setup(self.__pin2,GPIO.IN)


    # Get data from sensor
    def getSensorInfo(self):

        # Set pin to off (just for safety)
        GPIO.output(self.__pin1, False)

        # Trigger ultrasonic wave for 0.00001s
        GPIO.output(self.__pin1, True)
        time.sleep(0.00001)
        GPIO.output(self.__pin1, False)

        # Set trigger and echo time
        while GPIO.input(self.__pin2)==0:
            pulse_start = time.time()
        while GPIO.input(self.__pin2)==1:
            pulse_end = time.time()

        # Calculate duration between trigger and echo
        pulse_duration = pulse_end - pulse_start

        # Transform time in distance
        distance = pulse_duration * 17165
        distance = round(distance, 1)

        """test"""
        print(distance)

        # Return result
        return distance