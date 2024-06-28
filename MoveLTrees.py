import pygame
import random
import time

screen = pygame.display.set_mode((798,574))
#Left Side
left_tree1_X = 70
left_tree1_Y = 220

left_tree2_X = 25
left_tree2_Y = 495

left_tree3_X = 100
left_tree3_Y = 397

left_tree4_X = 25
left_tree4_Y = 158

left_tree5_X = 48
left_tree5_Y = 79

left_tree6_X = 61
left_tree6_Y = 297


Change_Y = 2
def movement_of_left_trees():
  global left_tree1_X
  global left_tree1_Y
  global left_tree2_X
  global left_tree2_Y
  global left_tree3_X
  global left_tree3_Y
  global left_tree4_X
  global left_tree4_Y
  global left_tree5_X
  global left_tree5_Y
  global left_tree6_X
  global left_tree6_Y
  global Change_Y
  tree = pygame.image.load("tree.png")
  screen.blit(tree,(left_tree1_X,left_tree1_Y))
  screen.blit(tree,(left_tree2_X,left_tree2_Y))
  screen.blit(tree,(left_tree3_X,left_tree3_Y))
  screen.blit(tree,(left_tree4_X,left_tree4_Y))
  screen.blit(tree,(left_tree5_X,left_tree5_Y))
  screen.blit(tree,(left_tree6_X,left_tree6_Y))
  left_tree1_Y += Change_Y
  left_tree2_Y += Change_Y
  left_tree3_Y += Change_Y
  left_tree4_Y += Change_Y
  left_tree5_Y += Change_Y
  left_tree6_Y += Change_Y
  if left_tree1_Y > 600:
      left_tree1_Y = -10
      tree = pygame.image.load("tree.png")
      screen.blit(tree,(left_tree1_X,left_tree1_Y))
  elif left_tree2_Y > 600:
      left_tree2_Y = -10
      tree = pygame.image.load("tree.png")
      screen.blit(tree,(left_tree2_X,left_tree2_Y))
  elif left_tree3_Y > 600:
      left_tree3_Y = -10
      tree = pygame.image.load("tree.png")
      screen.blit(tree,(left_tree3_X,left_tree3_Y))
  elif left_tree4_Y > 600:
      left_tree4_Y = -10
      tree = pygame.image.load("tree.png")
      screen.blit(tree,(left_tree4_X,left_tree4_Y))
  elif left_tree5_Y > 600:
      left_tree5_Y = -10
      tree = pygame.image.load("tree.png")
      screen.blit(tree,(left_tree5_X,left_tree5_Y))
  elif left_tree6_Y > 600:
      left_tree6_Y = -10
      tree = pygame.image.load("tree.png")
      screen.blit(tree,(left_tree6_X,left_tree6_Y))      
