import pygame
from settings import *

pygame.mixer.init()


window = pygame.display.set_mode(WINDOW_PARAMS)
clock = pygame.time.Clock()

while True:
    window.fill(CYAN)
    EXIT_EXIST()
    pygame.display.update()
    clock.tick(FPS)