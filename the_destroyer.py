import pygame as pg
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

    # Start the main loop for the game.
    while True:
        gf.check_events(character)
        character.update()
        gf.update_screen(td_settings, screen, character)

run_game()
