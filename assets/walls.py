from typing import List

from pygame import key, Surface

from assets.game_sprite import GameSprite
from settings import keybinds_dict, HEIGHT, WIDTH

class Walls(GameSprite):
    def __init__(self, x, y):
        super().__init__(x, y, 10, 30)
        
    def update(self, window: Surface, keybinds: List[str]):
        super().update(window=window)
        
        up, down = keybinds
        
        key_pressed = key.get_pressed()
        
        if key_pressed[keybinds_dict.get(up)] and self.rect.top > 0:
            self.rect.y -= self.speed
        if key_pressed[keybinds_dict.get(down)] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
            
P1 = Walls(20, HEIGHT//2)
P2 = Walls(WIDTH-20, HEIGHT//2)