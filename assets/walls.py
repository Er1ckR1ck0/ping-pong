from typing import List

from pygame import key, Surface

from assets.game_sprite import GameSprite
from settings import keybinds_dict, window_rect, P1_POS ,P2_POS

class Walls(GameSprite):
    def __init__(self, x, y):
        super().__init__(x, y, 10, 100, 14)
        
    def reset(self, POSITION):
        self.rect.center = POSITION
        
    def update(self, window: Surface, keybinds: List[str]):
        super().update(window=window)
        
        up, down = keybinds
        
        key_pressed = key.get_pressed()
        
        if key_pressed[keybinds_dict.get(up)] and self.rect.top > 0:
            self.rect.y -= self.speed
        if key_pressed[keybinds_dict.get(down)] and self.rect.bottom < window_rect.bottom:
            self.rect.y += self.speed
            
P1 = Walls(P1_POS[0], P1_POS[1])
P2 = Walls(P2_POS[0], P2_POS[1])