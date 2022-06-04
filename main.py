# OLD GAME: https://pastebin.pl/view/6a5325c7
import pygame
from game import Game
from player import Player

pygame.init()

player = Player()
game = Game(player)

while True:

    game.update()

    pygame.display.update()
