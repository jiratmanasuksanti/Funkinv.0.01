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
current_selected_menu = 1
############################Game Object Storage##############################
bopeebo_inst = pygame.mixer.music.load("./assets/music/Bopeebo_Inst.ogg")
bopeebo_voices = pygame.mixer.music.load("./assets/music/Bopeebo_Voices.ogg")
exitbutton_image = pygame.image.load("assets/images/exit_button.png")
pressed_exitbutton_image = pygame.image.load("assets/images/pressed_exit_button.png")
menu_music = pygame.mixer.music.load("./assets/music/freakyMenu.ogg")
confirmMenu_sounds = pygame.mixer.Sound("./assets/sounds/confirmMenu.ogg")
maximumMenu = 1
minimumMenu = 1
################Main Game Loop#################
def create_button(self):
  screen.blit(exitbutton_image,(Width/2,Height/2))
def confirmMenu():
  confirmMenu_sounds.play()
def BacktoMenu():
  if menu_music_play == False:
    menu_music_play = True
    pygame.mixer.music.stop()
    menu_music.play()
def press_Exit():
  for counter in range(1,10):
    screen.blit(pressed_exitbutton_image,(Width/2,Height/2))
    screen.blit(exitbutton_image,(Width/2,Height/2))
    pygame.display.update()
menu_music_play = False
BacktoMenu()
while mainloop:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        if not maximumMenu == current_selected_menu:
          current_selected_menu = current_selected_menu + 1
      if event.key == pygame.K_UP:
        if not minimumMenu == current_selected_menu:
          current_selected_menu = current_selected_menu - 1
      if event.key == pygame.K_ENTER:
        if current_selected_menu == 1:
          confirmMenu()
          press_Exit()
          exit()
  create_button("exit")
  pygame.display.update()
