import pygame
import sys

pygame.init()

screen= pygame.display.set_mode((600, 600))
pygame.display.set_caption("Draw Circle at mouse position")

WHT, BLU, RED, BLK = (255,255,255), (0,200,255), (255,0,0), (0,0,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    screen.fill(BLK)
    

    if pygame.mouse.get_pressed()[0]:  # Check if the left mouse button is pressed
        pos = pygame.mouse.get_pos()
        # Uncomment the line below to draw a circle at the mouse position
        pygame.draw.circle(screen, (0, 255, 0), pos, 20)  

    pygame.display.flip()