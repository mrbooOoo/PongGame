import pygame, sys

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

# Define the structures needed, ball, player and opponent bars
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30) #defining a rect with 30x30 centered in the screen
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)
midline = pygame.Rect(screen_width/2, 0, 1, screen_height)

#Definition of colors
bg_color = pygame.Color('grey12')
grey = (200, 200, 200)

#Ball speed
ball_speed_x = 7
ball_speed_y = 7

def ball_animation():
    global ball_speed_x, ball_speed_y

    #Ball Speed
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #Barriers for the board
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1  #inverse movement of y
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1  #inverse movement of x
    
    #Collisions with the bars
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

while True:
    #Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Visuals / Drawing the structures
    screen.fill(bg_color) #filling the color 'grey12' for the background (bg)
    pygame.draw.rect(screen, grey, player)
    pygame.draw.rect(screen, grey, opponent)
    pygame.draw.ellipse(screen, grey, ball)
    pygame.draw.rect(screen, grey, midline)

    #Running ball animation function
    ball_animation()

    #Updating the window 
    pygame.display.flip()
    clock.tick(60)
