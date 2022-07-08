import pygame
import random

WIDTH = 600 

SURFACE = pygame.display.set_mode((WIDTH, WIDTH))

WHITE = (255,255,255)
NAVY = (0, 0, 128)
TEAL = (0, 128, 128)

class Bars:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = WHITE
        self.bar_height = []

    def bar(self,surface):
        self.bar_height = []
        self.color = NAVY 
        pygame.draw.rect(surface, self.color,  (0, 3, self.width, self.height))

def main(surface, width):
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

main(SURFACE, WIDTH)