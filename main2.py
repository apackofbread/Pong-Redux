# Import the pygame library and initialise the game engine
import pygame
from paddle import Paddle
from ball import Ball


pygame.init()

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('Sounds/bgm.mp3')
pygame.mixer.music.play(-1) #-1 means loops for ever, 0 means play just once)
pygame.mixer.music.set_volume(0.2)


# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# Open a new window
width = 900
height = 600
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = height/2 - 50 #200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = width - 30 #670
paddleB.rect.y = height/2 - 50 #200

ball = Ball(WHITE,10,10)
ball.rect.x = width/2 - 5 #395
ball.rect.y = height/2 #originally 195 but 250 works aswell

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Add the paddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#Initialise player scores
scoreA = 0
scoreB = 0
 
background = pygame.image.load("image/pong.png")

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     carryOn=False  
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            while True: #Infinite loop that will be broken when the user press the space bar again
                font = pygame.font.Font(None, 72)
                text = font.render("PAUSE!!!", 1, (255, 0, 0))
                screen.blit(text, (350,250)) 
                
                pygame.display.flip()

                event = pygame.event.wait()
                pygame.mixer.music.pause()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    pygame.mixer.music.play()
                    break #Exit infinite loop

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    # --- Game logic should go here
    all_sprites_list.update()
    
    #Check if the ball is bouncing against any of the 4 walls:
    #Bouncing against the right wall
    if ball.rect.x>=(width-10):
        scoreA+=1
        effect = pygame.mixer.Sound('Sounds/point.wav')
        effect.play()
        effect.set_volume(0.5)
        ball.velocity[0] = -ball.velocity[0]

    #Bouncing against the left wall
    if ball.rect.x<=0:
        scoreB+=1
        effect = pygame.mixer.Sound('Sounds/point.wav')
        effect.play()
        effect.set_volume(0.5)
        ball.velocity[0] = -ball.velocity[0]

    #Bouncing against the bottom wall
    if ball.rect.y>(height-10):
        ball.velocity[1] = -ball.velocity[1]

    #Bouncing against the top wall
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]

    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        effect = pygame.mixer.Sound('Sounds/hit.wav')
        effect.play()
        ball.bounce()
 
    # --- Drawing code should go here
    # First, clear the screen to black. 
    screen.fill(BLACK)

    #Draw the Background
    screen.blit(background, (45, height/2 - 150))

    #Draw the net
    pygame.draw.line(screen, WHITE, [width/2 - 1, 0], [width/2 - 1, height], 5)
    
    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen)

    #Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (width/2 - 100,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (width/2 + 70 ,10))


 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()