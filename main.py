import pygame
import player_data
import variables

#----
#INIT
#----
pygame.init()
screen = pygame.display.set_mode(variables.SCREEN_SIZE)
pygame.display.set_caption("AFTER DEAD")
clock = pygame.time.Clock()
screen_width = screen.get_width()
screen_height = screen.get_height()

#PLAYER
player = player_data.Player()


#--------
#GAMELOOP
#--------
isGameRunning = True
while(isGameRunning):


    #-----
    #INPUT
    #-----
    for event in pygame.event.get():
        # quit button
        if(event.type == pygame.QUIT):
            isGameRunning = False


    #---------
    #RENDERING
    #---------
    screen.fill(variables.BACKGROUND_COLOR)
    player.draw(screen)

 


    # Screen
    pygame.display.flip()
    clock.tick(variables.FPS)

    

pygame.quit()