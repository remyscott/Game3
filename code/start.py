import math, random, os
from pathlib import Path
#from functions import *
import pickle

game_file = Path('..')
settings_path = Path('../data/user/settings.bin')

if settings_path.exists():

    #settings = load_settings()
    class settings():
        FULLSCREEN = False
        SCREEN_WIDTH = 720
        SCREEN_HEIGHT = 1080
else:
    class settings():
        FULLSCREEN = False
        SCREEN_WIDTH = 720
        SCREEN_HEIGHT = 1080

    new_settings_file = open(settings_path, 'wb')
    pickle.dump(settings, new_settings_file)
    new_settings_file.close()


