import pygame
import time
import random

# SETUP DISPLAY
pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 1250, 750
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKE GAME BY ADARESA")
pygame.display.update()

# COLORS
ORANGE = (255,123,7)
BLACK = (0,0,0)
RED = (213,50,80)
GREEN = (34,139,34)
BLUE = (10,53,73)

# GAME VARIABLES
snake_block = 50
snake_list = []
snake_speed = 7

# CREATE SNAKE
def snake(snake_block, snake_list):
    count = 1
    for i in snake_list:
        # DRAW FACE IF HEAD PIECE
        if count == len(snake_list):
            pygame.draw.rect(win, (50,205,50), [i[0], i[1], snake_block, snake_block])
            radius = 5
            circleMiddle = (i[0] + 15, i[1] + 16)
            circleMiddle2 = (i[0] + 37, i[1] + 16)
            pygame.draw.circle(win, BLACK, circleMiddle, radius)
            pygame.draw.circle(win, BLACK, circleMiddle2, radius)
            pygame.draw.rect(win, RED, [i[0] + 13, i[1] + 30, 25, 7])
        else:
            pygame.draw.rect(win, GREEN, [i[0], i[1], snake_block, snake_block])
        count += 1

# MAKE THE GRID
def drawGrid():
    gap = snake_block
    times = int(WIDTH / snake_block)
    x = 0
    y = 0
    for l in range(times):
        x += gap
        y += gap
        pygame.draw.line(win, BLUE, (x, 0), (x, 1250))
        pygame.draw.line(win, BLUE, (0, y), (1250, y))

# MAIN
def snakegame():
    run = True
    end = False
    # SNAKE COORDINATES
    x1 = 650
    y1 = 350
    # WHEN SNAKE MOVES
    x1_change = 0
    y1_change = 0
    # SNAKE LENGTH
    snake_list = []
    length_of_snake = 1
    # FOOD COORDINATES
    foodx = round(random.randrange(0, WIDTH - snake_block) / 50.0) * 50.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 50.0) * 50.0

    while run:
        clock.tick(snake_speed)
        # GAME END SCREEN
        while end == True:
            win.fill(BLACK)
            font_style = pygame.font.SysFont("comicsans", 45)
            msg = font_style.render("You lost! Press P to play again", True, RED)
            win.blit(msg, [WIDTH / 6, HEIGHT / 3])
            # DISPLAY THE SCORE
            score = length_of_snake - 1
            score_font = pygame.font.SysFont("comicsans", 65)
            value = score_font.render("Your Score: " + str(score), True, ORANGE)
            win.blit(value, [WIDTH / 3, HEIGHT / 5])
            pygame.display.update()
            # BUTTON PRESSES (p to restart game)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False # game still open
                    end = False # game over
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        snakegame()
        # BUTTON PRESSES (movement with keys)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != snake_block:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -snake_block:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != snake_block:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN and y1_change != -snake_block:
                    x1_change = 0
                    y1_change = snake_block
        # UPDATE COORDINATES
        x1 += x1_change
        y1 += y1_change
        win.fill(BLACK)
        # CREATE A FOOD
        pygame.draw.rect(win, RED, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # SNAKE KEEPS SIZE IF MOVING FORWARD
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        # GAME END 1/2 (out of bounds)
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            end = True
        # GAME END 2/2 (eats itself)
        for i in snake_list[:-1]:
            if i == snake_head:
                end = True
        # MOVE SNAKE
        snake(snake_block, snake_list)
        # EATING FOOD INCREASES SIZE AND CREATES NEW FOOD
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 50.0) * 50.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 50.0) * 50.0
            length_of_snake += 1
        drawGrid()
        pygame.display.update()
    pygame.quit()
    quit()
snakegame()
