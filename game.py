import random

import pygame
from pygame.locals import *

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 5
        self. max_velocity = 5
    
    def up(self):
        self.velocity = -20
    
    def coords(self):
        if self.velocity < self.max_velocity:
            self.velocity += 3
        if self.velocity = self.max_velocity:
            self.velocity = self.max_velocity
        self.y += self.velocity
        return self.x, self.y

# Set constant colours
PIPE = (0, 255, 0)
BACKGROUND = (0, 255, 255)
BIRD = (255, 255, 0)
TEXT = (0, 0, 0)

# Set screen variables
size = (800, 800)
width, height = size

# Initialise score
points = 0

# Initialise objects
bird = Bird(width // 4, height // 2)
pipe_height = random.randint(height // 4, 3 * height // 4) - 30
pipe1 = pygame.Rect(width, pipe_height + 50, 40, height - pipe_height)
pipe2 = pygame.Rect(width, 0, 40, pipe_height - 50)
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(size)

running = True
while running:
    clock.tick(40)
    
    # Handle keypresses
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.up()
            
            if event.type == pygame.QUIT:
                running = False
    
    # Draw everything
    screen.fill(BACKGROUND)
    pygame.draw.circle(screen, BIRD, bird.coords(), 20)
    pygame.draw.rect(screen, PIPE, pipe1)
    pygame.draw.rect(screen, PIPE, pipe2)

    # update pipe position
    pipe1.move_ip(-5. 0)
    pipe2.move_ip()

        
