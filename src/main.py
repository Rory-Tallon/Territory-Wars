import pygame
import math
import state
import man
import obstacle
import renderer

manTex = "..\\res\\man.png" #Location of the man texture for easy use
grassTexs = ["..\\res\\grassStart.png", "..\\res\\grassMid.png", "..\\res\\grassEnd.png"]

state = state.State(1024, 650) #Initialise state with with dimensions of 1024x650
state.men.append(man.Man(100, 100, manTex))
state.men.append(man.Man(400, 400, manTex)) #Create two men
state.currentMan = state.men.pop() #Set the current man to be the last man added


state.obstacles.append(obstacle.Obstacle(0, 634, grassTexs[0], grassTexs[1], grassTexs[2], 64))

renderer = renderer.Renderer() #Create renderer


def key_callback(state): #Key callback function which handles all input
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Quits game
            state.gameOver = True
            pygame.quit()

        if not(any(state.mode)): #If not in any mode, then enter mode select
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    state.mode[0] = True
                elif event.key == pygame.K_2:
                    state.mode[1] = True
                elif event.key == pygame.K_3:
                    state.mode[2] = True
                elif event.key == pygame.K_4:
                    state.mode[3] = True
            
        if state.mode[0]: #Movement mode
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: #Move right
                    state.currentMan.rightDown = True
                if event.key == pygame.K_LEFT: #Move left
                    state.currentMan.leftDown = True
                if event.key == pygame.K_UP: #Jump
                    state.currentMan.jump = True
                if event.key == pygame.K_2: #Halt and end movement
                    state.currentMan.rightDown = False
                    state.currentMan.leftDown = False
                    state.mode[0] = False

            if event.type == pygame.KEYUP: #Stop moving
                if event.key == pygame.K_RIGHT:
                    state.currentMan.rightDown = False
                if event.key == pygame.K_LEFT:
                    state.currentMan.leftDown = False
                if event.key == pygame.K_UP:
                    state.currentMan.jump = False



while not state.gameOver: #Main loop
    key_callback(state) #Check input

    state.currentMan.update(state) #Update the current man


    renderer.render(state) #Render the state

    pygame.display.update() #Update the screen
    
