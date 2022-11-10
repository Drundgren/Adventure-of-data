from slide import slider
import random
from settings import *

pygame.display.set_caption("Adventure of Data")
pygame.font.init()

WIN = pygame.display.set_mode((winlen, winheight))  # Setting up the game window
mixer.music.play(-1) # Playing the music


def room_0(animation_count, score_):  # displaying the environment for the first room.
    WIN.fill(black)
    background_room1 = BackgroundRoom1(0-display_scroll[0], -500-display_scroll[1], 1000, 1000, animation_count)
    if score_ == "00":  # Displays score depending on which enemies you´ve defeated
        background_room1.main(WIN, background_images1)
    if score_ == "10":  # Displays score depending on which enemies you´ve defeated
        background_room1.main(WIN, background_images2)
    if score_ == "20":  # Displays score depending on which enemies you´ve defeated
        background_room1.main(WIN, background_images3)

    text = font.render(score_, True, white, black)
    text_rect = text.get_rect()

    WIN.blit(carpet, (450-display_scroll[0], -180-display_scroll[1]))  # Carpet outside middle door
    WIN.blit(carpet, (110-display_scroll[0], -180-display_scroll[1]))  # Carpet outside left door
    WIN.blit(carpet, (790-display_scroll[0], -180-display_scroll[1]))  # Carpet outside right door
    character.main(WIN)
    WIN.blit(text, text_rect)

    if score_ == "WINNER":
        WIN.blit(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Winner.jpg')), (1000, 600)), (0, 0))
    pygame.display.update()


def character_movement(key_pressed):  # moving the character
    if key_pressed[pygame.K_w] and display_scroll[1] >= -515:  # Up movement with border
        display_scroll[1] -= vel
        character.moving_up = True  # Animation for moving
    if key_pressed[pygame.K_s] and display_scroll[1] <= 148:  # Down movement with border
        display_scroll[1] += vel
        character.moving_down = True  # Animation for moving
    if key_pressed[pygame.K_a] and display_scroll[0] >= -350:  # Left movement with border
        display_scroll[0] -= vel
        character.moving_left = True  # Animation for moving
    if key_pressed[pygame.K_d] and display_scroll[0] <= 350:  # Right movement with border
        display_scroll[0] += vel
        character.moving_right = True  # Animation for moving


def hub(score_):
    animation_count = 0
    run = True
    while run:
        clock.tick(fps)  # Limit the loop to update 60 times per second
        rect_room_middle = pygame.Rect(400-display_scroll[0],
                                       -220-display_scroll[1], 100, 50)  # Hit-box to enter middle room
        rect_room_left = pygame.Rect(60-display_scroll[0],
                                     -220-display_scroll[1], 100, 50)  # Hit-box to ender left room
        rect_room_right = pygame.Rect(740-display_scroll[0],
                                      -220-display_scroll[1], 100, 50)  # Hit-box to enter right room

        collide_middle = char.colliderect(rect_room_middle)  # Detecting collision between character and the hit-box
        collide_left = char.colliderect(rect_room_left)  # Detecting collision between character and the hit-box
        collide_right = char.colliderect(rect_room_right)  # Detecting collision between character and the hit-box

        if animation_count + 1 >= 24:  # Looping the background animation
            animation_count = 0
        animation_count += 1

        key_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # So the program quits when you hit the red x button
                run = False

        room_0(animation_count, score_)
        if collide_left and key_pressed[pygame.K_SPACE] and score_ == "00":
            run = False
            game(0, score_)
        if collide_right and key_pressed[pygame.K_SPACE] and score_ == "10":
            run = False
            game(1, score_)
        if collide_middle and key_pressed[pygame.K_SPACE] and score_ == "20":
            run = False
            game(2, score_)
        character_movement(key_pressed)


# Code for combat starts here
pygame.init()

# background-images
background = [
    pygame.image.load(f'assets/boss_1.png').convert_alpha(),
    pygame.image.load(f'assets/boss_2.png').convert_alpha(),
    pygame.image.load(f'assets/boss_3.png').convert_alpha()]


# used to choose run or attack
def mouse_collision(action_1, action_2):
    pos = pygame.mouse.get_pos()
    attack = pygame.Rect(720, 477, 166, 50)
    run = pygame.Rect(737, 540, 122, 40)
    if attack.collidepoint(pos[0], pos[1]):
        if pygame.mouse.get_pressed()[0] == 1 and action_1 is False:
            return "action_1"
    elif run.collidepoint(pos[0], pos[1]):
        if pygame.mouse.get_pressed()[0] == 1 and action_2 is False:
            return "action_2"


def text_image(text, text_color, x, y):
    img = font.render(text, True, text_color, black)
    WIN.blit(img, (x, y))


# Takes the background depending on the level.
def draw_bg(level):
    WIN.blit(pygame.transform.scale(background[level], (1000, 600)), (0, 0))


def draw_stats(level):
    text_image(f'{Hero.name}', green, 150, 50)
    text_image(f'HP: {Hero.hp}', green, 150, 100)
    text_image(f'{enemies[level].name}', red, 800, 15)
    text_image(f'HP: {enemies[level].hp}', red, 850, 55)

#combat function, 
def Combat(level, current_fighter, action_1, action_2): 
    if Hero.hp > 0 and enemies[level].hp > 0: #checks if Hero is alive and 
        if current_fighter:
            action = mouse_collision(action_1, action_2)
            if action:
                if action == "action_1":
                    slider(level, WIN, enemies)
                    return "switch"
                if action == "action_2":
                    Hero.hp = Hero.max_hp #reset hp
                    enemies[level].hp = enemies[level].max_hp # Reset hp
                    return "run"
        else:
            Hero.hp -= random.randint(5, 10)
            return "switch"

    if Hero.hp <= 0:
        Hero.hp = Hero.max_hp
        enemies[level].hp = enemies[level].max_hp
        return "Dead"

    if enemies[level].hp <= 0:
        Hero.hp = Hero.max_hp
        enemies[level].hp = enemies[level].max_hp
        return "Win"


def game(level, score):
    run = True
    enemies_health_bar = hp_bar(550, 100, enemies[level].hp, enemies[level].max_hp)
    current_fighter = True 
    action_1 = False
    action_2 = False

    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # draw background
        draw_bg(level)
        # Draws stats
        draw_stats(level)
        # draws health-bar
        enemies_health_bar.draw_hp(enemies[level].hp, WIN)
        Hero_health_bar.draw_hp(Hero.hp, WIN)
        combat = Combat(level, current_fighter, action_1, action_2)
        #Below we see different scenarios for the combat function.
        if combat == "switch" and current_fighter: #Switches to false if current_fighter == True
            current_fighter = False
        elif combat == "switch": #Switches to True if current_fighter == False
            current_fighter = True
        #All if statement below leaves game by setting run as false.
        if combat == "run": 
            run = False
            hub(score)
        if combat == "Win" and level == 0: #Level 0, goes to Hub with score 10
            run = False
            hub("10")

        if combat == "Win" and level == 1: #Level 1, goes to hub with score 20, changes background and level.
            run = False
            hub("20")

        if combat == "Win" and level == 2: #Level 2 win goes to hub "winner which displays a winner background.
            run = False
            hub("WINNER")

        if combat == "Dead": # goes out of combat.
            run = False
            #Reset to middle of the screen
            display_scroll[0] = 0
            display_scroll[1] = 0
            hub(score)
        pygame.display.update()


hub("00")
pygame.quit()
