import RPi.GPIO as GPIO
import time
import logging
import threading
import os

from GPIO.UltrasonicSensor import UltrasonicSensor
from GPIO.IrSensor import IrSensor
from VEHICLE.Vehicle import Vehicle
from PWM.Motor import Motor


# "Main" Class code
if __name__ == "__main__":
    # GPIO's settings
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Create a vehicle
    vehicle = Vehicle("My module")

    # Creating sensors
    capteur = UltrasonicSensor(23,24)
    capteur2 = IrSensor(20)

    # Adding sensors to the vehicle
    vehicle.addSensor(capteur)
    vehicle.addSensor(capteur2)


    # Menu :
    inputMenu = 0
    while inputMenu != 999 :
        print("----- Menu -----")
        print("1 - Go straight")
        print("2 - Go backwards")
        print("3 - Stop Wheels")
        print("4 - Straight, variable speed")
        print("5 - Backwards, variable speed")
        print("6 - 180 left")
        print("7 - 180 right")
        print("8 - Making a 8")
        print("9 - Go along a wall")
        print("10 - Straight until obstacle")
        print("11 - Straight until dark")
        print("12 - Straight until n laps")
        print("999 - exit")
        print("----------------")
        inputMenu = int(input("What do you want to do ? : "))
        os.system('clear')

        if inputMenu == 1 :
            motor = Motor(11,12,4)
            motor.setup()
            #test()
            motor.setSpeed(30)
            motor.forward()
        
        elif inputMenu == 3:
            try:
                motor = Motor(11,12,4)
                motor.setSpeed(0)
            except:
                pass
       
        elif inputMenu == 4 :
            motor = Motor(11,12,4)
            motor.setup()
            #test()
            motor.setSpeed(30)
            motor.forward()


        elif inputMenu == 9:
            t1 = threading.Thread(target=vehicle.moveUntilObstacle, args=(capteur,))
            t1.start()
            t1.join()
            time.sleep(0.5)
            os.system('clear')
            time.sleep(0.5)

        elif inputMenu == 10 :
            # Stop on dark line
            t1 = threading.Thread(target=vehicle.moveUntilDark, args=(capteur2,))
            t1.start()
            t1.join()
            time.sleep(0.5)
            os.system('clear')
            time.sleep(0.5) 

        elif inputMenu == 11 :
            # Stop on dark line
            lapsNumber = int(input("how many laps : "))
            t1 = threading.Thread(target=vehicle.moveUntilLaps, args=(capteur2,lapsNumber))
            t1.start()
            t1.join()
            time.sleep(0.5)
            os.system('clear')
            time.sleep(0.5) 

 