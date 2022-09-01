#importing pygame and initialising the game engine/libraries
import pygame
from paddle import Paddle

pygame.init()

#defining some colours to use later
BLACK = (0,0,0)
WHITE = (255,255,255)

#new window with given size and caption
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('pong')

#making 2 paddle objects
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

#List containing all the sprites we are using
all_sprites_list = pygame.sprite.Group()

#Adding paddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)

#boolean variable that will keep the main loop running till we want it to stop
carryON = True

#clock variable to control how fast the screen updates (basically fps)
clock = pygame.time.Clock()

#--------------Main program loop-----------------
while carryON:
    #---------Main Event Loop--------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryON = False
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryON = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    #---------Game Logic Here--------------------
    all_sprites_list.update()
    
    #---------Drawing Code Here------------------
    #clearing the screen to black first
    screen.fill(BLACK)
    #drawing the net (by splitting the screen into two parts)
    pygame.draw.line(screen,WHITE, [349,0], [349,500], 5)

    #---------Updating the stream with what we've drawn until now
    pygame.display.flip()

    #---------Limiting the fps to 60 frames per second
    clock.tick(60)

#After the main program loop is over we can stop the game engine
pygame.quit()

