import pygame
import engine
import variables

class Player():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.height = 0
        self.width = 0
        self.accelaration_x = 0
        self.accelaration_y = 0
        self.speed_x = 0
        self.speed_y = 0
        self.is_on_ground = False
        self.direction = 'right'
        self.state = 'idle'
        self.player_idle_animation =engine.Animation([
            pygame.image.load("assets/player/skeleton_idle_00.png"),
            pygame.image.load("assets/player/skeleton_idle_01.png"),
            pygame.image.load("assets/player/skeleton_idle_02.png"),
            pygame.image.load("assets/player/skeleton_idle_03.png"),
            pygame.image.load("assets/player/skeleton_idle_04.png"),
            pygame.image.load("assets/player/skeleton_idle_05.png"),
            pygame.image.load("assets/player/skeleton_idle_06.png"),
            pygame.image.load("assets/player/skeleton_idle_07.png"),
            pygame.image.load("assets/player/skeleton_idle_08.png"),
            pygame.image.load("assets/player/skeleton_idle_09.png"),
            pygame.image.load("assets/player/skeleton_idle_10.png"),
        ] )
    
    def set_location(self, inputx, inputy):
        self.x = inputx
        self.y = inputy

    def get_location(self):
        return (self.x, self.y)
    
    def draw(self,screen):

        #changng the speed  of the player
        self.speed_x += self.accelaration_x

        #applying friction to the player
        if self.speed_x < 0:
            self.speed_x += variables.PLAYER_FEET_FRICTION
            if self.speed_x > 0:
                self.speed_x = 0
        elif self.speed_x > 0:
            self.speed_x -= variables.PLAYER_FEET_FRICTION
            if self.speed_x < 0:
                self.speed_x = 0

        #player max speed check
        if(self.speed_x > variables.PLAYER_MAX_SPEED):
            self.speed_x = variables.PLAYER_MAX_SPEED
        if(self.speed_x < -variables.PLAYER_MAX_SPEED):
            self.speed_x = -variables.PLAYER_MAX_SPEED

        #resetting the accelaration to 0 so that character only accelarates while the key is pressed
        self.accelaration_x = 0

        #changing the location based on the speed
        self.x += self.speed_x

        #drawing idle character
        if(self.state == 'idle'):
            if self.direction == 'right':
                self.player_idle_animation.draw(screen, self.x, self.y, False)
            else:
                self.player_idle_animation.draw(screen, self.x, self.y, True)

            self.player_idle_animation.update()
   
    def push_right(self):
        self.accelaration_x = variables.PLAYER_MOVEMENT_FORCE
        self.direction = 'right'
    
    def push_left(self):
        self.accelaration_x = -variables.PLAYER_MOVEMENT_FORCE
        self.direction = 'left'
        

