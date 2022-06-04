import pygame


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
