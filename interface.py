from pygame import font, Surface
from settings import window_rect

font.init()


class Interface:
    h1 = font.Font(None, 64)
    h2 = font.Font(None, 32)
    h3 = font.Font(None, 24)
    h4 = font.Font(None, 12)

    counter_p1 = 0
    counter_p2 = 0

    @classmethod
    def inscrease_p1(cls):
        cls.counter_p1 += 1

    @classmethod
    def inscrease_p2(cls):
        cls.counter_p2 += 1

    @classmethod
    def update(cls, window: Surface):
        cls.text_p1 = cls.h1.render(str(cls.counter_p1), True, (255, 255, 255))
        cls.text_p2 = cls.h1.render(str(cls.counter_p2), True, (255, 255, 255))

        window.blit(cls.text_p1, (20, 20))
        window.blit(cls.text_p2, (window_rect.width - cls.text_p2.get_rect().width - 30, 20))
