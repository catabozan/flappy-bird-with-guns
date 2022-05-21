import pygame

# CONSTANTS
DISPLAY_WIDTH = 1400
DISPLAY_HEIGHT = 1050

pygame.init()

window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

bg = pygame.image.load("flappy_bg.png")

y = 100
vy = 0

clock = pygame.time.Clock()

while True:
    clock.tick(30)

    window.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                vy = -20

    y = y + vy
    vy = vy + 1

    pygame.draw.rect(window, (255, 255, 255), (100, y, 50, 50))

    pygame.display.update()
