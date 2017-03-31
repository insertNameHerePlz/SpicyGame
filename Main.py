import pygame
from sprite import Sprite
from pygame.locals import *
flags = DOUBLEBUF
from Renderer import setSurface, drawAll

pygame.init()
screen = pygame.display.set_mode((1280, 768), flags)
done = False
setSurface(screen)
memelord = Sprite()
memelord.loadAssets("test.txt")
#memelord.play("dab")


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        drawAll()
