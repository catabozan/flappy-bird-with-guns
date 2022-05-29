# OLD GAME: https://pastebin.pl/view/6a5325c7
import pygame
import random

pygame.init()


def collide(image1, x1, y1, image2, x2, y2):
    x = x2 - x1
    y = y2 - y1
    mask1 = pygame.mask.from_surface(image1)
    mask2 = pygame.mask.from_surface(image2)
    return mask1.overlap(mask2, (x, y)) != None


class Game:
    W_WIDTH = 1400
    W_HEIGHT = 1050
    W_BG = pygame.image.load("assets/redbg.jpeg")
    CLOCK = pygame.time.Clock()
    PIPE_SPRITE = pygame.image.load("assets/pipe.png")
    PIPES_PER_SECOND = 1.0
    pipes = []

    def __init__(self, player):
        self.window = pygame.display.set_mode((self.W_WIDTH, self.W_HEIGHT))
        self.player = player
        self.createPipe()

    def update(self):
        self.CLOCK.tick(30)
        self.window.blit(self.W_BG, (0, 0))
        self.player.update(self.window)
        for pipe in self.pipes:
            pipe.update(self.window)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player.jump()

        # Keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.player.moveLeft()
        if keys[pygame.K_d]:
            self.player.moveRight()

    def createPipe(self):
        pipe = Pipe(self.PIPE_SPRITE, self.W_WIDTH)
        self.pipes.append(pipe)


class Player:
    Y_ACCELERATION = 10
    X_ACCELERATION = 10
    y = 100
    vy = 0
    x = 100
    vx = 0
    sprite = pygame.image.load("assets/ghost.png")

    def __init__(self):
        self.sprite = pygame.transform.scale(self.sprite, (150, 150))

    def moveLeft(self):
        self.vx = -1 * self.X_ACCELERATION

    def moveRight(self):
        self.vx = self.X_ACCELERATION

    def jump(self):
        self.vy = -1 * self.Y_ACCELERATION

    def update(self, window):
        # Move vertically
        self.y = self.y + self.vy
        self.vy = self.vy + 1

        # Move horizontally
        self.x = self.x + self.vx
        if self.vx < 0:
            self.vx = self.vx + 1
        if self.vx > 0:
            self.vx = self.vx - 1

        # Draw player
        window.blit(self.sprite, (self.x, self.y))


class Pipe:
    MIN_PIPE_Y = -900
    MAX_PIPE_Y = -150
    GAP_Y_OFFSET = 930
    GAP_X_SIZE = 200
    GAP_Y_SIZE = 120
    X_ACCELERATION = -8

    def __init__(self, sprite, x):
        self.sprite = pygame.transform.scale(sprite, (120, 2100))
        self.y = random.randrange(self.MIN_PIPE_Y, self.MAX_PIPE_Y, 50)
        self.x = x

    def update(self, window):
        self.x = self.x + self.X_ACCELERATION
        window.blit(self.sprite, (self.x, self.y))


player = Player()
game = Game(player)

while True:

    game.update()

    # if collide(player.sprite, player.x, player.y, pipe_img, 300, max_pipe_y):
    #     quit()

    pygame.display.update()
