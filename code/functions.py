import pygame

def small_display_to_big_display():
    display.blit(pygame.transform.scale(small_display, (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)))
    pygame.display.update()