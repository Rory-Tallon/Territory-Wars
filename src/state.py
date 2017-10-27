import pygame

class State: #State class that holds all information about the game


    def __init__(self, screenX, screenY):
        self.gameOver = False
        self.men = [] #List that will store all the men apart from the current man
        self.screen = pygame.display.set_mode((screenX, screenY))
        self.width, self.height = screenX, screenY
        self.currentMan = None
        self.obstacles = []

        self.gravity = 4

        #mode[0] = movement
        #mode[1] = grenade
        #mode[2] = rifle
        #mode[3] = boot
        self.mode = [False, False, False, False] #Stores which mode the player is currently in
