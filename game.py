# game physics

GRAVITY, FLAP_SPEED = 0.3, 7

def step(bird_y, bird_velo, flap):
    if flap:
        bird_velo = FLAP_SPEED
    bird_velo -= GRAVITY
    bird_y -= bird_velo
    return bird_y, bird_velo