# game.py
#
# Cameron's Super-Fun Game
# Just a simple (and hopefully) fun game
#
VERSION = "0.1"

try:
    import sys
    import pygame
    import random
    from pygame.locals import (
    RLEACCEL,
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

        self.change_x = 0
        self.change_y = 0

        self.flying_frames_l = []
        self.flying_frames_r = []

        self. direction = "R"
 
        sprite_sheet = SpriteSheet("bluejaySpritesheet.png")
        image = sprite_sheet.getImage(66, 0, 30, 30)
        self.flying_frames_r.append(image)
        image = sprite_sheet.getImage(66, 0, 66, 90)
        self.flying_frames_r.append(image)
        image = sprite_sheet.getImage(132, 0, 67, 90)
        self.flying_frames_r.append(image)

        image = sprite_sheet.getImage(66, 0, 30, 30)
        image = pygame.transform.flip(image, True, False)
        self.flying_frames_l.append(image)
        image = sprite_sheet.getImage(66, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.flying_frames_l.append(image)
        image = sprite_sheet.getImage(132, 0, 67, 90)
        image = pygame.transform.flip(image, True, False)
        self.flying_frames_l.append(image)

        self.image = self.flying_frames_l[0]

        self.image.set_colorkey((225, 225, 225), RLEACCEL)
        self.rect = self.image.get_rect()
   
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()

        self.flying_frames_l = []

        self. direction = "L"
        
        sprite_sheet = SpriteSheet("redjaySpritesheet.png")
        image = sprite_sheet.getImage(0, 0, 30, 30)
        self.flying_frames_l.append(image)
        image = sprite_sheet.getImage(66, 0, 66, 90)
        self.flying_frames_l.append(image)
        image = sprite_sheet.getImage(132, 0, 67, 90)
        self.flying_frames_l.append(image)

        self.image = self.flying_frames_l[0]
        

        self.image.set_colorkey((225, 225, 225), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(1, 1)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

#class Cloud(pygame.sprite.Sprite):
#    def __init__(self) -> None:
#        super(Cloud, self).__init__()
#        self.surf = pygame.image.load

class SpriteSheet():
    sprite_sheet = None
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()
    
    def getImage(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((225, 225, 225), RLEACCEL)
        return image

pygame.init()
        
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

player = Player()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    enemies.update()

    screen.fill((0, 0, 0))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False

    pygame.display.flip()

pygame.quit()
