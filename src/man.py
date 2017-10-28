import math
import pygame
from pygame.locals import *

class Man:

    def __init__(self, x, y, tex, rifleTex):
        self.coords = [x, y]
        self.start = [x, y] #Can be used for finding distance from start of turn
        
        self.xVel = 0
        self.yVel = 0

        self.maxXVel = 1 
        self.jumpVel = -3
        
        self.leftDown = False
        self.rightDown = False
        self.jump = False

        self.rifleDown = False
        self.rifleUp = False
        self.rifleAngle = 0

        self.distanceWalked = 0

        self.tex = pygame.image.load(tex) #Load the image
        self.rect = self.tex.get_rect() #Create a rectangle with the correct width and height corresponding to the texture
        self.rect.x, self.rect.y = self.coords[0], self.coords[1] #Move the rectangle so it is in the correct position
        

        self.rifleTex_ = pygame.image.load(rifleTex) 
        self.rifleWidth, self.rifleHeight = self.rifleTex_.get_rect().width, self.rifleTex_.get_rect().height
        self.rifleTex = pygame.Surface((self.rifleWidth*2 + self.rect.width, self.rect.height), pygame.SRCALPHA)
        self.rifleTex.blit(self.rifleTex_, (0, self.rect.height/2 - 15))

        self.startRifleTex = self.rifleTex.copy() 


    def update(self, state): #Updates the man based on velocities, ensures he does not got out of bounds
        if self.distanceWalked <= state.maxDistance:
            if self.leftDown: #Horizontal movement
                self.xVel = -1 * self.maxXVel
            elif self.rightDown:
                self.xVel = self.maxXVel
            else:
                self.xVel = 0
        else:
            self.xVel = 0

        self.yVel += state.gravity/60 #Acceleration due to gravity (divided by 60 because 60 frames per second)
        self.coords[0] += self.xVel #Actually move the man
        self.coords[1] += self.yVel

        oob = self.out_of_bounds(state) #Check if the man is out of bounds
        if oob[0]:
            self.coords[0] += oob[1][0] #If they are out of bounds, shift them back into the  screen
            self.coords[1] += oob[1][1]
            self.rect.x, self.rect.y = self.coords[0], self.coords[1] #Move the rectangle accordingly

        else:
            self.rect.x, self.rect.y = self.coords[0], self.coords[1]

        for obstacle in state.obstacles: # Collision with all obstacles
            if self.rect.colliderect(obstacle.rect):
                if self.yVel > 0: # Collision on the top of an object
                    self.coords[1] = obstacle.rect.top - self.rect.height
                    if self.jump and self.distanceWalked <= state.maxDistance: # Jumping should only be able to happen if you are on the floor
                        self.yVel = self.jumpVel
                    else:
                        self.yVel = 0

                elif self.yVel < 0: #Collision on the bottom of an object
                    self.coords[1] = obstacle.rect.bottom
                    self.yVel = 0

                self.rect.y = self.coords[1]

                if self.xVel > 0 and self.rect.right <= obstacle.rect.left: #Collision on the left of an object (The extra and statement is to make sure this only happens on x-based collisions and not y-based collisions
                    self.coords[0] = obstacle.rect.left - self.rect.width

                elif self.xVel < 0 and self.rect.left >= obstacle.rect.right: #Collision on the right of an object
                    self.coords[0] = obstacle.rect.right


                self.rect.x = self.coords[0]
        self.distanceWalked = math.sqrt((self.start[0] - self.coords[0])**2 + (self.start[1] - self.coords[1])**2)


        if self.rifleDown and self.rifleAngle < state.maxRifleAngle:
            self.rifleAngle += 0.3
            self.rifleTex = pygame.transform.rotate(self.startRifleTex, self.rifleAngle)

        elif self.rifleUp and self.rifleAngle > -1 * state.maxRifleAngle:
            self.rifleAngle -= 0.3
            self.rifleTex = pygame.transform.rotate(self.startRifleTex, self.rifleAngle)

    def out_of_bounds(self, state):
        if (self.rect.right > state.width) or (self.rect.left < 0) or (self.rect.bottom > state.height) or (self.rect.top < 0): #Check if out of bounds of map
            return [True, [-1 * (self.rect.right > state.width) + int(self.rect.left < 0), -1 * (self.rect.bottom > state.height) + int(self.rect.top < 0)]] #Dumb way of creating a vector that would be like [1, 0] or [-1, 0] to push the player back if they reach the edge using boolean logic and addition and stuff


        return [False]
        

        

        
        

    
