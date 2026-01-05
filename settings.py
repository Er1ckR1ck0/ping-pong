import os
from pygame import event, QUIT

# MUSIC FOLDER
MAIN_MUSIC = "1.ogg"
LOSE_MUSIC = "2.ogg"
MUSIC_PATH = "./music/"


MAIN_MUSIC_PATH = os.path.join(MUSIC_PATH, MAIN_MUSIC)
LOSE_MUSIC_PATH = os.path.join(MUSIC_PATH, LOSE_MUSIC)

# WINDOWS
WINDOW_PARAMS = (500, 500)
WINDOW_WIDTH, WINDOW_HEIGHT = WINDOW_PARAMS

# COLOR
BLACK = (0,0,0)
WHITE = (255,255,255)
CYAN = (0,200,200)

# GAME
FPS = 60


def EXIT_EXIST():
    for e in event.get():
        if e.type == QUIT:
            exit()