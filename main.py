import pygame
import player_data
import variables
import platforms

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

#PLATFORMS
platforms = platforms.Platforms()

platforms.add_platform(0,0, 50 ,50)


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
    
    #make player jump
    if(key_pressed[pygame.K_SPACE]):
        player.jump()


    #---------
    #RENDERING
    #---------
    screen.fill(variables.BACKGROUND_COLOR)
    player.draw(screen)
    platforms.draw(screen)

 


    # Screen
    pygame.display.flip()
    clock.tick(variables.FPS)

    

pygame.quit()