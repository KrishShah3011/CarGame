import math
import sqlite3
from MoveLHuman import *
from MoveLStones import *
from MoveLTrees import *
from MoveRHuman import *
from MoveRStones import *
from MoveRTrees import *from MoveYellowStrip import *

clock = pygame.time.Clock()
pygame.init()


#  refuelsound = pygame.mixer.Sound("refuel.wav")
#  collisionsound = pygame.mixer.Sound("collision.wav")
#  oilspillsound = pygame.mixer.Sound("oilspill.wav")
#  music = pygame.mixer.music.load("music.mp3")
#  pygame.mixer.music.play(-1)


#  Side View
def side_view():
    movement_of_right_trees()
    movement_of_left_stones()
    movement_of_left_trees()
    movement_of_right_stones()
    movement_of_left_human()
    movement_of_right_human()
    show_yellow_strip()


#  BACKGROUND image
screen = pygame.display.set_mode((798, 574))
background = pygame.image.load("road.png")
yellow_strip = pygame.image.load("yellowstrip.png")
pygame.display.set_caption("Hurdle Hit")
icon = pygame.image.load("iconcar.png")
pygame.display.set_icon(icon)
oil = pygame.image.load("oilspill.png")

#  Initialze Database Connection
Database = sqlite3.connect("Score.db")
Cursor_of_Database = Database.cursor()

#  Car
carX = 367
carY = 505
carXchange = 0
carnum = 5


def car(x, y):
    global carX
    global carY
    car = pygame.image.load("car.png")
    screen.blit(car, (carX, carY))


def car_boundaries(x, y):
    global carX
    global carY
    if carX < 150:
        carX = 150
    elif carX > 584:
        carX = 584


num = 5
#  Hurdle
hole1X = random.randint(160, 580)
hole1Y = random.randint(-128, -64)
holeX = random.randint(160, 580)
holeY = random.randint(-128, -64)
jumpX = random.randint(160, 580)
jumpY = random.randint(-128, -64)
jump1X = random.randint(160, 580)
jump1Y = random.randint(-128, -64)
ob3 = False


def jump():
    global jumpX
    global jumpY
    global jump_running
    global num
    jumpXchange = 0
    jumpYchange = num
    jumpY += jumpYchange
    jump = pygame.image.load("hurdle.png")
    screen.blit(jump, (jumpX, jumpY))

    if jumpY > 570:
        jump_running = False
        jumpX = random.randint(160, 580)
        jumpY = random.randint(-128, -64)


def jump1():
    global jump1X
    global jump1Y
    global jump_running
    global num
    global ob3
    jumpXchange = 0
    jumpYchange = num
    jump1Y += jumpYchange
    jump = pygame.image.load("hurdle.png")
    screen.blit(jump, (jump1X, jump1Y))

    if jump1Y > 570:
        jump_running = False
        jump1X = random.randint(160, 580)
        jump1Y = random.randint(-128, -64)
        ob3 = True


def hole():
    global holeX
    global holeY
    global jump_running
    global num
    holeXchange = 0
    holeYchange = num
    holeY += holeYchange
    hole = pygame.image.load("hole.png")
    screen.blit(hole, (holeX, holeY))

    if holeY > 570:
        jump_running = True
        holeX = random.randint(160, 580)
        holeY = random.randint(-128, -64)


def hole1():
    global hole1X
    global hole1Y
    global jump_running
    global num
    global ob3
    holeXchange = 0
    holeYchange = num
    hole1Y += holeYchange
    hole = pygame.image.load("hole.png")
    screen.blit(hole, (hole1X, hole1Y))

    if hole1Y > 570:
        jump_running = True
        hole1X = random.randint(160, 580)
        hole1Y = random.randint(-128, -64)
        ob3 = False


level = True
level3 = False

jump_running = True


def hurdles():
    global jump_running
    global jumpX
    global jumpY
    global holeX
    global holeY
    global jump1X
    global jump1Y
    global hole1X
    global hole1Y
    global score
    global level
    global level3
    if level:
        if jump_running is True:
            jump()
        elif jump_running is False:
            hole()
        if score == 15:
            level3 = True
            level = False
    if level3:
        if jump_running is True:
            if jumpX - holeX > 100:
                jump()
                hole()
            else:
                holeX = random.randint(160, 580)
                holeY = random.randint(-128, -64)
                jumpX = random.randint(160, 580)
                jumpY = random.randint(-128, -64)
        elif jump_running is False:
            if jumpX - holeX > 100:
                hole()
                jump()
            else:
                holeX = random.randint(160, 580)
                holeY = random.randint(-128, -64)
                jumpX = random.randint(160, 580)
                jumpY = random.randint(-128, -64)
    if score >= 30:
        level3 = False
        if ob3:
            if jumpX - holeX >= 100 and holeX - hole1X >= 50:
                jump()
                hole()
                hole1()
            else:
                holeX = random.randint(300, 430)
                holeY = random.randint(-128, -64)
                jumpX = random.randint(450, 580)
                jumpY = random.randint(-128, -64)
                hole1X = random.randint(160, 280)
                hole1Y = random.randint(-128, -64)

        if not ob3:
            if holeX - jumpX >= 100 and jumpX - jump1X >= 50:
                hole()
                jump()
                jump1()
            else:
                holeX = random.randint(450, 580)
                holeY = random.randint(-128, -64)
                jumpX = random.randint(300, 430)
                jumpY = random.randint(-128, -64)
                jump1X = random.randint(160, 280)


refillX = random.randint(280, 300)
refillY = random.randint(-128, -64)


def refill():
    global refillX
    global refillY
    global score
    global num
    refillXchange = 0
    refillYchange = num
    refillY += refillYchange
    refill = pygame.image.load("petroleum.png")
    screen.blit(refill, (refillX, refillY))


#  Collision
def collision():
    global holeX
    global holeY
    global jumpX
    global jumpY
    global hole1X
    global hole1Y
    global jump1X
    global jump1Y
    global carX
    global carY
    global refillX
    global refillY
    distance_hole = math.sqrt((math.pow(holeX - carX, 2)) + (math.pow(holeY - carY, 2)))
    distance_jump = math.sqrt((math.pow(jumpX - carX, 2)) + (math.pow(jumpY - carY, 2)))
    distance_hole1 = math.sqrt((math.pow(hole1X - carX, 2)) + (math.pow(hole1Y - carY, 2)))
    distance_jump1 = math.sqrt((math.pow(jump1X - carX, 2)) + (math.pow(jump1Y - carY, 2)))
    distance_refill = math.sqrt((math.pow(refillX - carX, 2)) + (math.pow(refillY - carY, 2)))
    if distance_hole < 41 or distance_jump < 41 or distance_hole1 < 41 or distance_jump1 < 41 or distance_refill < 41:
        return True
    else:
        return False


#  Font
font_1 = pygame.font.SysFont("Lucida Handwriting", 32)
font_2 = pygame.font.SysFont("Lucida Handwriting", 64, False, True)
font_3 = pygame.font.SysFont("Lucida Calligraphy", 25)
font_4 = pygame.font.SysFont("Lucida Calligraphy", 15)

#  Score
score = 0


def display_level1():
    global screen
    global font_2
    global level1
    if level1:
        screen.fill((0, 0, 0))
        level_1 = font_2.render("Level 1", True, (255, 255, 255))
        screen.blit(level_1, (798 / 2 - level_1.get_rect().width / 2, 574 / 2 - level_1.get_rect().height / 2))
        pygame.display.update()
        time.sleep(1)


level1 = True
display_level2 = True
display_level3 = False
display_infinity_mode = False


def display_levels():
    global font_2
    global score
    global display_level2
    global display_level3
    global display_infinity_mode
    global num
    global carnum
    global level1
    if score == 0:
        display_level1()
        level1 = False
    if display_level2:
        num = 9
        carnum = 7
        if score == 5:
            screen.fill((0, 0, 0))
            level_2 = font_2.render("Level 2", True, (255, 255, 255))
            screen.blit(level_2, (798 / 2 - level_2.get_rect().width / 2, 574 / 2 - level_2.get_rect().height / 2))
            pygame.display.update()
            time.sleep(1)
            display_level2 = False
            display_level3 = True
    if display_level3:
        num = 11
        carnum = 9
        if score == 15:
            screen.fill((0, 0, 0))
            level_3 = font_2.render("Level 3", True, (255, 255, 255))
            screen.blit(level_3, (798 / 2 - level_3.get_rect().width / 2, 574 / 2 - level_3.get_rect().height / 2))
            pygame.display.update()
            time.sleep(1)
            display_level3 = False
            display_infinity_mode = True
    if display_infinity_mode:
        num = 13
        carnum = 10
        if score == 25:
            screen.fill((0, 0, 0))
            infinite = font_2.render("Infinite Mode", True, (255, 255, 255))
            screen.blit(infinite, (798 / 2 - infinite.get_rect().width / 2, 574 / 2 - infinite.get_rect().height / 2))
            pygame.display.update()
            time.sleep(1)
            display_infinity_mode = False
    if score == 35:
        num = 15
        carnum = 10
    elif score == 45:
        num = 17
        carnum = 12


def show_score(x, y):
    global score
    global holeY
    global jumpY
    global cargame
    global num
    global d
    boom = collision()
    if not boom and 505 <= jumpY <= 504 + num:
        score += 1
    if not boom and 505 <= holeY <= 504 + num:
        score += 1
    if not boom and 505 <= hole1Y <= 504 + num:
        score += 1
    if not boom and 505 <= jump1Y <= 504 + num:
        score += 1
    score_render = font_1.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_render, (x, y))
    score_to = font_1.render("Score to", True, (255, 255, 255))
    screen.blit(score_to, (10, 500))
    beat_d = font_1.render("beat: " + str(d), True, (255, 255, 255))
    screen.blit(beat_d, (10, 540))


m = False
oilY = 535
oilX = 0


def lives():
    global holeY
    global fuel_num
    global jumpY
    global cargame
    global num
    global play_again
    global carX
    global m
    global carY
    global oilY
    global oilX
    global jump1X
    global jump1Y
    global hole1X
    global hole1Y
    global n
    v = 0
    change = 1
    boom = collision()
    if boom and 505 <= holeY <= 504 + num:
        fuel_num += 20
        m = True
        #         collisionsound.play()
        pygame.time.delay(300)
        #         oilspillsound.play()
        oilX = carX + 50
    if boom and 505 <= jumpY <= 504 + num:
        fuel_num += 20
        m = True
        #         collisionsound.play()
        pygame.time.delay(300)
        #         oilspillsound.play()
        oilX = carX + 50
    if boom and 505 <= jump1Y <= 504 + num:
        fuel_num += 20
        m = True
        #         collisionsound.play()
        pygame.time.delay(300)
        #  oilspillsound.play()
        # oilX = carX + 50
    if boom and 505 <= hole1Y <= 504 + num:
        fuel_num += 20
        m = True
        # collisionsound.play()
        pygame.time.delay(300)
        # oilspillsound.play()
        oilX = carX + 50
    if boom and 505 <= refillY <= 504 + num:
        fuel_num -= 15
        # refuelsound.play()
    if fuel_num >= 101:
        fuel_num = 101
        game_over()
        play_again = True
        n = True

    if m:
        oilY += change
        screen.blit(oil, (oilX, oilY))

        pygame.display.update()
        if oilY > 574:
            m = False
            oilY = 535


fuel_num = 0
green = False
red = False
p = True


def game_over():
    screen.fill((0, 0, 0))
    game_over = font_2.render("GAME OVER", True, (0, 255, 0))
    out_of_fuel = font_1.render("You are out of fuel!", True, (0, 255, 0))
    screen.blit(out_of_fuel, (223, 350))
    screen.blit(game_over, (195, 267))
    pygame.display.update()
    time.sleep(1.5)


def fuel():
    outline = pygame.image.load("outline.png")
    global fuel_num
    global green
    global p
    global red
    if fuel_num < 0:
        fuel_num = 0
    if fuel_num > 101:
        fuel_num = 101
    screen.blit(outline, (673, 5))
    if fuel_num <= 85:
        green = True
        red = False
    if green:
        for a in range(fuel_num, 101):
            greenline = pygame.image.load("green_line.png")
            screen.blit(greenline, (a + 680, 12))
    if fuel_num > 85:
        red = True
        green = False
    if red:
        for a in range(fuel_num, 101):
            redline = pygame.image.load("red_line.png")
            screen.blit(redline, (a + 680, 12))

    if fuel_num >= 86:
        if p:
            low_fuel = font_2.render("Low_fuel", True, (255, 255, 255))
            screen.blit(low_fuel, (798 / 2 - low_fuel.get_rect().width / 2, 574 / 2 - low_fuel.get_rect().height / 2))
            screen.blit(outline, (673, 5))
            pygame.display.update()
            time.sleep(0.5)
            p = False
    if fuel_num <= 85:
        p = True
    fuel = font_3.render("Fuel", True, (0, 0, 0))
    screen.blit(fuel, (695, 65))


play_again = False
over_it2 = False
click = True
over_it = False
rules = False
controls = False
while click:
    screen.fill((255, 255, 255))
    PlayScreen = pygame.image.load("PlayScreen.png")
    screen.blit(PlayScreen, (0, 0))
    pygame.draw.rect(screen, (240, 250, 120), (230, 465, 100, 50))
    start = font_3.render("Start", True, (0, 0, 0))
    screen.blit(start, (244, 472))
    mouse = pygame.mouse.get_pos()
    if 330 > mouse[0] > 230:
        if 515 > mouse[1] > 465:
            pygame.draw.rect(screen, (0, 0, 0), (230, 465, 100, 50))
            start = font_3.render("Start", True, (255, 255, 255))
            screen.blit(start, (244, 472))
            over_it = True
    if mouse[0] < 230 or mouse[0] > 330:
        if mouse[1] < 465 or mouse[1] > 515:
            over_it = False
    for i in pygame.event.get():
        if over_it:
            if i.type == pygame.MOUSEBUTTONDOWN:
                rules = True
                over_it = False
        if i.type == pygame.QUIT:
            pygame.quit()
            click = False
            cargame = False
    while rules:
        rules_image = pygame.image.load("Rules.png")
        screen.blit(rules_image, (0, 0))
        pygame.display.update()
        for i in pygame.event.get():
            if i.type == pygame.MOUSEBUTTONDOWN:
                rules = False
                controls = True
            if i.type == pygame.QUIT:
                pygame.quit()
                click = False
                rules = False
                cargame = False
    while controls:
        controls_image = pygame.image.load("Controls.png")
        screen.blit(controls_image, (0, 0))
        pygame.display.update()
        for i in pygame.event.get():
            if i.type == pygame.MOUSEBUTTONDOWN:
                controls = False
                cargame = True
                click = False
            if i.type == pygame.QUIT:
                pygame.quit()
                click = False
                cargame = False
                controls = False
    pygame.display.update()

e = 1
a = 1
q = False
n = False
count = 0
fuel_num = 0
c = []
sql = "SELECT * from HIGHSCORE;"
Cursor_of_Database.execute(sql)
highscore = Cursor_of_Database.fetchall()
for b in highscore:
    b = list(b)
    c.append(b)
d = max(c)
d = str(d)
d = d[1:-1]


def save_score(x):
    global Cursor_of_Database
    global Database
    global n
    global c
    global d
    insert = "INSERT INTO HIGHSCORE(HighScore) VALUES(?);"
    Cursor_of_Database.execute(insert, (x,))
    Database.commit()
    sql = "SELECT * from HIGHSCORE;"
    Cursor_of_Database.execute(sql)
    highscore = Cursor_of_Database.fetchall()
    for b in highscore:
        b = list(b)
        c.append(b)
    d = max(c)
    d = str(d)
    d = d[1:-1]
    n = False
    cargame = False


while cargame:
    clock.tick(60)
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cargame = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                carXchange = -carnum
                fuel_num += 1
                e += 1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                carXchange = carnum
                fuel_num += 1
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RSHIFT:
                cargame = False
                pygame.quit()
            if event.key == pygame.K_KP0 or event.key == pygame.K_f:
                count += a
                remainder = count % 2
                while remainder == 1:
                    screen.blit(background, (0, 0))
                    side_view()
                    car(367, 505)
                    pause = font_2.render("Paused", True, (20, 20, 20))
                    screen.blit(pause, (260, 50))
                    pausesign = pygame.image.load("pause.png")
                    screen.blit(pausesign, (383, 130))
                    cargame = False
                    pygame.display.update()
                    for r in pygame.event.get():
                        if r.type == pygame.KEYDOWN:
                            if r.key == pygame.K_KP0 or r.key == pygame.K_f:
                                count += 1
                                remainder = count % 2
                                if remainder == 0:
                                    cargame = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_a:
                carXchange = 0
                fuel_num += 0

    display_levels()
    side_view()
    carX += carXchange
    car(carX, carY)
    car_boundaries(carX, carY)
    hurdles()
    show_score(10, 10)
    if score % 2 == 0:
        if score % 12 == 0:
            if 285 < jumpY < 299 + num:
                q = True
            if 285 < holeY < 299 + num:
                q = True
            if 285 < hole1Y < 299 + num:
                q = True
            if 285 < jump1Y < 299 + num:
                q = True
    if q:
        refill()
        if refillY > 570:
            refillX = random.randint(160, 580)
            refillY = random.randint(-128, -64)
            q = False
    fuel()
    lives()

    if n:
        save_score(score)
    pygame.display.update()

    while play_again:  #  Reset value
        screen.blit(background, (0, 0))
        side_view()
        car(367, 505)
        pygame.draw.rect(screen, (240, 250, 120), (350, 275, 100, 50))
        Play = font_4.render("Play", True, (0, 0, 0))
        Again = font_4.render("Again", True, (0, 0, 0))
        screen.blit(Play, (377, 280))
        screen.blit(Again, (370, 300))
        mouse = pygame.mouse.get_pos()
        if 450 > mouse[0] > 350:
            if 315 > mouse[1] > 275:
                pygame.draw.rect(screen, (0, 0, 0), (350, 275, 100, 50))
                Play = font_4.render("Play", True, (255, 255, 255))
                Again = font_4.render("Again", True, (255, 255, 255))
                screen.blit(Play, (377, 280))
                screen.blit(Again, (370, 300))
                over_it2 = True
        if mouse[0] < 350 or mouse[0] > 450:
            if mouse[1] < 275 or mouse[1] > 315:
                over_it2 = False
        for j in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if j.type == pygame.MOUSEBUTTONDOWN:
                if over_it2:
                    cargame = True
                    score = 0
                    num = 7
                    carnum = 5
                    level = True
                    level3 = False
                    level1 = True
                    display_level2 = True
                    display_level3 = False
                    fuel_num = 0
                    display_infinity_mode = False
                    play_again = False
                    over_it2 = False
            if j.type == pygame.KEYDOWN:
                if j.key == pygame.K_s or j.key == pygame.K_DOWN:
                    cargame = True
                    score = 0
                    num = 7
                    carnum = 5
                    level = True
                    level3 = False
                    level1 = True
                    fuel_num = 0
                    display_level2 = True
                    display_level3 = False
                    display_infinity_mode = False
                    play_again = False
                    over_it2 = False
                if j.key == pygame.K_ESCAPE or j.key == pygame.K_RSHIFT:
                    play_again = False
                    pygame.quit()
            if j.type == pygame.QUIT:
                pygame.quit()
                play_again = False
        pygame.display.update()
