from pygame import sprite, draw

from game_sprite import GameSprite
from settings import WINDOW_RECT, BORDER_WIDTH

class Ball(GameSprite):
    def __init__(self):
        super().__init__(
            x=WINDOW_RECT.centerx,
            y=WINDOW_RECT.centery,
            w=50,
            h=50,
            speed=10
        )
        self.speed_x, self.speed_y = self.speed, self.speed

    def wall_collide(self, player_1, player_2):
        if not (WINDOW_RECT.top <= self.rect.centery <= WINDOW_RECT.bottom):
            self.speed_y *= -1
        
        if sprite.collider_rect(self, player_1) or sprite.collider_rect(self, player_2):
            self.speed_x *= -1

    def movement(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def update(self, window):
        pygame.draw.circle(window, self.color, (self.rect.x, self.rect.y), self.w // 2)
        pygame.draw.circle(window, self.color, (self.rect.x, self.rect.y), self.w // 2, width=BORDER_WIDTH)
        
        self.movement()

ball = Ball()