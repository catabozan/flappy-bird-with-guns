# OLD GAME: https://pastebin.pl/view/6a5325c7
import pygame

# CONSTANTS
DISPLAY_WIDTH = 1400
DISPLAY_HEIGHT = 1050

pygame.init()

window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

bg = pygame.image.load("flappy_bg.png")
bird = pygame.image.load("bird_with_gun.png")
bird = pygame.transform.scale(bird, (150, 150))

y = 100
vy = 0

x = 100
vx = 0

clock = pygame.time.Clock()

while True:
    clock.tick(30)

    window.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                vy = -20

            if event.key == pygame.K_a:
                vx = -5

            if event.key == pygame.K_d:
                vx = 5

    y = y + vy
    vy = vy + 1

    x = x + vx
    if vx < 0:
        vx = vx + 1
    if vx > 0:
        vx = vx - 1

    window.blit(bird, (x, y))

    pygame.display.update()
