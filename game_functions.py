import sys

import pygame as pg
from bullet import Bullet

def check_keydown_events(event, td_settings, screen, character, bullets):
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
    elif event.key == pg.K_SPACE:
        fire_bullet(td_settings, screen, character, bullets)

def fire_bullet(td_settings, screen, character, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < td_settings.bullets_allowed:
        new_bullet = Bullet(td_settings, screen, character)
        bullets.add(new_bullet)

def check_keyup_events(event, character):
    if event.key == pg.K_UP:
        character.moving_up = False
    elif event.key == pg.K_DOWN:
        character.moving_down = False
    elif event.key == pg.K_RIGHT:
        character.moving_right = False
    elif event.key == pg.K_LEFT:
        character.moving_left = False

def check_events(td_settings, screen, character, bullets):
    """Responds to keypresses and mouse events."""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, td_settings, screen, character, bullets)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, character)

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.left > 1280:
            bullets.remove(bullet)

def update_screen(td_settings, screen, character, bullets):
    """Update images on screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(td_settings.bg_color)

    # Redraw all bullets behind character and libtards.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    character.blitme()

    # Make the most recently drawn screen visible.
    pg.display.flip()
