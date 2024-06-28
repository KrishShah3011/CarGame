import pygame
import random
import time

screen = pygame.display.set_mode((798,574))

Change_Y = 2
right_human1_X = 648
right_human1_Y = 20

right_human2_X = 648
right_human2_Y = 440

def movement_of_right_human():
  global right_human1_X
  global right_human1_Y
  global right_human2_X
  global right_human2_Y

  global Change_Y
  human = pygame.image.load("oldman.png")
  screen.blit(human,(right_human1_X,right_human1_Y))
  screen.blit(human,(right_human2_X,right_human2_Y))

  right_human1_Y += Change_Y
  right_human2_Y += Change_Y

  if right_human1_Y > 600:
      right_human1_Y = -10
      human = pygame.image.load("oldman.png")
      screen.blit(human,(right_human1_X,right_human1_Y))
  elif right_human2_Y > 600:
      right_human2_Y = -10
      human = pygame.image.load("oldman.png")
      screen.blit(human,(right_human2_X,right_human2_Y))
