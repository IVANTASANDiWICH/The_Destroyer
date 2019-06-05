import pygame as pg
from pygame.sprite import (Group)
from settings import Settings
from character import Character
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pg.init()
    td_settings = Settings()
    screen = pg.display.set_mode(
        (td_settings.screen_width, td_settings.screen_height))
    pg.display.set_caption("The Destroyer")

    # Make a character.
    character = Character(td_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game.
    while True:
        gf.check_events(td_settings, screen, character, bullets)
        character.update()
        gf.update_bullets(bullets)
        gf.update_screen(td_settings, screen, character, bullets)


if __name__ == '__main__':
    run_game()
