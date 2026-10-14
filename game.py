# game physics and logic

import random
import collections


# game constants
GRAVITY, FLAP_SPEED = 0.3, 6
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 800
BIRD_RADIUS, BIRD_X = 15, 100
PIPE_WIDTH, GAP_HEIGHT, PIPE_SPEED = 75, 125, 2
MARGIN = 50


class Pipe:
    def __init__(self, gap_y):
        self.x = SCREEN_WIDTH
        self.gap_y = gap_y
        self.passed = False

    def move(self):
        self.x -= PIPE_SPEED

    def rectangles(self):   # create top and bottom rectangles to form full pipe
        top = (self.x, 0, PIPE_WIDTH, self.gap_y) 
        bottom = (self.x, self.gap_y + GAP_HEIGHT,
                   PIPE_WIDTH, SCREEN_HEIGHT - self.gap_y - GAP_HEIGHT)
        
        return top, bottom


class FlappyGame:
    def __init__(self):
        self.rng = random.Random()
        self.reset()

    def reset(self):    # game initial conditions
        self.bird_y = 400
        self.bird_velo = 0
        self.frame_counter = 0
        self.score = 0
        self.dead = False
        self.pipes = collections.deque()
        self.create_pipe()
        
    def create_pipe(self):
        pipe_gap_y = self.rng.randint(MARGIN, SCREEN_HEIGHT - GAP_HEIGHT - MARGIN)
        self.pipes.append(Pipe(pipe_gap_y))

    def bird_box(self):
        return (BIRD_X - BIRD_RADIUS, self.bird_y - BIRD_RADIUS,
                 BIRD_RADIUS * 2, BIRD_RADIUS * 2)

    def step(self, flap):
        if self.dead:
            return 
                
        if flap:
            self.bird_velo = FLAP_SPEED

        self.bird_velo -= GRAVITY
        self.bird_y -= self.bird_velo

        if self.bird_y - BIRD_RADIUS < 0:   # top border - keep bird under
            self.bird_y = BIRD_RADIUS
            self.bird_velo = 0

        if self.bird_y + BIRD_RADIUS >= SCREEN_HEIGHT:  # kill bird on floor
            self.dead = True

        if self.frame_counter == 200:   # send a new pipe every 200 frames
            self.create_pipe()
            self.frame_counter = 0

        for pipe in self.pipes:
            pipe.move()

        # check bird collision with pipes & if bird passed a new pipe
        bird_hit_box = self.bird_box()
        for pipe in self.pipes:
            for rectangle in pipe.rectangles():
                if overlap(bird_hit_box, rectangle):
                    self.dead = True
            if BIRD_X > pipe.x + PIPE_WIDTH and pipe.passed == False:
                self.score += 1
                pipe.passed = True

        if self.pipes[0].x + PIPE_WIDTH < 0:    # remove pipe once it's off screen
            self.pipes.popleft()

        self.frame_counter += 1


# helper method to determine if two rectangles are overlapped
def overlap(rect1: tuple, rect2: tuple):
    ax, ay, aw, ah = rect1
    bx, by, bw, bh = rect2

    rect1_rx = ax + aw  # x val of right edge - rect1
    rect2_rx = bx + bw  # x val of right edge - rect2

    rect1_by = ay + ah  # y val of the bottom edge - rect1
    rect2_by = by + bh  # y val of the bottom edge - rect2

    return (rect1_rx > bx and rect2_rx > ax) and (rect1_by > by and rect2_by > ay)


        