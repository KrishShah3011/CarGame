import pygame
import random
import time

screen = pygame.display.set_mode((798,574))

Change_Y = 2
left_stone1_X = 35
left_stone1_Y = 458

left_stone2_X = 100
left_stone2_Y = 150

left_stone3_X = 25
left_stone3_Y = 137

left_stone4_X = 48
left_stone4_Y = 40

left_stone5_X = 61
left_stone5_Y = 264

left_stone6_X = 61
left_stone6_Y = 590

if left_stone1_Y > 600:
  left_stone6_Y = 40
  left_stone6_X = 10
  tree = pygame.image.load("stone.png")
  screen.blit(tree,(left_stone6_X,left_stone6_Y))

def movement_of_left_stones():
  global left_stone1_X
  global left_stone1_Y
  global left_stone2_X
  global left_stone2_Y
  global left_stone3_X
  global left_stone3_Y
  global left_stone4_X
  global left_stone4_Y
  global left_stone5_X
  global left_stone5_Y
  global left_stone6_X
  global left_stone6_Y
  global Change_Y
  stone = pygame.image.load("stone.png")
  screen.blit(stone,(left_stone1_X,left_stone1_Y))
  screen.blit(stone,(left_stone2_X,left_stone2_Y))
  screen.blit(stone,(left_stone3_X,left_stone3_Y))
  screen.blit(stone,(left_stone4_X,left_stone4_Y))
  screen.blit(stone,(left_stone5_X,left_stone5_Y))
  screen.blit(stone,(left_stone6_X,left_stone6_Y))
  left_stone1_Y += Change_Y
  left_stone2_Y += Change_Y
  left_stone3_Y += Change_Y
  left_stone4_Y += Change_Y
  left_stone5_Y += Change_Y
  left_stone6_Y += Change_Y
  if left_stone1_Y > 600:
      left_stone1_Y = -10
      stone = pygame.image.load("stone.png")
      screen.blit(stone,(left_stone1_X,left_stone1_Y))
  elif left_stone2_Y > 600:
      left_stone2_Y = -10
      stone = pygame.image.load("stone.png")
      screen.blit(stone,(left_stone2_X,left_stone2_Y))
  elif left_stone3_Y > 600:
      left_stone3_Y = -10
      stone = pygame.image.load("stone.png")
      screen.blit(stone,(left_stone3_X,left_stone3_Y))
  elif left_stone4_Y > 600:
      left_stone4_Y = -10
      stone = pygame.image.load("stone.png")
      screen.blit(stone,(left_stone4_X,left_stone4_Y))
  elif left_stone5_Y > 600:
      left_stone5_Y = -10
      stone = pygame.image.load("stone.png")
      screen.blit(stone,(left_stone5_X,left_stone5_Y))
  elif left_stone6_Y > 600:
      left_stone6_Y = -10
      stone = pygame.image.load("stone.png")
      screen.blit(stone,(left_stone6_X,left_stone6_Y))
  
