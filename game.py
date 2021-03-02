import random

import pygame
from pygame.locals import *

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 5
        self. max_velocity = 5