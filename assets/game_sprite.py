from pygame import Rect, Surface
from pygame.draw import rect as dw_rect
from pygame.sprite import Sprite

from settings import WHITE, BLACK, BORDER_WIDTH

class GameSprite(Sprite):
    def __init__(
        self,
        x: int = 20,
        y: int = 20,
        w: int = 100,
        h: int = 100,
        speed: int = 10,
        color: tuple = WHITE,
        border_color: tuple = BLACK,
    ):
        self.rect = Rect(x, y, w, h)
        self.speed = speed
        self.color = color
        self.border_color = border_color

    def update(self, window: Surface) -> None:
        dw_rect(window, self.color, self.rect)
        dw_rect(window, self.border_color, self.rect, width=BORDER_WIDTH)
        

