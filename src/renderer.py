import pygame


class Renderer:  # Renderer class that renders the screen
    def __init__(self):
        pass

    def render(self, state):

        state.screen.fill((0, 255, 255)) #Temporary, this is just a blue background for now so you can see the man

        if len(state.particles) != 0:
            for particle in state.particles:
                pygame.draw.rect(state.screen, particle.colour, particle.rect)

        
        for man in state.men:
            state.screen.blit(man.tex, (man.coords[0] + state.camera.x, man.coords[1] + state.camera.y)) #Blit all the men and then the current man
            pygame.draw.rect(state.screen, (0, 0, 0),
                             pygame.Rect(man.coords[0] - ((man.healthBarWidth - man.rect.width)/2) + state.camera.x - 1,
                                        man.coords[1] - 10 + state.camera.y - 1,
                                         man.healthBarWidth + 2,
                                         7))

                                                                    
            pygame.draw.rect(state.screen, (255, 0, 0),
                             pygame.Rect(man.coords[0] - ((man.healthBarWidth - man.rect.width)/2) + state.camera.x, #Red
                                         man.coords[1] - 10 + state.camera.y,
                                         man.healthBarWidth,
                                         5))

            if man.health:
                pygame.draw.rect(state.screen, (0, 255, 0),
                                 pygame.Rect(man.coords[0] - ((man.healthBarWidth - man.rect.width)/2) + state.camera.x,  #green
                                             man.coords[1] - 10 + state.camera.y,
                                             (man.health/man.maxHealth) * man.healthBarWidth,
                                             5))

            

        if state.currentMan.flip:
            state.screen.blit(pygame.transform.flip(state.currentMan.tex, True, False), (state.currentMan.coords[0] + state.camera.x, state.currentMan.coords[1] + state.camera.y))
        else:
            state.screen.blit(state.currentMan.tex, (state.currentMan.coords[0] + state.camera.x, state.currentMan.coords[1] + state.camera.y))


        pygame.draw.rect(state.screen, (0, 0, 0),
                         pygame.Rect(state.currentMan.coords[0] - ((state.currentMan.healthBarWidth - state.currentMan.rect.width)/2) + state.camera.x - 1,
                                     state.currentMan.coords[1] - 10 + state.camera.y - 1,
                                     state.currentMan.healthBarWidth + 2,
                                     7))
        pygame.draw.rect(state.screen, (255, 0, 0),
                         pygame.Rect(state.currentMan.coords[0] - (state.currentMan.healthBarWidth - state.currentMan.rect.width)/2 + state.camera.x,
                                     state.currentMan.coords[1] - 10 + state.camera.y,
                                     state.currentMan.healthBarWidth,
                                     5))

        if state.currentMan.health:
            pygame.draw.rect(state.screen, (0, 255, 0),
                             pygame.Rect(state.currentMan.coords[0] - (state.currentMan.healthBarWidth - state.currentMan.rect.width)/2 + state.camera.x,
                                         state.currentMan.coords[1] - 10 + state.camera.y,
                                         (state.currentMan.health/state.currentMan.maxHealth) * state.currentMan.healthBarWidth,
                                         5))


        for obstacle in state.obstacles:
            state.screen.blit(obstacle.startTex, (obstacle.coords[0] + state.camera.x, obstacle.coords[1] + state.camera.y))
            for section in range(1, obstacle.width - 1):
                state.screen.blit(obstacle.midTex, (obstacle.coords[0]  + (obstacle.texWidth * section) + state.camera.x, obstacle.coords[1] + state.camera.y))
            state.screen.blit(obstacle.endTex, (obstacle.coords[0] + (obstacle.texWidth * (obstacle.width - 1)) + state.camera.x, obstacle.coords[1] + state.camera.y))

        if state.currentMan.fired:
            state.screen.blit(state.currentMan.bullet.tex, (state.currentMan.bullet.x + state.camera.x, state.currentMan.bullet.y + state.camera.y))
        
        for cloud in state.clouds:
            state.screen.blit(cloud.cloudTex, (cloud.coords[0] + state.camera.x, cloud.coords[1] + state.camera.y))
        if state.mode[2]:
            if state.currentMan.flip:
                state.screen.blit(pygame.transform.flip(state.currentMan.rifleTex, True, False), (state.currentMan.coords[0] - state.currentMan.rifleWidth - 5 + state.camera.x, state.currentMan.coords[1] - state.currentMan.rifleWidth/2 - 5 + state.camera.y))
            else:
                state.screen.blit(state.currentMan.rifleTex, (state.currentMan.coords[0] - state.currentMan.rifleWidth + 5 + state.camera.x, state.currentMan.coords[1] - state.currentMan.rifleWidth/2 - 5 + state.camera.y))

            
        

        pygame.display.flip()
