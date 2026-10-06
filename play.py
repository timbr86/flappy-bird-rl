# actual playable game using physics defined in game.py

import pygame
from game import step

# pygame setup
pygame.init()
screen = pygame.display.set_mode([500, 800])
clock = pygame.time.Clock()
y, vel = 400, 0

running = True

while running:
    flap = False
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            flap = True
    y, vel = step(y, vel, flap)
    screen.fill((135, 206, 235))    # sky
    pygame.draw.circle(screen, (255, 220, 0), (100, int(y)), 15)    # bird
    pygame.display.flip()
    clock.tick(60)