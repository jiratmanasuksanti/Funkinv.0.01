import os,sys
import pygame
import math
import time
#################
pygame.init()
Width = 800
Height = 600
screen = pygame.display.set_mode((Width,Height), pygame.FULLSCREEN)
mainloop = True
############################Game Object Storage##############################
bopeebo_inst = pygame.mixer.music.load("./assets/music/Bopeebo_Inst.ogg")
bopeebo_voices = pygame.mixer.music.load("./assets/music/Bopeebo_Voices.ogg")
exitbutton_image = pygame.image.load("assets/images/exit_button.png")
pressed_exitbutton_image = pygame.image.load("assets/images/pressed_exit_button.png")
menu_music = pygame.mixer.music.load("./assets/music/freakyMenu.ogg")
confirmMenu_sounds = pygame.mixer.Sound("./assets/sounds/confirmMenu.ogg")
################Main Game Loop#################
def BacktoMenu():
  if menu_music_play == False:
    menu_music_play = True
    pygame.mixer.music.stop()
    menu_music.play()
menu_music_play = False
BacktoMenu()
while mainloop:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()
