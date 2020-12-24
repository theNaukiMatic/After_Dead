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
        self.accelaration_y = variables.GRAVITY
        self.speed_x = 0
        self.speed_y = 0
        self.is_on_ground = False
        self.direction = 'right'
        self.state = 'idle'

        #player's idle animation
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

        #player's walking animations
        self.player_walking_animation = engine.Animation([
            pygame.image.load("assets/player/skeleton_walk_00.png"),
            pygame.image.load("assets/player/skeleton_walk_01.png"),
            pygame.image.load("assets/player/skeleton_walk_02.png"),
            pygame.image.load("assets/player/skeleton_walk_03.png"),
            pygame.image.load("assets/player/skeleton_walk_04.png"),
            pygame.image.load("assets/player/skeleton_walk_05.png"),
            pygame.image.load("assets/player/skeleton_walk_06.png"),
            pygame.image.load("assets/player/skeleton_walk_07.png"),
            pygame.image.load("assets/player/skeleton_walk_08.png"),
            pygame.image.load("assets/player/skeleton_walk_09.png"),
            pygame.image.load("assets/player/skeleton_walk_10.png"),
            pygame.image.load("assets/player/skeleton_walk_11.png"),
            pygame.image.load("assets/player/skeleton_walk_12.png"),      
        ])


    #to manualy set the player's location (spawning, or maybe teleportaion feature)
    #also usefull to stick the player perfectly to the ground after a jump
    def set_location(self, inputx, inputy):
        self.x = inputx
        self.y = inputy

    def get_location(self):
        return (self.x, self.y)
    
    def update(self, platforms):
        #set default state as idle
        self.state = 'idle'
        if self.speed_x != 0:
            self.state = 'walking'
        
        self.is_on_ground = False

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


        #horizontal movement
        self.speed_x += self.accelaration_x
        new_x = self.x + self.speed_x

        hitbox_x = pygame.Rect(new_x, self.y, 96, 128)
        is_colliding_x = False

        #horizontal collision detection
        for p in platforms.get_platforms():
            if(p.colliderect(hitbox_x)):
                is_colliding_x = True
                self.speed_x *= (-1)
                break
        
        if is_colliding_x == False:
            self.x = new_x

        #vertical movement
        self.speed_y += self.accelaration_y
        new_y = self.y + self.speed_y

        hitbox_y = pygame.Rect(self.x, new_y, 96, 128)
        is_colliding_y = False

        #vertical collision detection
        for p in platforms.get_platforms():
            if(p.colliderect(hitbox_y)):
                is_colliding_y = True
                self.speed_y = 0

                #stick the player to the ground in case of a collision
                if(self.y < p[1]):
                    self.y  = p[1] - 128
                    self.is_on_ground = True
                
                break
        
        if(is_colliding_y == False):
            self.y = new_y
    


    def draw(self,screen):

        #drawing idle character
        if(self.state == 'idle'):
            if self.direction == 'right':
                self.player_idle_animation.draw(screen, self.x, self.y, False)
            else:
                self.player_idle_animation.draw(screen, self.x, self.y, True)

            self.player_idle_animation.update()
        
        #drawing the walking character
        elif(self.state == 'walking'):
            if self.direction == 'right':
                self.player_walking_animation.draw(screen, self.x, self.y, False)
            else:
                self.player_walking_animation.draw(screen, self.x, self.y, True)
            self.player_walking_animation.setAnimationSpeed(14/(abs(self.speed_x)+1))
            self.player_walking_animation.update()
   
    def push_right(self):
        self.accelaration_x = variables.PLAYER_MOVEMENT_FORCE
        self.direction = 'right'
    
    def push_left(self):
        self.accelaration_x = -variables.PLAYER_MOVEMENT_FORCE
        self.direction = 'left'
    
    def jump(self):
        if(self.is_on_ground):
            self.speed_y = -variables.JUMP_SPEED

    def get_hitbox(self):
        return pygame.Rect(self.x, self.y, 96, 128)
    
    def get_is_on_ground(self):
        return is_on_ground