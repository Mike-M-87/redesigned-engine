import pygame
import sys

def zoom(path):
    return pygame.transform.smoothscale_by(pygame.image.load(path),1)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.attack_animation = False
        self.sprites = []

        for i in range(6, 25):
            self.sprites.append(zoom("./new/Subject {0}.png".format(i)))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def attack(self):
        self.attack_animation = True

    def update(self, speed):
        if self.attack_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.attack_animation = False

        self.image = self.sprites[int(self.current_sprite)]


# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 800
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(100, 100)
moving_sprites.add(player)

fps = 0.1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player.attack()

    # Drawing
    screen.fill((255, 255, 255))
    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update(fps)
    pygame.display.flip()
    clock.tick(60)
