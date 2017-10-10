import pygame
import time
from pygame.locals import *


#Creates the screen
screen = pygame.display.set_mode((1024,650))
black = (164,237,92)

#Adds the sky and ground
background = pygame.image.load('sky.png')
screen.blit(background, (0,0))
man_pic = pygame.image.load('man.png')
pygame.display.flip()


x = 50
y = 488
manx = 0
def man(x,y):
    screen.blit(man_pic,(x, y))

#main game loop
game_over = False
while not game_over:
    
    #gets user to input movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                manx += 1
                man_pic = pygame.image.load('man.png')
            elif event.key == pygame.K_LEFT:
                manx -= 1
                man_pic = pygame.image.load('man.png')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                manx = 0


    x += manx
    y = 488
    man(x,y)
    
    #updates screen
    pygame.display.update()


pygame.quit()
quit()
