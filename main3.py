# Import the pygame library and initialise the game engine
import pygame
from paddle import Paddle
from ball2 import Ball
import time
import random

def text_display(text, text_pos, font = None, font_size = 20, font_location = 0, text_color = (255,255,255)):
    if font_location == 0:
        Fnt = pygame.font.SysFont(font, font_size)
    else :
        Fnt = pygame.font.Font(font_location, font_size)

    txt = Fnt.render(text, True, text_color)
    screen.blit(txt, text_pos)
    pygame.display.update()


def reset_all_values():
    global scoreA
    global scoreB
    scoreA = 0
    scoreB = 0

    paddleA.rect.x = 20
    paddleA.rect.y = height/2 - 50 #200
 
    paddleB.rect.x = width - 30 #670
    paddleB.rect.y = height/2 - 50 #200

    ball.rect.x = width/2 - 5 #395
    ball.rect.y = height/2 #originally 195 but 250 works aswell

    all_sprites_list.update()
    
    
    
pygame.init()

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('Sounds/bgm.mp3')
pygame.mixer.music.play(-1) #-1 means loops for ever, 0 means play just once)
pygame.mixer.music.set_volume(0.2)

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BAll_COLOR = (255,255,255)
list_color= [(255,255,255),(255,0,0),(0,255,0),(0,0,255)]

# Open a new window
width = 900
height = 600
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong Remastered")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = height/2 - 50 #200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = width - 30 #670
paddleB.rect.y = height/2 - 50 #200

ball = Ball(10,10)
ball.rect.x = width/2 - 5 #395
ball.rect.y = height/2 #originally 195 but 250 works aswell

#load sounds
point_sound = pygame.mixer.Sound('Sounds/point.wav')
hit_sound = pygame.mixer.Sound('Sounds/hit.wav')
win_sound = pygame.mixer.Sound('Sounds/applause.mp3')
start_sound = pygame.mixer.Sound('Sounds/begin_retro.wav')

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Add the paddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
# Add the ball to the list of sprites
all_sprites_list.add(ball)

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#Initialise player scores
scoreA = 0
scoreB = 0
max_score = 5 # setting max_score


background = pygame.image.load("image/pong.png")
intro_bg = pygame.image.load("image/background.jpg")
intro_bg = pygame.transform.scale(intro_bg, (900, 600))
game_state = "INTRO"
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     carryOn=False

        if game_state == "INTRO":
            screen.blit(intro_bg, (0,0))
            text_display(font = 'Minecraft', font_size = 50, font_location="fonts/Minecraft.ttf", text="PONG REMASTERED" , text_color = (255,255,255), text_pos = (220,70))
            text_display(font = 'Brush Script MT Italic', font_location="fonts/Minecraft.ttf",font_size = 30, text="\'Classics Never Dies\'" , text_color = (255,255,255), text_pos = (350,130))
            text_display(font = 'Consolas', font_size = 25, text="INSTRUCTIONS" , text_color = (255,255,255), text_pos = (100,300))
            text_display(font = 'Consolas', font_size = 25, text="1) The Player who first to score 2 points WINS" , text_color = (255,255,255), text_pos = (100,350))
            text_display(font = 'Consolas', font_size = 25, text="2) Press SPACE to pause" , text_color = (255,255,255), text_pos = (100,400))

            font = pygame.font.SysFont('Consolas', 30)
            text = font.render("HIT SPACE TO START", True, BLACK, WHITE)
            textRect = text.get_rect()
            textRect.center = (475,510)
            screen.blit(text, textRect)
            pygame.display.update()
            
            while True:
                event = pygame.event.wait()
                if event.type == pygame.QUIT:
                    pygame.quit()
                   # sys.exit()
                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE :
                    
                    start_sound.play()
                    game_state = "Game"
                    reset_all_values()
                    break
            

        if scoreA == max_score or scoreB==max_score:
            while True:
                if scoreA == max_score:
                    text_display(font = 'Minecraft', font_size = 50, font_location = "fonts/Minecraft.ttf", text="LEFT WINS" , text_color = (255,255,255), text_pos = (80,250))
                   
                elif scoreB == max_score:
                    text_display(font = 'Minecraft', font_size = 50, font_location = "fonts/Minecraft.ttf", text="RIGHT WINS" , text_color = (255,255,255), text_pos = (470,250))
                    
                
                # text_display(font = None, font_size = 20, (optional)font_location = 0, text, text_color = (255,255,255) text_pos)
                text_display(font = 'Minecraft', font_size = 30, font_location = 0, text="Press <SPACE> to restart Game" , text_color = (255,255,255), text_pos = (500,550))

                
                win_sound.play()

                waiting =True
                while waiting:
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                            waiting = False
                            reset_all_values()
                            
                            
                if waiting == False:
                    break
                

                
                #if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # setting default values
                       

             
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            while True: #Infinite loop that will be broken when the user press the space bar again
                font = pygame.font.Font(None, 140)
                text = font.render("<PAUSE>", 1, (255, 255, 255))
                screen.blit(text, (230,250))
                
                event = pygame.event.wait()
                pygame.mixer.music.pause()
                pygame.display.flip()
                
                if event.type == pygame.QUIT: # If user clicked close
                    carryOn = False
                    break
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
    if ball.rect.x>=(width+10):
        scoreA+=1
        point_sound.play()
        point_sound.set_volume(0.5)
        ball.rect.x=450
        ball.rect.y=300
        ball.velocity[0] = -ball.velocity[0]

    #Bouncing against the left wall
    if ball.rect.x<=(-10):
        scoreB+=1
        
        point_sound.play()
        point_sound.set_volume(0.5)
        ball.rect.x=450
        ball.rect.y=300
        ball.velocity[0] = -ball.velocity[0]
        
        

    #Bouncing against the bottom wall
    if ball.rect.y>(height-10):
        ball.velocity[1] = -ball.velocity[1]

    #Bouncing against the top wall
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]

    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
    #if pygame.Rect.colliderect(ball, paddleA) or pygame.Rect.colliderect(ball, paddleB)
        hit_sound.play()
        ball.bounce()
        #ball.color=random.choice(list_color)
        #ball = Ball(10,10)
        
        
 
    # --- Drawing code should go here
    # First, clear the screen to black. 
    screen.fill(BLACK)

    #Draw the Background
    screen.blit(background, (50,150))

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
