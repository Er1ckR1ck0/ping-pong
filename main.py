import pygame
from settings import *
from interface import Interface
from assets.walls import P1, P2
from assets.ball import ball
from assets.ball import ball

pygame.mixer.init()


clock = pygame.time.Clock()

while True:
    window.fill(CYAN)
    GameLogic.exit_check()

    if not GameLogic.is_finish:
        
        Interface.update(window)
        P1.update(window=window, keybinds=["w", "s"])
        P2.update(window=window, keybinds=["up", "down"])
        ball.update(window=window)
        ball.movement(P1, P2)
        GameLogic.check_goal_p1(P1, ball)
        GameLogic.check_goal_p2(P2, ball)
        
        

    pygame.display.update()
    clock.tick(FPS)
