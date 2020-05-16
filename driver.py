from time import ctime
from adafruit_motorkit import MotorKit

class Driver:
    def __init__(self):
        self.kit = MotorKit()
        self.speed = 0


    def Forward(self):
        self.kit.motor1.throttle = float(int(self.speed)/255)
        self.kit.motor2.throttle = float(int(self.speed)/255)
        self.kit.motor3.throttle = float(int(self.speed)/255)
        self.kit.motor4.throttle = float(int(self.speed)/255)

    def Backward(self):
        self.kit.motor1.throttle = -float(int(self.speed)/255)
        self.kit.motor2.throttle = -float(int(self.speed)/255)
        self.kit.motor3.throttle = -float(int(self.speed)/255)
        self.kit.motor4.throttle = -float(int(self.speed)/255)

    def Right(self):
        self.kit.motor1.throttle = float(int(self.speed)/255)
        self.kit.motor2.throttle = float(int(self.speed)/255)
        self.kit.motor3.throttle = - float(int(self.speed) / 255)
        self.kit.motor4.throttle = - float(int(self.speed) / 255)

    def Left(self):
        self.kit.motor1.throttle = - float(int(self.speed) / ( 255))
        self.kit.motor2.throttle = - float(int(self.speed)/  ( 255))
        self.kit.motor3.throttle = float(int(self.speed) / 255)
        self.kit.motor4.throttle = float(int(self.speed) / 255)


    def Stop(self):
        self.kit.motor1.throttle = float(0)
        self.kit.motor2.throttle = float(0)
        self.kit.motor3.throttle = float(0)
        self.kit.motor4.throttle = float(0)


                
    def setSpeed(self, new_speed):

        self.speed = new_speed
        print('Setting speed to %s' % self.speed)




