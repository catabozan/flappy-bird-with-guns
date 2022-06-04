import pygame
from pipe import Pipe


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

        # Collisions
        if self.player.touchesPipes(self.pipes):
            self.reset()

    def createPipe(self):
        pipe = Pipe(self.PIPE_SPRITE, self.W_WIDTH)
        self.pipes.append(pipe)

    def reset(self):
        self.pipes = []
        self.player.reset()
