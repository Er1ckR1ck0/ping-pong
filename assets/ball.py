from pygame import Surface
from pygame.draw import circle as draw_circle
from pygame.sprite import spritecollide, Group

from .game_sprite import GameSprite

from settings import BORDER_WIDTH, window_rect

class Ball(GameSprite):
    def __init__(self):
        super().__init__(window_rect.centerx, window_rect.centery, 30, 30)
        self.speed_x = self.speed
        self.speed_y = self.speed
        
    def reset(self):
        self.rect.center = window_rect.center
        
    def movement(self, player_1, player_2):
        if self.rect.bottom > window_rect.bottom or self.rect.top < window_rect.top:
            self.speed_y *= -1
        
        if spritecollide(self, Group(player_1, player_2), 0):
            self.speed_x *= -1
            
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
    def update(self, window: Surface):
        draw_circle(window, self.color, self.rect.center, 15)
        draw_circle(window, self.border_color, self.rect.center, 15, BORDER_WIDTH)
        
ball = Ball()