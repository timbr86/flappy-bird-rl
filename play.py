# actual playable game using physics defined in game.py

import pygame
from game import FlappyGame, SCREEN_HEIGHT, SCREEN_WIDTH

# pygame setup
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

game = FlappyGame()

running = True

while running:
    flap = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            flap = True
    game.step(flap)
    screen.fill((135, 206, 235))    # sky
    pygame.draw.circle(screen, (255, 220, 0), (100, int(game.bird_y)), 15)    # bird

    for pipe in game.pipes:
        for rectangle in pipe.rectangles():    #draw bottom and top rect to form a pipe
            pygame.draw.rect(screen, (0, 255, 100), rectangle)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()