import pygame

#used to render an animation instead of a static image
class Animation():
    def __init__(self, images):
        self.imageList = images
        self.currentImage = 0
        self.counter = 0
        self.animationSpeed = 4

    def update(self):
        self.counter += 1
        if self.counter >= self.animationSpeed:
            self.counter = 0
            self.currentImage += 1
            if self.currentImage > len(self.imageList) - 1:
                self.currentImage = 0

    def draw(self, screen, x, y, isFlipped):

        if isFlipped:
            screen.blit(pygame.transform.flip(
                self.imageList[self.currentImage], True, False), (x, y))
        else:
            screen.blit(self.imageList[self.currentImage], (x, y))

    def setAnimationSpeed(self, speed):
        self.animationSpeed = speed

#detects collision between a player and array of platforms
class Collision():
    def __init__(self, player, platforms):
        self.player = player
        self.platforms = platforms
    
    def is_collision_x(self):
         # collision detection horizontally
        for p in self.platforms.get_platforms():
            if p.colliderect(self.player.get_hitbox()):
                self.player.set_is_colliding_x(True)
                break

    
    def is_colliding_y(self):
        #collision detection vertically
        for p in self.platforms.get_platforms():
            if p.colliderect(self.player.get_hitbox()):
                self.player.set_is_colliding_y(True)

                tempx, tempy = self.player.get_location()
                # if player collide with platform it sticks to the platform
                if(tempy < p[1]):
                    self.player.set_location(tempx,p[1] - 128)
                break