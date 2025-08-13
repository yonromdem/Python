import pygame
import random
import sys

pygame.init()
W, H = 600, 600
screen=pygame.display.set_mode((W , H))
pygame.display.set_caption("Welcome to Falling Blocks")

WHT, BLU, RED, BLK = (255,255,255), (0,200,255), (255,0,0), (0,0,0)

clock=pygame.time.Clock()
font = pygame.font.SysFont(None, 26)

paddle=pygame.Rect(W // 2, H - 20, 120, 10)

block = pygame.Rect(random.randint(0, W - 20), 2, 20, 20)

b_speed= 5

score = 0

run =  True
while run:
    screen.fill(BLK)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0 :
        paddle.move_ip(-8, 0)
    if keys[pygame.K_RIGHT] and paddle.right < W :
        paddle.move_ip(8,0)
    
    block.y = block.y + b_speed

    if block.colliderect(paddle):
        block.y = 0
        block.x = random.randint(0,W-20)
        score = score + 1
        b_speed = b_speed + 0.1
    
    if block.y > H:
        game_over = font.render(f"Game Over! Final Score : {score}", True, RED)
        screen.blit(game_over, (W // 2 - 150, H // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        run = False
    
    pygame.draw.rect(screen, WHT, paddle)
    pygame.draw.rect(screen, BLU, block)

    score_text =  font.render(f"Score {score}", True, WHT)
    screen.blit (score_text, (10,10))

    pygame.display.flip()
    clock.tick(60)

    