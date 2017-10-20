import pygame

class State:

    def __init__(self, screenX, screenY):
        self.gameOver = False
        self.men = []
        self.screen = pygame.display.set_mode((screenX, screenY))
        self.width, self.height = screenX, screenY
        self.currentMan = None


        #mode[0] = movement
        #mode[1] = grenade
        #mode[2] = rifle
        #mode[3] = boot
        self.mode = [False, False, False, False]
