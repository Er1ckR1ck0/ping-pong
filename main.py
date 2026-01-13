import pygame
from settings import *
from interface import Interface
from assets.walls import P1, P2

pygame.mixer.init()

window = pygame.display.set_mode(PARAMS_WINDOW)
clock = pygame.time.Clock()

while True:
    window.fill(CYAN)
    GameLogic.exit_check()

    if not GameLogic.is_finish:
        Interface.update(window)
        P1.update(window=window, keybinds=["w", "s"])
        P2.update(window=window, keybinds=["up", "down"])
        # GameLogic.check_goal_p1()
        # GameLogic.check_goal_p2()

    pygame.display.update()
    clock.tick(FPS)
