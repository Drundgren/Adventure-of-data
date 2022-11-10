import pygame

red = (255, 0, 0)
green = (0, 255, 0)


class characters():
    def __init__(self, name, max_hp):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp


class hp_bar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw_hp (self, hp, WIN):
        self.hp = hp
        Hp_ratio = self.hp/self.max_hp
        pygame.draw.rect(WIN, red, (self.x, self.y, self.max_hp, 20))
        pygame.draw.rect(WIN, green, (self.x, self.y, self.max_hp*Hp_ratio, 20))