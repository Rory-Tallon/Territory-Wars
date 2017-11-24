import random
import math

class Camera:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xVel = 0
        self.yVel = 0

        self.shakeXVel = 0
        self.shakeYVel = 0
        
        self.shakeBool = False
        self.shakeReduce = 0.9
        self.shakeCount = int(math.log(0.001, self.shakeReduce))
        self.shakeCountMax = self.shakeCount

        self.tempXVel = 0
        self.tempYVel = 0
        self.tempX = x
        self.tempY = y

    def shake(self, magnitude):

        if not(self.shakeBool):
            self.tempX = self.x
            self.tempY = self.y
            
            self.shakeXVel = (random.random() - 0.5) * magnitude
            self.shakeYVel = (random.random() - 0.5) * magnitude
            self.shakeBool = True
            self.shakeCount = self.shakeCountMax

    def update(self):
        
        self.x += self.xVel
        self.y += self.yVel


        if self.shakeBool:
            self.tempXVel += self.xVel
            self.tempYVel += self.yVel

            if self.shakeCount % 5 == 0:
                self.shakeXVel = self.shakeXVel  * self.shakeReduce * -1
                self.shakeYVel = self.shakeYVel  * self.shakeReduce * -1

                self.x += self.shakeXVel
                self.y += self.shakeYVel

            self.shakeCount -= 1


            if self.shakeCount == 0:
                self.shakeBool = False
                self.x = self.tempX + self.tempXVel
                self.y = self.tempY + self.tempYVel
                self.tempXVel = 0
                self.tempYVel = 0
