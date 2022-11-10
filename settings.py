import os
import pygame
from pygame import mixer
from classes import characters, hp_bar

mixer.init()
pygame.font.init()
pygame.mixer.music.load(os.path.join('Assets', 'Backgorund_music.mp3'))
mixer.music.set_volume(0.2)

character_images_left_right = [pygame.image.load(os.path.join('Assets', 'Side.png')),
                               pygame.image.load(os.path.join('Assets', 'SideWalkL2.png')),
                               pygame.image.load(os.path.join('Assets', 'Side.png')),
                               pygame.image.load(os.path.join('Assets', 'WalkSideR2.png'))]  # Character images in a list

character_images_up = [pygame.image.load(os.path.join('Assets', 'Back2.png')),
                       pygame.image.load(os.path.join('Assets', 'BackWalkL2.png')),
                       pygame.image.load(os.path.join('Assets', 'Back2.png')),
                       pygame.image.load(os.path.join('Assets', 'BackWalkR2.png'))]

character_images_down = [pygame.image.load(os.path.join('Assets', 'Front2.png')),
                         pygame.image.load(os.path.join('Assets', 'FrontWalkL2.png')),
                         pygame.image.load(os.path.join('Assets', 'Front2.png')),
                         pygame.image.load(os.path.join('Assets', 'FrontWalkR2.png'))]

background_images1 = [pygame.image.load(os.path.join('Assets', 'Background1.png')),
                      pygame.image.load(os.path.join('Assets', 'Background2.png.png')),
                      pygame.image.load(
                          os.path.join('Assets', 'Background3.png.png'))]  # All background images in a list

background_images2 = [pygame.image.load(os.path.join('Assets', 'Background2.png')),
                      pygame.image.load(os.path.join('Assets', 'Background2.1.png')),
                      pygame.image.load(os.path.join('Assets', 'Background2.2.png'))]

background_images3 = [pygame.image.load(os.path.join('Assets', 'Background3.png')),
                      pygame.image.load(os.path.join('Assets', 'Background3.1.png')),
                      pygame.image.load(os.path.join('Assets', 'Background3.2.png'))]

display_scroll = [0, 0]  # List with x and y value to move the background in relation to the character


class Character:  # Class for the character
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def main(self, window):
        if self.animation_count + 1 >= 24:
            self.animation_count = 0
        self.animation_count += 1

        if self.moving_up:
            window.blit(pygame.transform.scale(character_images_up[self.animation_count // 6],
                                               (self.height, self.width)), (self.x, self.y))
        elif self.moving_down:
            window.blit(pygame.transform.scale(character_images_down[self.animation_count // 6],
                                               (self.height, self.width)), (self.x, self.y))
        elif self.moving_right:
            window.blit(pygame.transform.scale(character_images_left_right[self.animation_count // 6],
                                               (self.height, self.width)), (self.x, self.y))
        elif self.moving_left:
            window.blit(pygame.transform.scale(
                pygame.transform.flip(character_images_left_right[self.animation_count // 6], True,
                                      False), (self.height, self.width)), (self.x, self.y))
        else:
            window.blit(pygame.transform.scale(character_images_down[0], (self.height, self.width)), (self.x, self.y))

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False


class BackgroundRoom1:  # Class for the animated background
    def __init__(self, x, y, width, height, animation_count):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = animation_count

    def main(self, window, background):
        window.blit(pygame.transform.scale(background[self.animation_count // 8], (self.width, self.height)),
                    (self.x, self.y))


character = Character(475, 250, 100, 50)  # Calling the character via the Character class

char = pygame.Rect(450, 310, 10, 10)  # A rectangle for the characters hit-box.

winheight = 600  # Dimensions for the game window
winlen = 1000

clock = pygame.time.Clock()  # Setting up a clock that limits the loop to update 60 times per second

white = (255, 255, 255)
black = (0, 0, 0)

vel = 3  # Speed of character movement

fps = 60  # Frames per second variable

font = pygame.font.SysFont("arial", 34)

carpet = pygame.Surface(
    (100, 50))  # Opaque red square that can be placed outside each door to indicate intractable area
carpet.set_alpha(65)
carpet.fill((255, 0, 0))

Hero = characters('Hero', 100)
Hero_health_bar = hp_bar(100, 500, Hero.hp, Hero.max_hp)
enemies = [characters('Lava Monster', 200), characters('Void Man', 250), characters('Thunder God', 300)]

# colors for health-bar
red = (255, 0, 0)
green = (0, 255, 0)
