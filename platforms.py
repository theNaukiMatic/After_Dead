import pygame
import variables

class Platforms ():
    def __init__(self):
        self.platform_array = []
    
    def add_platform(self, x, y, w, h):
        temp = pygame.Rect(x, y, w, h)
        self.platform_array.append(temp)
    
    def draw(self, screen):
        for p in self.platform_array:
            pygame.draw.rect(screen, variables.GROUND_COLOR, p)
        
    def get_platforms(self):
        return self.platform_array