import os
from pygame import event, QUIT, K_w, K_s, K_UP, K_DOWN, display


# music
MAIN_MUSIC = "1.ogg"
LOSE_MUSIC = "2.ogg"
MUSIC_PATH = "./music"

# path_main_music = os.path.join(path_music, main_music)
# path_lose_music = os.path.join(path_music, lose_music)

# window_set
PARAMS_WINDOW = (500, 500)
WINDOW_WIDTH, WINDOW_HEIGHT = PARAMS_WINDOW
window = display.set_mode(PARAMS_WINDOW)
window_rect = window.get_rect()

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 200, 200)

# game_states
FPS = 60

# BORDER WIDTH
BORDER_WIDTH = 3

# KEYBINDS
keybinds_dict = {"w": K_w, "s": K_s, "down": K_DOWN, "up": K_UP}

P1_POS = (20, window_rect.height//2)
P2_POS = (window_rect.width-40, window_rect.height//2)


from interface import Interface

class GameLogic:
    is_finish = False
    ready = True
    def exit_check():
        for e in event.get():
            if e.type == QUIT:
                exit()

    @staticmethod
    def check_goal_p1(player, ball):
        if player.rect.left > ball.rect.right:
            ball.reset()
            Interface.inscrease_p2()
            

    @staticmethod
    def check_goal_p2(player, ball):
        if player.rect.right < ball.rect.left:
            ball.reset()
            Interface.inscrease_p1()
            

    