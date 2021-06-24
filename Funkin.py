import pygame
import math
#################
pygame.init()
Width = 800
Height = 600
screen = pygame.display.set_mode((Width,Height), RESIZEABLE)
mainloop = True
################Main Game Loop#################
while mainloop:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()
