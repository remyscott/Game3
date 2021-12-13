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

os.system('code/loop.py')