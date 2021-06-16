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

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((225, 225, 225))
        self.rect = self.surf.get_rect()
    
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length
        


pygame.init()
        
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()
square = Square(4)
rectangle = Rectangle(2, 4)

running = True
while running:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            print('Keydown')
            if event.key == K_UP:
                print(square.area())
                print(rectangle.perimeter())
            if event.key == K_ESCAPE:
                print('Quit')
                running = False
        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)

    screen.fill((0, 0, 0))

    surf_center = (
       (SCREEN_WIDTH-player.surf.get_width())/2,
       (SCREEN_HEIGHT-player.surf.get_height())/2
    )

    screen.blit(player.surf, player.rect)

    pygame.display.flip()

pygame.quit()
