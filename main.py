import pygame
from settings import *
from interface import Interface
from assets.walls import P1, P2
from assets.ball import ball

pygame.mixer.init()

clock = pygame.time.Clock()

while True:
    window.fill(CYAN)
    GameLogic.exit_check()

    if not GameLogic.is_finish:
        Interface.update(WINDOW)
        P1.update(window=WINDOW, keybinds=["w", "s"])
        P2.update(window=WINDOW, keybinds=["up", "down"])
        ball.update(window=WINDOW)
        # GameLogic.check_goal_p1()
        # GameLogic.check_goal_p2()

    pygame.display.update()
    clock.tick(FPS)
