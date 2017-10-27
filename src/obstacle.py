import pygame

class Obstacle: #Generic obstacle class that takes a texture for the start, end and middle of the obstacle
    def __init__(self, startTex, midTex, endTex, width, x, y):
        self.coords = [self.x, self.y]
        self.startTex = pygame.image.load(startTex) # Load textures
        self.midTex = pygame.image.load(midTex)
        self.endTex = pygame.image.load(endTex)
        
        self.rect = pygame.Rect(x, y, width * self.startTex.get_rect().width, self.startTex.get_rect().height) #Creates a rect for the obstacle
        
        
