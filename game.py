# game physics and logic

import random

GRAVITY, FLAP_SPEED = 0.3, 7
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 800
PIPE_WIDTH, GAP_HEIGHT, PIPE_SPEED = 75, 125, 2
MARGIN = 50


class Pipe:
    def __init__(self, gap_y):
        self.x = SCREEN_WIDTH
        self.gap_y = gap_y

    def move(self):
        self.x -= PIPE_SPEED

    def rectangles(self):
        top = (self.x, 0, PIPE_WIDTH, self.gap_y) 
        bottom = (self.x, 0 + self.gap_y + GAP_HEIGHT,
                   PIPE_WIDTH, SCREEN_HEIGHT - self.gap_y - GAP_HEIGHT)
        
        return top, bottom


class FlappyGame:
    def __init__(self):
        self.rng = random.Random()
        self.reset()

    def reset(self):
        self.bird_y = 400
        self.bird_velo = 0
        pipe_gap_y = self.rng.randint(MARGIN, SCREEN_HEIGHT - GAP_HEIGHT - MARGIN)
        self.pipe = Pipe(pipe_gap_y)

    def step(self, flap):
        if flap:
            self.bird_velo = FLAP_SPEED
        self.bird_velo -= GRAVITY
        self.bird_y -= self.bird_velo
        self.pipe.move()


