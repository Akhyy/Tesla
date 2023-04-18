import RPi.GPIO as GPIO
import PWM.PCA9685 as p
import time    # Import necessary modules


class Motor:
     # Constructor
    def __init__(self,pin1,pin2,channel) :
        self.__pin1 = pin1
        self.__pin2 = pin2
        self.__channel = channel

        self.__pins = [self.__pin1, self.__pin2]

        for pin in self.__pins:
            GPIO.setup(pin, GPIO.OUT) 

    def setSpeed(self, speed):
        speed *= 40
        print ('speed is: ', speed)
        pwm.write(self.__channel, 0, speed)

    def setup(self):
        self.__forward == 'True'
        global pwm
        pwm = p.PWM()                  
        pwm.frequency = 60
        try:
            for line in open("config"):
                if line[0:8] == "forward":
                    forward = line[11:-1]
        except:
            pass
        if self.__forward == 'True':
            self.__backward = 'False'
        elif self.__forward == 'False':
            self.__backward = 'True'

    def motor(self,x):
        if x == 'True':
            GPIO.output(self.__pin1, GPIO.LOW)
            GPIO.output(self.__pin2, GPIO.HIGH)
        elif x == 'False':
            GPIO.output(self.__pin1, GPIO.HIGH)
            GPIO.output(self.__pin2, GPIO.LOW)
        else:
            print ('Config Error')

    def forward(self):
        self.motor(self.__forward)

    def backward(self):
        self.motor(self.__backward)
    
    def stop(self):
        for pin in self.__pins:
            GPIO.output(pin, GPIO.LOW)

