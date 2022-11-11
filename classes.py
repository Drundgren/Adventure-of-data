import pygame

red = (255, 0, 0)
green = (0, 255, 0)


class characters(): #class to make the hero and the enemies
    def __init__(self, name, max_hp):
        self.name = name #name of the character
        self.max_hp = max_hp #static max hp variable
        self.hp = max_hp #self.hp will be controlling the hp in each round, will changed.


class hp_bar(): #class for hp bar of heroes and enemies.
    def __init__(self, x, y, hp, max_hp):
        self.x = x # x-cordinate of the hp bar
        self.y = y # y-cordninate of the hp bar
        self.hp = hp 
        self.max_hp = max_hp 

    def draw_hp (self, hp, WIN): #draws the hp bar
        self.hp = hp
        Hp_ratio = self.hp/self.max_hp # used to represent a percentage of the max hp.
        pygame.draw.rect(WIN, red, (self.x, self.y, self.max_hp, 20)) #draws hp bars depending on the size of the characters max health
        pygame.draw.rect(WIN, green, (self.x, self.y, self.max_hp*Hp_ratio, 20)) #draws a green health bar ontop of the character
