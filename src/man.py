import math
import pygame
from pygame.locals import *

class Man:

    def __init__(self, x, y, tex):
        self.coords = [x, y]
        self.start = self.coords #Can be used for finding distance from start of turn
        
        self.xVel = 0
        self.yVel = 0

        self.maxXVel = 0.2 
        
        self.leftDown = False
        self.rightDown = False

        self.distanceWalked = 0

        self.tex = pygame.image.load(tex) #Load the image
        self.rect = self.tex.get_rect() #Create a rectangle with the correct width and height corresponding to the texture
        self.rect.x, self.rect.y = self.coords[0], self.coords[1] #Move the rectangle so it is in the correct position
        

    def update(self, state): #Updates the man based on velocities, ensures he does not got out of bounds
        if self.leftDown: #Horizontal movement
            self.xVel = -1 * self.maxXVel
        elif self.rightDown:
            self.xVel = self.maxXVel
        else:
            self.xVel = 0

        self.coords[0] += self.xVel #Actually move the man
        self.coords[1] += self.yVel

        oob = self.out_of_bounds(state) #Check if the man is out of bounds

        if oob[0]:
            self.coords[0] += oob[1][0] #If they are out of bounds, shift them back into the  screen
            self.coords[1] += oob[1][1]
            self.rect.x, self.rect.y = self.coords[0], self.coords[1] #Move the rectangle accordingly
        else:
            self.rect.x, self.rect.y = self.coords[0], self.coords[1]

    def out_of_bounds(self, state):
        if (self.rect.right > state.width) or (self.rect.left < 0) or (self.rect.bottom > state.height) or (self.rect.top < 0): #Check if out of bounds of map
            return [True, [-1 * (self.rect.right > state.width) + int(self.rect.left < 0), -1 * (self.rect.bottom > state.height) + int(self.rect.top < 0)]] #Dumb way of creating a vector that would be like [1, 0] or [-1, 0] to push the player back if they reach the edge using boolean logic and addition and stuff


        return [False]
        

        

        
        

    
