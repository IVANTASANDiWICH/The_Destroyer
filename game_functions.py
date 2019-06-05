import sys

import pygame as pg

def check_events(character):
    """Responds to keypresses and mouse events."""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, character)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, character)

def check_keydown_events(event, character):
    """Respond to keypresses."""
    if event.key == pg.K_ESCAPE:
        sys.exit()
    if event.key == pg.K_UP:
        character.moving_up = True
    elif event.key == pg.K_DOWN:
        character.moving_down = True
    elif event.key == pg.K_RIGHT:
        character.moving_right = True
    elif event.key == pg.K_LEFT:
        character.moving_left = True

def check_keyup_events(event, character):
    if event.key == pg.K_UP:
        character.moving_up = False
    elif event.key == pg.K_DOWN:
        character.moving_down = False
    elif event.key == pg.K_RIGHT:
        character.moving_right = False
    elif event.key == pg.K_LEFT:
        character.moving_left = False

def update_screen(td_settings, screen, character):
    """Update images on screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(td_settings.bg_color)
    character.blitme()

    # Make the most recently drawn screen visible.
    pg.display.flip()