import pygame
import camera

class State: #State class that holds all information about the game


    def __init__(self, screenX, screenY):
        self.gameOver = False
        self.men = [] #List that will store all the men apart from the current man
        self.screen = pygame.display.set_mode((screenX, screenY))
        self.width = screenX
        self.height = screenY - 100
        self.currentMan = None
        self.maxDistance = 1000
        self.maxRifleAngle = 30
        self.obstacles = []
        self.clouds = []

        self.particles = []

        self.bulletDamage = 15
        
        self.camera = camera.Camera(0,0)

        self.gravity = 1

        #mode[0] = movement
        #mode[1] = grenade
        #mode[2] = rifle
        #mode[3] = boot
        self.mode = [False, False, False, False] #Stores which mode the player is currently in
