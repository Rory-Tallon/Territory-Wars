import pygame
import random
import particle
class Bullet:
    def __init__(self, xVel, yVel, x, y, tex, angle):
        self.xVel = xVel
        self.yVel = yVel

        self.x = x
        self.y = y

        self.tex = pygame.image.load(tex)
        self.rect = self.tex.get_rect()
        rot_image = pygame.transform.rotate(self.tex, angle)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        self.tex = rot_image.subsurface(rot_rect).copy()

    def update(self, state):

        if self.out_of_bounds(state):
            state.currentMan.fired = False
            state.currentMan.bullet = None

        for obstacle in state.obstacles:
            if self.rect.colliderect(obstacle.rect):
                state.currentMan.fired = False
                print("here")
                state.camera.shake(20)
                state.currentMan.bullet = None
                for x in range(30):
                    state.particles.append(particle.Particle((139, 69, 19),(random.random() - 0.5), -1 * (random.random()*2), self.x, self.y, state.gravity))

        for man in state.men:
            if self.rect.colliderect(man.rect):
                man.health -= state.bulletDamage
                state.currentMan.fired = False
                state.camera.shake(20)
                for x in range(30):
                    state.particles.append(particle.Particle((255, 0, 0),(random.random() - 0.5), -1 * (random.random()*2), self.x, self.y, state.gravity))
                
                state.currentMan.bullet = None
        
        
        self.x += self.xVel
        self.y += self.yVel

        self.rect.x, self.rect.y = self.x, self.y
        
    
    def out_of_bounds(self, state):
        if (self.rect.right > state.width) or (self.rect.left < 0) or (self.rect.bottom > state.height) or (self.rect.top < 0): #Check if out of bounds of map
            return True
        return False
