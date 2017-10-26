import pygame
import state
import man
import renderer

manTex = "..\\res\\man.png"

state = state.State(1024, 650)
state.men.append(man.Man(100, 100, manTex))
state.men.append(man.Man(400, 400, manTex))
state.currentMan = state.men.pop()
renderer = renderer.Renderer()


def key_callback(state):
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
                if event.key == pygame.K_2: #Halt and end movement
                    state.currentMan.rightDown = False
                    state.currentMan.leftDown = False
                    state.mode[0] = False

            if event.type == pygame.KEYUP: #Stop moving
                if event.key == pygame.K_RIGHT:
                    state.currentMan.rightDown = False
                if event.key == pygame.K_LEFT:
                    state.currentMan.leftDown = False


while not state.gameOver:
    key_callback(state)

    state.currentMan.update(state)


    renderer.render(state)

    pygame.display.update()
    
