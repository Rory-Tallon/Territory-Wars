import pygame

class Obstacle: #Generic obstacle class that takes a texture for the start, end and middle of the obstacle
    def __init__(self, x, y, startTex, midTex, endTex, width):
        self.coords = [x, y]
        self.startTex = pygame.image.load(startTex) # Load textures
        self.midTex = pygame.image.load(midTex)
        self.endTex = pygame.image.load(endTex)
        self.texWidth = self.startTex.get_rect().width
        self.width = width
        
        self.rect = pygame.Rect(x, y, width * self.texWidth, self.startTex.get_rect().height) #Creates a rect for the obstacle
        
        
