# OLD GAME: https://pastebin.pl/view/6a5325c7
import pygame

# CONSTANTS
DISPLAY_WIDTH = 1400
DISPLAY_HEIGHT = 1050

pygame.init()

window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

bg = pygame.image.load("redbg.jpeg")
bird_img = pygame.image.load("bird_with_gun.png")
bird_img = pygame.transform.scale(bird_img, (150, 150))
pipe_img = pygame.image.load("pipe.png")
pipe_img = pygame.transform.scale(pipe_img, (120, 2100))


def collide(image1, x1, y1, image2, x2, y2):
    x = x2 - x1
    y = y2 - y1
    mask1 = pygame.mask.from_surface(image1)
    mask2 = pygame.mask.from_surface(image2)
    return mask1.overlap(mask2, (x, y)) != None


y = 100
vy = 0

x = 100
vx = 0

min_pipe_y = -900
max_pipe_x = -150

clock = pygame.time.Clock()

while True:
    clock.tick(30)

    window.blit(bg, (0, 0))

    window.blit(pipe_img, (300, max_pipe_x))

    # if collide(bird_img, x, y, pipe_img, 300, max_pipe_x):
    #     quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                vy = -10

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        vx = -10
    if keys[pygame.K_d]:
        vx = 10

    y = y + vy
    vy = vy + 1

    x = x + vx
    if vx < 0:
        vx = vx + 1
    if vx > 0:
        vx = vx - 1

    window.blit(bird_img, (x, y))

    pygame.display.update()
