import pygame

class Renderer:  # Renderer class that renders the screen
    def __init__(self):
        pass

    def render(self, state):

        state.screen.fill((0, 255, 255)) #Temporary, this is just a blue background for now so you can see the man
        
        for man in state.men:
            state.screen.blit(man.tex, (man.coords[0], man.coords[1])) #Blit all the men and then the current man

        state.screen.blit(state.currentMan.tex, (state.currentMan.coords[0], state.currentMan.coords[1]))

        for obstacle in state.obstacles:
            state.screen.blit(obstacle.startTex, (obstacle.coords[0], obstacle.coords[1]))
            for section in range(1, obstacle.width - 1):
                state.screen.blit(obstacle.midTex, (obstacle.coords[0]  + (obstacle.texWidth * section), obstacle.coords[1]))
            state.screen.blit(obstacle.endTex, (obstacle.coords[0] + (obstacle.texWidth * (obstacle.width - 1)), obstacle.coords[1]))

        for cloud in state.clouds:
            state.screen.blit(cloud.cloudTex, (cloud.coords[0], cloud.coords[1]))



        pygame.display.flip()
