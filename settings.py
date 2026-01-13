import os
from pygame import event, QUIT, K_w, K_s, K_UP, K_DOWN
from interface import Interface

# music
MAIN_MUSIC = "1.ogg"
LOSE_MUSIC = "2.ogg"
MUSIC_PATH = "./music"

# path_main_music = os.path.join(path_music, main_music)
# path_lose_music = os.path.join(path_music, lose_music)

# window_set
PARAMS_WINDOW = (500, 500)
WIDTH, HEIGHT = PARAMS_WINDOW

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

class GameLogic:
    is_finish = False

    def exit_check():
        for e in event.get():
            if e.type == QUIT:
                exit()

    @staticmethod
    def check_goal_p2(player, ball):
        if player.rect.left <= ball.rect.right:
            Interface.inscrease_p2()

    @staticmethod
    def check_goal_p1(player, ball):
        if player.rect.right >= ball.rect.left:
            Interface.inscrease_p1()
