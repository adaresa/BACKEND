import pygame
import math
import random

# SETUP DISPLAY
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# FONTS
LETTER_FONT = pygame.font.SysFont("comicsans", 35)
WORD_FONT = pygame.font.SysFont("comicsans", 60)
TITLE_FONT = pygame.font.SysFont("comicsans", 70)

# LOAD IMAGES
images = []
for i in range(7):
    image = pygame.image.load(
        r"C:\Users\kaspe\Documents\GitHub\BACKEND\Python\Hangman\images\hangman" + str(i) + ".png")
    images.append(image)

# LETTER BUTTONS
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 12 - 2 * RADIUS) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + RADIUS + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])


# GAME VARIABLES
play_more = True
hangman_status = 0
words = []
open_file = open(
    r"C:\Users\kaspe\Documents\GitHub\BACKEND\Python\Hangman\words\wordlist.txt", "r")
contents = open_file.readlines()
for i in range(len(contents)):
    words.append(contents[i].strip("\n"))
open_file.close()
word = random.choice(words).upper()
guessed = []

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def draw():
    win.fill(WHITE)
    # DRAW TITLE
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # DRAW WORD
    display_word = ""
    for letter in word:
        if letter == " " or letter == "-":
            guessed.append(letter)
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (370, 200))

    # DRAW BUTTONS
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() /
                            2, y - text.get_height() / 2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    # WIN/LOSE SCREEN
    FPS = 60
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        win.fill(WHITE)
        text = WORD_FONT.render(message, 1, BLACK)
        text2 = WORD_FONT.render(word, 1, BLACK)
        text3 = WORD_FONT.render("The phrase was:", 1, BLACK)
        win.blit(text, (WIDTH/2 - text.get_width() / 2, 100))
        win.blit(text2, (WIDTH/2 - text2.get_width()/2, 250))
        win.blit(text3, (WIDTH/2 - text3.get_width()/2, 200))
        pygame.display.update()
        pygame.time.delay(1000)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                reset()
                run = False


def reset():
    # RESET GAME WHEN PLAYING AGAIN
    global hangman_status
    global word
    global words
    global guessed
    global letters
    hangman_status = 0
    word = random.choice(words).upper()
    guessed = []
    letters = []
    startx = round((WIDTH - (RADIUS * 2 + GAP) * 12 - 2 * RADIUS) / 2)
    starty = 400
    A = 65
    for i in range(26):
        x = startx + RADIUS + ((RADIUS * 2 + GAP) * (i % 13))
        y = starty + ((i // 13) * (GAP + RADIUS * 2))
        letters.append([x, y, chr(A + i), True])


def main():
    global hangman_status
    # SETUP GAMELOOP
    FPS = 60
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            draw()
            pygame.time.delay(1500)
            display_message("You WON, click to play again...")

        if hangman_status == 6:
            draw()
            pygame.time.delay(1500)
            display_message("You Lost, click to play again...")


main()
pygame.quit()
