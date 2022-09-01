import pygame
import random

BLACK = (0,0,0)
list_color= [(255,255,255),(255,0,0),(0,255,0),(0,0,255)]

class Ball(pygame.sprite.Sprite):

    def __init__(self, width=10, height=10):

        super().__init__()
        self.color =(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.image = pygame.Surface([width, height])
        self.image.fill((255,0,0,30))
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, self.color, [0,0,width,height])

        x,y = 0,0
        while x==0 or y==0:
            x = random.randint(-8,8)
            y = random.randint(-8,8)

        self.velocity = [x,y]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.randint(0,8)
