import pygame
import renderer
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
        self.player_animation =renderer.Animation([
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
        self.player_animation.draw(screen, self.x, self.y, False)
        self.player_animation.update()