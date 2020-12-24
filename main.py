import pygame
import player_data
import variables
import platforms
import engine

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
platforms.add_platform(0,500, 960 ,40)
platforms.add_platform(0,400, 100 ,100)
platforms.add_platform(860,400, 100 ,100)

#Collision Engine
collision = engine.Collision(player, platforms)

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


    # collision.is_collision_x()
    # collision.is_colliding_y()
    player.update(platforms)
    #---------
    #RENDERING
    #---------
    screen.fill(variables.BACKGROUND_COLOR)
    platforms.draw(screen)
    player.draw(screen)

    # Screen
    pygame.display.flip()
    clock.tick(variables.FPS)

    

pygame.quit()