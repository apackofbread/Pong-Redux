import pygame

BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    #This is the paddle class and it is derived from the 'Sprite' class in pygame.
    #Child class of sprite class basically
    
    #The constructor for our Paddle class
    def __init__(self, color, width, height):
        #Sends a super call to the constructor of the parent class
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #drawing the paddle (a rectangle)
        pygame.draw.rect(self.image, color, [0,0,width,height])

        #Fetch the rectangle object that has dimensions of the image.
        self.rect = self.image.get_rect()
    
    def moveUp(self, pixels):
        self.rect.y -= pixels

        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels

        if self.rect.y > 500:
            self.rect.y = 500