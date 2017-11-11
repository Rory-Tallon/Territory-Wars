import pygame
import math
import state
import man
import obstacle
import renderer
import cloud
import tex_names


state = state.State(1024, 650) #Initialise state with with dimensions of 1024x650
state.men.append(man.Man(400, 434, tex_names.manTex, tex_names.rifleTex, tex_names.manWalk)) #Create a man 
state.currentMan = state.men.pop() #Set the current man to be the last man added


state.clouds.append(cloud.Cloud(200, 200, tex_names.cloudTex))
state.clouds.append(cloud.Cloud(400, 130, tex_names.cloudTex))
state.clouds.append(cloud.Cloud(700, 240, tex_names.cloudTex))


state.obstacles.append(obstacle.Obstacle(0, 434, tex_names.grassTexs[0], tex_names.grassTexs[1], tex_names.grassTexs[2], 64))

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
                    state.currentMan.flip = True
                    
                if event.key == pygame.K_LEFT: #Move left
                    state.currentMan.leftDown = True
                    state.currentMan.flip = False
                    
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
                

        if state.mode[2]: #Rifle mode
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: #Point up
                    state.currentMan.rifleUp = True
                if event.key == pygame.K_DOWN: #Point down
                    state.currentMan.rifleDown = True
                    
                if event.key == pygame.K_RIGHT:
                    state.currentMan.flip = True
                if event.key == pygame.K_LEFT:
                    state.currentMan.flip = False
        
            if  event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    state.currentMan.rifleUp = False
                if event.key == pygame.K_DOWN:
                    state.currentMan.rifleDown = False



while not state.gameOver: #Main loop
    key_callback(state) #Check input

    state.currentMan.update(state) #Update the current man
    for cloud in state.clouds:
        cloud.update(state)


    renderer.render(state) #Render the state

    pygame.display.update() #Update the screen
