import sys
import pygame
from settings import *
from buttonClass import *
from app_class import *

class Menu:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.Font('../assets/fonts/maldini/MaldiniNormal2.ttf', 70) # cell numbers
        self.font2 = pygame.font.Font('../assets/fonts/maldini/MaldiniNormal2.ttf', 40) # cell numbers
        
        self.running = True
        self.state = "main_menu"
        self.app = None
        
        self.menuButtons = []
        self.loadButtons()
    
    def run(self):
        while self.running:
            if self.state == "main_menu":
                self.menu_events()
                self.menu_update()
                self.menu_draw()
            elif self.state == "playing":
                self.app.playing_events()
                self.app.playing_update()
                self.app.playing_draw()
            elif self.state == "achievements":
                pass
            elif self.state == "options":
                pass
        pygame.quit()
        sys.exit()
        
    ###### MAIN MENU FUNCTIONS ######

    def menu_events(self):
        for event in pygame.event.get():
                                
            if event.type == pygame.QUIT:
                self.running = False

            #if event.type == pygame.MOUSEMOTION:

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.menuButtons:
                    button.activate(self.mousePos)

    def menu_update(self):
        self.mousePos = pygame.mouse.get_pos()
        for button in self.menuButtons:
            button.update(self.mousePos)
        
    def menu_draw(self):
        self.window.fill(BG)
        self.titleText()
        for button in self.menuButtons:
            button.draw(self.window)
        pygame.display.update()
    
    ###### HELPER FUNCTIONS ######
    
    def titleText(self):
        # title text
        text = self.font.render("Simple Sudoku", True, SNOW) # (text, antialias, color)
        text_rect = text.get_rect(center=(WIDTH/2, 100))
        self.window.blit(text, text_rect)
    
    def loadingScreen(self):
        self.window.fill(BG)
        text = self.font.render("LOADING ...", True, SNOW) # (text, antialias, color)
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        self.window.blit(text, text_rect)
        pygame.display.update()
        
    def launchGame(self):
        if not self.app:
            self.loadingScreen()
            self.app = App(self.launchMenu, self.quitGame, self.loadingScreen)
        self.state = "playing"
        
    def launchMenu(self):
        self.state = "main_menu"
        
    def quitGame(self):
        self.running = False
        
    def loadButtons(self):
        text = self.font2.render("PLAY GAME", True, SNOW) # (text, antialias, color)
        self.menuButtons.append(Button(WIDTH/2 - 100, 200, 240, 60, text, function = self.launchGame))
        
        text = self.font2.render("ACHIEVEMENTS", True, SNOW) # (text, antialias, color)
        self.menuButtons.append(Button(WIDTH/2 - 100, 290, 240, 60, text))
        
        text = self.font2.render("OPTIONS", True, SNOW) # (text, antialias, color)
        self.menuButtons.append(Button(WIDTH/2 - 100, 380, 240, 60, text))
        
        text = self.font2.render("EXIT GAME", True, SNOW) # (text, antialias, color)
        self.menuButtons.append(Button(WIDTH/2 - 100, 470, 240, 60, text, function = self.quitGame))