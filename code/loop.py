import pygame
from pygame.locals import *
from functions import *

class settings():
        FULLSCREEN = False
        SCREEN_WIDTH = 1080
        SCREEN_HEIGHT = 720
        SMALL_SCREEN_WIDTH = 1080
        SMALL_SCREEN_HEIGHT = 720

#pygame setup
display = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
small_display = pygame.Surface((settings.SMALL_SCREEN_WIDTH, settings.SMALL_SCREEN_HEIGHT))

# functions
def small_display_to_big_display():
    display.blit(pygame.transform.scale(small_display, (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)))

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

        small_display_to_big_display()
        pygame.display.update()

def render_menu():
    pass
#///////////////Screens (Above)///////////////
#///////////////Creatures (Below)///////////////
class Skeleton(pygame.sprite.Sprite):
    def __init__(self, position):
        self.position = position
        self.image = pygame.Surface((50,50))

    def update():
        

game_loop()
