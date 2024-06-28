import pygame
import random
import time

screen = pygame.display.set_mode((798,574))

Change_Y = 2
right_stone1_X = 650
right_stone1_Y = 350

right_stone2_X = 741
right_stone2_Y = 430

right_stone3_X = 710
right_stone3_Y = 150

right_stone5_X = 760
right_stone5_Y = 285

right_stone6_X = 675
right_stone6_Y = 520

def movement_of_right_stones():
  global right_stone1_X
  global right_stone1_Y
  global right_stone2_X
  global right_stone2_Y
  global right_stone3_X
  global right_stone3_Y
  global right_stone5_X
  global right_stone5_Y
  global right_stone6_X
  global right_stone6_Y
  global Change_Y
  stone = pygame.image.load("stone.png")
  screen.blit(stone,(right_stone1_X,right_stone1_Y))
  screen.blit(stone,(right_stone2_X,right_stone2_Y))
  screen.blit(stone,(right_stone3_X,right_stone3_Y))
  screen.blit(stone,(right_stone5_X,right_stone5_Y))
  screen.blit(stone,(right_stone6_X,right_stone6_Y))
  right_stone1_Y += Change_Y
  right_stone2_Y += Change_Y
  right_stone3_Y += Change_Y
  right_stone5_Y += Change_Y
  right_stone6_Y += Change_Y
  if right_stone1_Y > 600:
      right_stone1_Y = -10
      stone = pygame.image.load("stone.png")
      screen.blit(stone,(right_stone1_X,right_stone1_Y))
  elif right_stone2_Y > 600:
      right_stone2_Y = -10
      stone = pygame.image.load("stone.png")
      screen.blit(stone,(right_stone2_X,right_stone2_Y))
  elif right_stone3_Y > 600:
      right_stone3_Y = -10
      stone = pygame.image.load("stone.png")
      screen.blit(stone,(right_stone3_X,right_stone3_Y))
  elif right_stone5_Y > 600:
      right_stone5_Y = -10
      stone = pygame.image.load("stone.png")
      screen.blit(stone,(right_stone5_X,right_stone5_Y))
  elif right_stone6_Y > 600:
      right_stone6_Y = -10
      stone = pygame.image.load("stone.png")
      screen.blit(stone,(right_stone6_X,right_stone6_Y))

