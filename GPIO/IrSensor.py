import RPi.GPIO as GPIO
import time
import logging
import threading
import os

class IrSensor:
    def __init__(self,pin) :
        self.__pin = pin
        # Set Ir pin in "in" mode (Receiving) 
        GPIO.setup(pin, GPIO.IN)

    def getSensorInfo(self):
        # Return result (0: RGB, 1: black)
        return GPIO.input(self.__pin)