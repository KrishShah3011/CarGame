import pygame
import random
import time

screen = pygame.display.set_mode((798,574))

Change_Y = 2
left_human1_X = 84
left_human1_Y = 20

left_human2_X = 84
left_human2_Y = 485

def movement_of_left_human():
  global left_human1_X
  global left_human1_Y
  global left_human2_X
  global left_human2_Y
  global Change_Y
  human = pygame.image.load("oldman1.png")
  screen.blit(human,(left_human1_X,left_human1_Y))
  screen.blit(human,(left_human2_X,left_human2_Y))
  
  left_human1_Y += Change_Y
  left_human2_Y += Change_Y

  if left_human1_Y > 600:
      left_human1_Y = -10
      human = pygame.image.load("oldman1.png")
      screen.blit(human,(left_human1_X,left_human1_Y))
  elif left_human2_Y > 600:
      left_human2_Y = -10
      human = pygame.image.load("oldman1.png")
      screen.blit(human,(left_human2_X,left_human2_Y))
