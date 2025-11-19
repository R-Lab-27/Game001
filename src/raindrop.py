import pygame, random
import constants

class Raindrop():
    def __init__(self):
        self.x = random.randint(0, constants.WINDOW_WIDTH)
        self.y = -5
        self.speed = random.randint(5, 15)

    def move(self):
        self.y += self.speed

    def is_off_screen(self):
        return self.y > constants.WINDOW_HEIGHT

    def draw(self, screen):
        pygame.draw.line(screen, (0,0,0), (self.x, self.y), (self.x, self.y + 5), 1)