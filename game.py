# game.py
#
# Cameron's Super-Fun Game
# Just a simple (and hopefully) fun game
#
VERSION = "0.1"

try:
    import sys
    import pygame
    from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
except ImportError as err:
    print(f"couldn't load module. {err}")
    sys.exit(2)

pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True
while running:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            print('Keydown')
            if event.key == K_ESCAPE:
                print('Quit')
                running = False
        elif event.type == QUIT:
            running = False

    screen.fill((225, 225, 225))

    pygame.draw.circle(screen, (52, 235, 192), (250, 250), 75)

    pygame.display.flip()

pygame.quit()
