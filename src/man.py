import math
import pygame
import bullet
import particle
from pygame.locals import *

class Man:

    def __init__(self, x, y, standingTex, rifleTex, walkAnim, holdRifleTex, bulletTex, manDead):
        self.coords = [x, y]
        self.start = [x, y] #Can be used for finding distance from start of turn
        
        self.xVel = 0
        self.yVel = 0

        self.maxXVel = 0.5
        self.jumpVel = -3/2
        
        self.leftDown = False
        self.rightDown = False
        self.jump = False

        self.rifleDown = False
        self.rifleUp = False
        self.rifleAngle = 0

        self.distanceWalked = 0

        self.health = 50
        self.maxHealth = 50

        self.healthBarWidth = 50
        

        self.tex = pygame.image.load(standingTex) #Load the image
        self.standingTex = pygame.image.load(standingTex)
        self.walkAnim = [pygame.image.load(frame) for frame in walkAnim]
        self.rect = self.tex.get_rect() #Create a rectangle with the correct width and height corresponding to the texture
        self.rect.x, self.rect.y = self.coords[0], self.coords[1] #Move the rectangle so it is in the correct position

        self.holdRifleTex = pygame.image.load(holdRifleTex)
        
        self.walkAnimationCounter = 0
        self.walkAnimationFrameTime = 30
        self.walkAnimationCounterCap = self.walkAnimationFrameTime * len(self.walkAnim)

        self.rifleTex_ = pygame.image.load(rifleTex) 
        self.rifleWidth, self.rifleHeight = self.rifleTex_.get_rect().width, self.rifleTex_.get_rect().height
        self.rifleTex = pygame.Surface((self.rifleWidth*2 + self.rect.width, self.rifleWidth*2 + self.rect.width), pygame.SRCALPHA)
        self.rifleTex.blit(self.rifleTex_, (0, (self.rifleWidth*2 + self.rect.width)/2))
        self.rifleRect = self.rifleTex.get_rect()
        self.startRifleTex = self.rifleTex.copy()

        self.deadTex = pygame.image.load(manDead)

        self.bulletTex = bulletTex
        self.bullet = None
        self.fired = False
        self.flip = False
        self.alive = True

        self.maxDeathTimer = 300
        self.deathTimer = self.maxDeathTimer


    def update(self, state): #Updates the man based on velocities, ensures he does not got out of bounds

        if self.alive:
            if self.distanceWalked <= state.maxDistance:
                if self.leftDown: #Horizontal movement
                    if self.walkAnimationCounter % self.walkAnimationFrameTime <= 0:
                        self.tex = self.walkAnim[self.walkAnimationCounter // self.walkAnimationFrameTime]
                    self.xVel = -1 * self.maxXVel
                    
                    self.walkAnimationCounter += 1

                    self.walkAnimationCounter = self.walkAnimationCounter % self.walkAnimationCounterCap
                    
                elif self.rightDown:
                    self.xVel = self.maxXVel

                    if self.walkAnimationCounter % self.walkAnimationFrameTime <= 0:
                        self.tex = self.walkAnim[self.walkAnimationCounter // self.walkAnimationFrameTime]
                    self.walkAnimationCounter += 1

                    self.walkAnimationCounter = self.walkAnimationCounter % self.walkAnimationCounterCap

                else:
                    self.xVel = 0
                    if self.tex != self.standingTex:
                        self.tex = self.standingTex
                        self.walkAnimationCounter = 0
            else:
                self.xVel = 0

            if state.mode[2] and self == state.currentMan:
                self.tex = self.holdRifleTex

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

                rot_image = pygame.transform.rotate(self.startRifleTex, self.rifleAngle)
                rot_rect = self.rifleRect.copy()
                rot_rect.center = rot_image.get_rect().center
                self.rifleTex = rot_image.subsurface(rot_rect).copy()
                
                #self.rifleTex = pygame.transform.rotate(self.startRifleTex, self.rifleAngle)

            elif self.rifleUp and self.rifleAngle > -1 * state.maxRifleAngle:
                self.rifleAngle -= 0.3
                rot_image = pygame.transform.rotate(self.startRifleTex, self.rifleAngle)
                rot_rect = self.rifleRect.copy()
                rot_rect.center = rot_image.get_rect().center
                self.rifleTex = rot_image.subsurface(rot_rect).copy()
                
                #self.rifleTex = pygame.transform.rotate(self.startRifleTex, self.rifleAngle)

            if self.health <= 0:
                self.alive = False
                self.health = 0
            
        else:

            
            if self.deathTimer == self.maxDeathTimer:

                self.coords[1] += (self.rect.height - self.deadTex.get_rect().height)

                self.tex = self.deadTex
            if self.deathTimer == 0:
                if self in state.men:
                    state.men.pop(state.men.index(self))
                else:
                    state.currentMan = None
            self.deathTimer -= 1

    def out_of_bounds(self, state):
        if (self.rect.right > state.width) or (self.rect.left < 0) or (self.rect.bottom > state.height) or (self.rect.top < 0): #Check if out of bounds of map
            return [True, [-1 * (self.rect.right > state.width) + int(self.rect.left < 0), -1 * (self.rect.bottom > state.height) + int(self.rect.top < 0)]] #Dumb way of creating a vector that would be like [1, 0] or [-1, 0] to push the player back if they reach the edge using boolean logic and addition and stuff


        return [False]

    def fire_rifle(self):
        self.bullet = bullet.Bullet(math.cos(math.radians(self.rifleAngle)) if self.flip else -1 * math.cos(math.radians(self.rifleAngle)),
                                    math.sin(math.radians(self.rifleAngle)),
                                    self.rifleTex.get_rect().left + self.coords[0] + self.rect.width/2,
                                    self.rifleTex.get_rect().top + self.coords[1] + self.rect.height/2,
                                    self.bulletTex,
                                    self.rifleAngle if self.flip else 180 - self.rifleAngle)
        self.fired = True
        print(self.rifleAngle)
    
                               
                               
        

        

        
        

    
