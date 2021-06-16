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

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((225, 225, 225))
        self.rect = self.surf.get_rect()

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

    surf = pygame.Surface((50, 50))

    surf.fill((0, 0, 0))
    rect = surf.get_rect()

    surf_center = (
       (SCREEN_WIDTH-surf.get_width())/2,
       (SCREEN_HEIGHT-surf.get_height())/2
    )

    screen.blit(surf, surf_center)

    pygame.display.flip()

pygame.quit()
