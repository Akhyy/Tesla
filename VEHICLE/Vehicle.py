import RPi.GPIO as GPIO
import time
import logging
import threading
import os

class Vehicle:
    # Constructor
    def __init__(self, name):
        self.__name = name
        self.__sensors = []

    # Accessor and Mutator of name
    def getVehicleName(self):
        return self.__name
    
    def setVehicleName(self,name):
        self.__name = name

    # Add a Sensor to the car
    def addSensor(self,sensor) :
        self.__sensors.append(sensor)

    # Returns a list of sensors present on the vehicle 
    def getSensorsList(self):
        return self.__sensors
    
    """ 1 """
    def moveForward(self):
        while EmergencyStop != True:
            time.sleep(0.3)
            print("avance")
        print("stop")
    
    # Print all sensors info
    def getCarInfo(self):
        while 1:
            for sensor in self.__sensors :
                print(sensor.getSensorInfo())
            time.sleep(0.5)

    """ 9 """
    # Go straight until detect a wall
    def moveUntilObstacle(self,ultrasonicSensor):
        # Reset emergencyStop
        global EmergencyStop
        EmergencyStop = False

        # Start a thread that will continuously spin the wheels
        t2 = threading.Thread(target=self.moveForward, args=())
        t2.start()

        # If distance to the wall > 5cm, set "emergencyStop" to "True"
        while ultrasonicSensor.getSensorInfo() >= 5:
            time.sleep(0.3)
        EmergencyStop = True


    """ 10 """
    # Go straight until see a dark line
    def moveUntilDark(self, irSensor):
        # Reset emergencyStop
        global EmergencyStop
        EmergencyStop = False

        # Start a thread that will continuously spin the wheels
        t2 = threading.Thread(target=self.moveForward, args=())
        t2.start()

        # If sensor detect black, stop loop and set "emergencyStop" to "True"
        while irSensor.getSensorInfo() != 1:
            time.sleep(0.3)
        EmergencyStop = True

    """ 11 """
    # Go straight until car passed n times the dark line 
    def moveUntilLaps(self, irSensor, lapsNumber):
        # Reset emergencyStop
        global EmergencyStop
        EmergencyStop = False
         
        # Start a thread that will continuously spin the wheels
        t2 = threading.Thread(target=self.moveForward, args=())
        t2.start()

        # If sensor detect black and count number of loops. Then, set emergencyStop to "True"
        for i in range(0,lapsNumber):
            while irSensor.getSensorInfo() != 1:
                time.sleep(0.3)
            while irSensor.getSensorInfo() == 1:
                time.sleep(0.3)
        EmergencyStop = True
        
    def alongAWall(self):
        pass