import pygame

class Particle:
    def __init__(self, colour, xVel, yVel, x, y, gravity):
        self.colour = colour
        self.xVel = xVel
        self.yVel = yVel
        self.x = x
        self.y = y

        self.gravity = gravity

        self.rect = pygame.Rect(x, y, 1, 1)


    def out_of_bounds(self, state):
        if self.x > state.width or self.x < 0 or self.y > state.height or self.y < 0:
            return True
        return False

    def update(self, state):
        self.x += self.xVel
        self.y += self.yVel
        self.yVel += self.gravity/60

        self.rect.left = self.x
        self.rect.top = self.y
        
        if self.out_of_bounds(state):
            state.particles.remove(self)
