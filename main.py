# OLD GAME: https://pastebin.pl/view/6a5325c7
import pygame
from game import Game
from player import Player

pygame.init()


def collide(image1, x1, y1, image2, x2, y2):
    x = x2 - x1
    y = y2 - y1
    mask1 = pygame.mask.from_surface(image1)
    mask2 = pygame.mask.from_surface(image2)
    return mask1.overlap(mask2, (x, y)) != None


player = Player()
game = Game(player)

while True:

    game.update()

    # if collide(player.sprite, player.x, player.y, pipe_img, 300, max_pipe_y):
    #     quit()

    pygame.display.update()
