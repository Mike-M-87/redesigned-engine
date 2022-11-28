import pygame
import sys

# General setup
pygame.init()
clock = pygame.time.Clock()

class Button:
    def __init__(self, text, pos, fontSize, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", fontSize)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        screen.blit(button1.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    player.animate()
                    self.change_text(self.feedback, bg="red")


def zoom(path, sizeX):
    return pygame.transform.smoothscale(pygame.image.load(path), (sizeX / 2, 130))


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sequence_animation = False
        self.sprites = []

        self.sprites.append(zoom("./new/Subject 6.png", 150))
        self.sprites.append(zoom("./new/Subject 7.png", 150))
        self.sprites.append(zoom("./new/Subject 8.png", 173))
        self.sprites.append(zoom("./new/Subject 9.png", 189))
        self.sprites.append(zoom("./new/Subject 10.png", 203))
        self.sprites.append(zoom("./new/Subject 11.png", 192))
        self.sprites.append(zoom("./new/Subject 12.png", 164))
        self.sprites.append(zoom("./new/Subject 12.png", 164))
        self.sprites.append(zoom("./new/Subject 14.png", 164))
        self.sprites.append(zoom("./new/Subject 14.png", 164))
        self.sprites.append(zoom("./new/Subject 14.png", 164))
        self.sprites.append(zoom("./new/Subject 12.png", 164))
        self.sprites.append(zoom("./new/Subject 12.png", 164))
        self.sprites.append(zoom("./new/Subject 16.png", 164))
        self.sprites.append(zoom("./new/Subject 16.png", 164))
        self.sprites.append(zoom("./new/Subject 16.png", 164))
        self.sprites.append(zoom("./new/Subject 12.png", 164))
        self.sprites.append(zoom("./new/Subject 12.png", 164))
        self.sprites.append(zoom("./new/Subject 11.png", 192))
        self.sprites.append(zoom("./new/Subject 10.png", 203))
        self.sprites.append(zoom("./new/Subject 9.png", 189))
        self.sprites.append(zoom("./new/Subject 8.png", 173))
        self.sprites.append(zoom("./new/Subject 7.png", 150))
        self.sprites.append(zoom("./new/Subject 6.png", 150))
        self.sprites.append(zoom("./new/Subject 17.png", 150))
        self.sprites.append(zoom("./new/Subject 17.png", 150))
        self.sprites.append(zoom("./new/Subject 18.png", 150))
        self.sprites.append(zoom("./new/Subject 18.png", 150))
        self.sprites.append(zoom("./new/Subject 19.png", 150))
        self.sprites.append(zoom("./new/Subject 19.png", 150))
        self.sprites.append(zoom("./new/Subject 18.png", 150))
        self.sprites.append(zoom("./new/Subject 18.png", 150))
        self.sprites.append(zoom("./new/Subject 17.png", 150))
        self.sprites.append(zoom("./new/Subject 17.png", 150))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.sequence_animation = True

    def update(self, speed):
        if self.sequence_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.sequence_animation = False
                button1.change_text("Animate", bg="navy")

        self.image = self.sprites[int(self.current_sprite)]
# Game Screen
screen_width = 848
screen_height = 477
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(300, 250)
moving_sprites.add(player)
bg = pygame.image.load("./new/bg.webp")

width = screen.get_width()
height = screen.get_height()
color_white = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)

fps = 0.15

button1 = Button(
    "Animate",
    (340, 430),
    fontSize=30,
    bg="navy",
    feedback="Animating"
)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player.animate()

    # Drawing
    mouse = pygame.mouse.get_pos()
    screen.fill([255, 255, 255])
    screen.blit(pygame.transform.smoothscale(bg, (848, 477)), (0, 0))

    button1.click(event)
    button1.show()

    moving_sprites.draw(screen)
    moving_sprites.update(fps)
    pygame.display.flip()
    clock.tick(60)
