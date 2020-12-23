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

    key_pressed = pygame.key.get_pressed()

    #move player left
    if(key_pressed[pygame.K_LEFT]):
        player.push_left()

    #move player right
    if(key_pressed[pygame.K_RIGHT]):
        player.push_right()


    #---------
    #RENDERING
    #---------
    screen.fill(variables.BACKGROUND_COLOR)
    player.draw(screen)

 


    # Screen
    pygame.display.flip()
    clock.tick(variables.FPS)

    

pygame.quit()