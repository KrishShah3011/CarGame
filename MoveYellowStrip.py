import pygame
pygame.init()

screen = pygame.display.set_mode((798,574))

ChangeYellowStripY = 2
yellowstrip_X = 394
yellowstrip1_Y = -10
yellowstrip2_Y = 100
yellowstrip3_Y = 210
yellowstrip4_Y = 320
yellowstrip5_Y = 430
yellowstrip6_Y = 540
yellowstrip7_Y = 650

def show_yellow_strip():
    global yellow_strip
    global ChangeYellowStripY
    global yellowstrip_X
    global yellowstrip1_Y
    global yellowstrip2_Y
    global yellowstrip3_Y
    global yellowstrip4_Y
    global yellowstrip5_Y
    global yellowstrip6_Y
    global yellowstrip7_Y
    yellow_strip = pygame.image.load("yellowstrip.png")
    screen.blit(yellow_strip,(yellowstrip_X,yellowstrip1_Y))
    screen.blit(yellow_strip,(yellowstrip_X,yellowstrip2_Y))
    screen.blit(yellow_strip,(yellowstrip_X,yellowstrip3_Y))
    screen.blit(yellow_strip,(yellowstrip_X,yellowstrip4_Y))
    screen.blit(yellow_strip,(yellowstrip_X,yellowstrip5_Y))
    screen.blit(yellow_strip,(yellowstrip_X,yellowstrip6_Y))
    screen.blit(yellow_strip,(yellowstrip_X,yellowstrip7_Y))
    yellowstrip1_Y += ChangeYellowStripY
    yellowstrip2_Y += ChangeYellowStripY
    yellowstrip3_Y += ChangeYellowStripY
    yellowstrip4_Y += ChangeYellowStripY
    yellowstrip5_Y += ChangeYellowStripY
    yellowstrip6_Y += ChangeYellowStripY
    yellowstrip7_Y += ChangeYellowStripY
    if yellowstrip1_Y > 649:
        yellowstrip1_Y = -120
        yellow_strip = pygame.image.load("yellowstrip.png")
        screen.blit(yellow_strip,(yellowstrip_X,yellowstrip1_Y))
    elif yellowstrip2_Y > 649:
        yellowstrip2_Y = -120
        yellow_strip = pygame.image.load("yellowstrip.png")
        screen.blit(yellow_strip,(yellowstrip_X,yellowstrip2_Y))
    elif yellowstrip3_Y > 649:
        yellowstrip3_Y = -120
        yellow_strip = pygame.image.load("yellowstrip.png")
        screen.blit(yellow_strip,(yellowstrip_X,yellowstrip3_Y))
    elif yellowstrip4_Y > 649:
        yellowstrip4_Y = -120
        yellow_strip = pygame.image.load("yellowstrip.png")
        screen.blit(yellow_strip,(yellowstrip_X,yellowstrip4_Y))
    elif yellowstrip5_Y > 649:
        yellowstrip5_Y = -120
        yellow_strip = pygame.image.load("yellowstrip.png")
        screen.blit(yellow_strip,(yellowstrip_X,yellowstrip5_Y))
    elif yellowstrip6_Y > 649:
        yellowstrip6_Y = -120
        yellow_strip = pygame.image.load("yellowstrip.png")
        screen.blit(yellow_strip,(yellowstrip_X,yellowstrip6_Y))
    elif yellowstrip7_Y > 649:
        yellowstrip7_Y = -120
        yellow_strip = pygame.image.load("yellowstrip.png")
        screen.blit(yellow_strip,(yellowstrip_X,yellowstrip7_Y))

