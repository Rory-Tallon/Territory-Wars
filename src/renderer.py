import pygame

class Renderer:
    def __init__(self):
        pass

    def render(self, state):

        state.screen.fill((0, 255, 255))
        
        for man in state.men:
            state.screen.blit(man.tex, (man.coords[0], man.coords[1]))

        state.screen.blit(state.currentMan.tex, (state.currentMan.coords[0], state.currentMan.coords[1]))



        pygame.display.flip()
