import pygame, sys
from math import *
from pygame.locals import *
import random
from environment import *

clock = pygame.time.Clock()
clock.tick(50)
# window
WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
# player_car=pygame.image.load('player_car.png').convert_alpha()
pygame.font.init()
pygame.display.set_caption('Drive your own FERRARI 2019')
font = pygame.font.Font('freesansbold.ttf', 32)

pygame.draw.polygon(win, (90, 179, 0), [(0, 250), (0, 550), (350, 250)])
pygame.draw.polygon(win, (90, 179, 0), [(800, 250), (800, 550), (450, 250)])

pygame.draw.line(win, (255, 0, 0), (0, 550), (350, 250), 5)
pygame.draw.line(win, (255, 0, 0), (800, 550), (450, 250), 5)

pygame.draw.polygon(win, (50, 50, 255), [(0, 0), (0, 250), (800, 250), (800, 0)])
pygame.draw.circle(win, (255, 255, 42), (690, 100), 30)
# linie
x = 0
y = 375










#main loop
def main():
    while True:

        pygame.display.update()
    pass


main()
