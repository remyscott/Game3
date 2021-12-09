import math, random, os
from pathlib import Path
import pygame
from pygame.locals import *
#from functions import *
import pickle



settings_path = Path('data/user/settings.bin')

if settings_path.exists():

    #settings = load_settings()
    class settings():
        FULLSCREEN = False
        SCREEN_WIDTH = 1080
        SCREEN_HEIGHT = 720
else:
    class settings():
        FULLSCREEN = False
        SCREEN_WIDTH = 1080
        SCREEN_HEIGHT = 720
    
    settings_file = open(settings_path, 'wb')
    pickle.dump(settings, settings_file)
    settings_file.close()

#pygame setup
display = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

#///////////////////Sceens///////////////////
def main_menu():
    running = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

def load_game_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

def new_game_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

#def render_menu()
#///////////////Screens (Above)///////////////

main_menu()