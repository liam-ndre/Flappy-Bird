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
    