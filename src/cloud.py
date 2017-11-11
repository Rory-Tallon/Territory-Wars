import random
import pygame
class Cloud: #Scenery cloud class that moves horizontally by a random value and wraps across the screen
        def __init__(self, x, y, cloudTex):
            self.coords = [x, y]
            self.cloudTex = pygame.image.load(cloudTex)
            self.width = self.cloudTex.get_rect().width
            self.xVel = (random.random()) * 0.5 # Get a value between -1 and 1 for the x velocity

        def update(self, state):
            self.coords[0] += self.xVel #Move the cloud
            if self.coords[0] < 0 - self.width: # If the cloud moves off the left side, move it to the right
                self.coords[0] = state.width
            elif self.coords[0] > state.width: #If the cloud moves off the right side, move it to the left
                self.coords[0] = 0 - self.width
            

