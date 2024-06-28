import pygame
import random
import time

screen = pygame.display.set_mode((798,574))
#right Side
right_tree1_X = 658
right_tree1_Y = 188

right_tree2_X = 700
right_tree2_Y = 239

right_tree3_X = 698
right_tree3_Y = 364

right_tree4_X = 650
right_tree4_Y = -30

right_tree5_X = 728
right_tree5_Y = 70

right_tree6_X = 714
right_tree6_Y = 465

Change_Y = 2
if right_tree2_Y > 580:
    right_tree4_Y = -30
    right_tree4_X = 650
    tree = pygame.image.load("tree.png")
    screen.blit(tree,(right_tree4_X,right_tree4_Y))
def movement_of_right_trees():
  global right_tree1_X
  global right_tree1_Y
  global right_tree2_X
  global right_tree2_Y
  global right_tree3_X
  global right_tree3_Y
  global right_tree4_X
  global right_tree4_Y
  global right_tree5_X
  global right_tree5_Y
  global right_tree6_X
  global right_tree6_Y
  global Change_Y
  tree = pygame.image.load("tree.png")
  screen.blit(tree,(right_tree1_X,right_tree1_Y))
  screen.blit(tree,(right_tree2_X,right_tree2_Y))
  screen.blit(tree,(right_tree3_X,right_tree3_Y))
  screen.blit(tree,(right_tree4_X,right_tree4_Y))
  screen.blit(tree,(right_tree5_X,right_tree5_Y))
  screen.blit(tree,(right_tree6_X,right_tree6_Y))
  right_tree1_Y += Change_Y
  right_tree2_Y += Change_Y
  right_tree3_Y += Change_Y
  right_tree4_Y += Change_Y
  right_tree5_Y += Change_Y
  right_tree6_Y += Change_Y
  if right_tree1_Y > 600:
      right_tree1_Y = -10
      tree = pygame.image.load("tree.png")
      screen.blit(tree,(right_tree1_X,right_tree1_Y))
  elif right_tree2_Y > 600:
      right_tree2_Y = -10
      tree = pygame.image.load("tree.png")
      screen.blit(tree,(right_tree2_X,right_tree2_Y))
  elif right_tree3_Y > 600:
      right_tree3_Y = -10
      tree = pygame.image.load("tree.png")
      screen.blit(tree,(right_tree3_X,right_tree3_Y))
  elif right_tree4_Y > 600:
      right_tree4_Y = -10
      tree = pygame.image.load("tree.png")
      screen.blit(tree,(right_tree4_X,right_tree4_Y))
  elif right_tree5_Y > 600:
      right_tree5_Y = -10
      tree = pygame.image.load("tree.png")
      screen.blit(tree,(right_tree5_X,right_tree5_Y))
  elif right_tree6_Y > 600:
      right_tree6_Y = -10
      tree = pygame.image.load("tree.png")
      screen.blit(tree,(right_tree6_X,right_tree6_Y))    
