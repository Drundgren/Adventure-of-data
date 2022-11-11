import pygame

FPS = 60

playerX = 64
playerY = 136


class Rectangle: #Used for rect2
    def __init__(self, x, y, pos_y, pos_x):
        self.x = x
        self.y = y
        self.pos_y = pos_y
        self.pos_x = pos_x


def draw_window(rect2, keys_pressed, level, WIN, enemies): #draws the different rectangles and their hitboxes, see comments on line 21 and 23.
    pygame.draw.rect(WIN, (128, 128, 128), (600, 400, 300, 100))

    #draws the different rectangles and their hitboxes, see comments on the red rectangle. line 21 and 23.
    
    # red
    pygame.draw.rect(WIN, (200, 0, 0), (610, 410, 56, 80)) #Draws rectangle
    pygame.draw.rect(WIN, (255, 0, 0), (834, 410, 56, 80))
    rect_red1 = pygame.Rect(610, 410, 56, 80) #Hitbox for rectangle
    rect_red2 = pygame.Rect(834, 410, 56, 80)
    
    # yellow
    pygame.draw.rect(WIN, (255, 255, 0), (666, 410, 56, 80))
    pygame.draw.rect(WIN, (255, 255, 0), (778, 410, 56, 80))
    rect_yellow1 = pygame.Rect(666, 410, 56, 80)
    rect_yellow2 = pygame.Rect(778, 410, 56, 80)
    
    # green
    pygame.draw.rect(WIN, (0, 255, 0), (722, 410, 56, 80))
    rect_green = pygame.Rect(722, 410, 56, 80)
    
    # black
    pygame.draw.rect(WIN, (0, 0, 0), (rect2.x, rect2.y, 4, 80))
    
    
    #checks if space is pressed and rect2 is within the hitboxes, see more information about rect2 on line 63.
    
    if (rect2.colliderect(rect_red1) or rect2.colliderect(rect_red2)) and keys_pressed[pygame.K_SPACE]: # space pressed  + red
        enemies[level].hp -= 5 #damage to enemy health
        return True # stops the while loop for the slider
    
    if (rect2.colliderect(rect_yellow1) or rect2.colliderect(rect_yellow2)) and keys_pressed[pygame.K_SPACE]: # space pressed  + yellow
        enemies[level].hp -= 10
        return True
    
    if rect2.colliderect(rect_green) and keys_pressed[pygame.K_SPACE]: # space pressed + green
        enemies[level].hp -= 25
        return True
    
    pygame.display.update()


def slider(level, WIN, enemies):
    rect2 = pygame.Rect(748, 410, 4, 80) # draws a thin rectangle, which will move in the while loop on line 67.
    vel = 10
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        rect2.x += vel # updates rect2 position each loop.
        if rect2.x >= 886: #changes direction if rect2 hits the end of the slide bar.
            vel = -10
        elif rect2.x <= 610: #also changes direction
            vel = 10

        keys_pressed = pygame.key.get_pressed()
        if draw_window(rect2, keys_pressed, level, WIN, enemies):
            run = False
