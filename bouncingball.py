import pygame, sys, random

pygame.init()

size= width, height = 600, 600
speed = [2, 2]
black = (0, 0, 0)

Screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing Ball")

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ballrect = ballrect.move(speed)
    
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    Screen.fill(black)
    Screen.blit(ball, ballrect)
    pygame.display.flip()
    pygame.time.delay(10)
