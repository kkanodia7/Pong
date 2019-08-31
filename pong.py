print("PONG\n")
mode = False
gamemode = False
player1mode = False
player2mode = False
enemymode = False
trackdistance = False
specmode = False
turns = False
while gamemode == False:
    gamemode = input("Game Mode: SinglePlayer(1), Multiplayer(2), or Spectate(3)? ")
    '''
    if gamemode == "0":
        gamemode = random.randrange(1,4)
        gamemode = str(gamemode)
        '''
    if gamemode == "1":
        while enemymode == False:
            enemymode = input("Enemy Mode: Easy(1), Hard(2), Wall(3), or Mirror(4)? ")
            '''
            if enemymode == "0":
                enemymode = random.randrange(1,5)
                enemymode = str(enemymode)
                '''
            if enemymode == "1" or enemymode == "2":
                if enemymode == "1":
                    espeed = 1.5
                elif enemymode == "2":
                    espeed = 2.0
            elif enemymode != "1" and enemymode != "2" and enemymode != "3" and enemymode != "4":
                enemymode = False

    elif gamemode == "2":
        while player2mode == False:
            player2mode = input("Player 2 Mode: Control(1) or Constant(2)? ")
            '''
            if player2mode == "0":
                player2mode = random.randrange(1,3)
                player2mode = str(player2mode)
                '''
            if player2mode != "1" and player2mode != "2":
                player2mode = False

    elif gamemode == "3":
        while specmode == False:
            specmode = input("Player Modes: Easy(1) or Hard(2)? ")
            '''
            if specmode == "0":
                specmode = random.randrange(1,3)
                specmode = str(specmode)
                '''
            if specmode == "1":
                tracker = 300
                tracker2 = 900
                espeed = 1.5
                enemymode = "1"
            elif specmode == "2":
                tracker = 1200
                tracker2 = 0
                espeed = 2
                enemymode = "2"
            elif specmode != "1" and specmode != "2":
                specmode = False
    while trackdistance == False and (enemymode == "1" or enemymode == "2" or gamemode == "3"):
        trackdistance = input("Enemy Vision Distance: 300(1), 600(2), 900(3), or 1200(4)? ")
        '''
        if trackdistance == "0":
            trackdistance = random.randrange(1,5)
            trackdistance = str(trackdistance)
            '''
        if trackdistance == "1":
            tracker, tracker2 = 300, 900
        elif trackdistance == "2":
            tracker, tracker2 = 600, 600
        elif trackdistance == "3":
            tracker, tracker2 = 900, 300
        elif trackdistance == "4":
            tracker, tracker2 = 1200, 0
        else:
            trackdistance = False

    if gamemode != "1" and gamemode != "2" and gamemode != "3":
        gamemode = False
while player1mode == False and gamemode != "3":
    player1mode = input("Player 1 Mode: Control(1) or Constant(2)? ")
    '''
    if player1mode == "0":
        player1mode = random.randrange(1,3)
        player1mode = str(player1mode)
        '''
    if player1mode != "1" and player1mode != "2":
        player1mode = False
while turns == False and enemymode != "4":
    turns = input("Turns: Yes(1) or No(2)? ")
    '''
    if turns == "0":
        turns = random.randrange(1,3)
        turns = str(turns)
        '''
    if turns != "1" and turns != "2":
        turns = False

print("\n\n")

wallif = r"Images/PongPaddle.png"
ballif = r"Images/PongBall.png"
bgif = r"Images/PongBG.jpg"
import pygame, sys, os
from random import randrange
from pygame.locals import *


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)
pygame.init()
screen = pygame.display.set_mode((1200, 600), 0, 32)
pygame.display.set_caption("Pong")
background = pygame.image.load(bgif).convert()
char = pygame.image.load(wallif).convert_alpha()
enemy = pygame.image.load(wallif).convert_alpha()
ball = pygame.image.load(ballif).convert_alpha()
pygame.mouse.set_visible(False)
pygame.display.set_icon(ball)
ballspeed = 1
x, y = 1190, 260
movey1 = 0
movey2 = 0
ex, ey = 0, 260
bx, by = 595, 275
bmx, bmy = randrange(-1, 1), randrange(-10, 10) / 10
if bmx == 0:
    bmx = 1
    pturn = True
else:
    pturn = False
if bmy == 0:
    bmy = 1
score1 = 0
score2 = 0
first = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and gamemode != "3":
            if event.key == K_UP:
                movey1 = -1.5
            if event.key == K_DOWN:
                movey1 = +1.5
        if event.type == KEYDOWN and gamemode != "3":
            if event.key == K_q and gamemode == "2":
                movey2 = -1.5
            if event.key == K_a and gamemode == "2":
                movey2 = +1.5

        if event.type == KEYUP:
            if (event.key == K_UP or event.key == K_DOWN) and player1mode == "1":
                movey1 = 0
            if (event.key == K_q or event.key == K_a) and player2mode == "1":
                movey2 = 0

    if y <= 20:
        movey1 = 0
        y = 21
    if y >= 541:
        movey1 = 0
        y = 540
    if (turns == "1" and pturn == True) or turns != "1":
        y += movey1

    bx += bmx
    by += bmy

    if bx + 10 > x and bx - 10 < x and by + 10 > y and by - 40 < y:
        pturn = False
        bmx += .1
        bmx *= -1
        if bmy > 0:
            bmy = randrange(1, 16) / 10 - bmx - 1
        elif bmy < 0:
            bmy = randrange(-15, 0) / 10 + bmx + 1
        score1 += 1
    if by < 20 or by > 570:
        bmy *= -1
    if gamemode == "1" or gamemode == "3":
        if enemymode == "1" or enemymode == "2":
            if (turns == "1" and pturn == False) or turns != "1":
                if ey + 15 < by and bx < tracker and ey < 539:
                    ey += espeed
                if ey + 15 > by and bx < tracker and ey > 21:
                    ey -= espeed
        elif enemymode == "3":
            if ey + 15 < by and ey < 539:
                ey = by - 15
            if ey + 15 > by and ey > 21:
                ey = by - 15
        elif enemymode == "4":
            ey = y
    if gamemode == "3":
        if specmode == "1" or specmode == "2":
            if (turns == "1" and pturn == True) or turns != "1":
                if y + 15 < by and bx + 10 > tracker2 and y < 539:
                    y += espeed
                if y + 15 > by and bx + 10 > tracker2 and y > 21:
                    y -= espeed
    elif gamemode == "2":
        if (turns == "1" and pturn == False) or turns != "1":
            ey += movey2
            if ey > 539:
                ey = 539
            if ey < 21:
                ey = 21
    if bx + 10 > ex and bx - 10 < ex and by + 10 > ey and by - 40 < ey:
        pturn = True
        bmx *= -1
        bmx += .1
        if bmy > 0:
            bmy = randrange(1, 16) / 10 + bmx - 1
        elif bmy < 0:
            bmy = randrange(-15, 0) / 10 - bmx + 1
        score2 += 1
    if bx > 1190 and (by + 10 < y or by > y + 40):
        if gamemode == "1":
            if enemymode != "4":
                print("You lose! Your score was", score1)
            elif enemymode == "4":
                print("You lose! Your score was", score1 + score2)
        elif gamemode == "2" or gamemode == "3":
            print("Player 2 wins!\nPlayer 1 score:  ", score1, "\nPlayer 2 score:  ", score2)
        pygame.quit()
        sys.exit()
    if bx < 0 and (by + 10 < ey or by > ey + 40):
        if gamemode == "1":
            if enemymode != "4":
                print("You win! Your score was", score1)
            elif enemymode == "4":
                print("You lose! Your score was", score1 + score2)
        elif gamemode == "2" or gamemode == "3":
            print("Player 1 wins!\nPlayer 1 score:  ", score1, "\nPlayer 2 score:  ", score2)
        pygame.quit()
        sys.exit()

    screen.blit(background, (0, 0))
    screen.blit(char, (x, y))
    screen.blit(enemy, (ex, ey))
    screen.blit(ball, (bx, by))
    pygame.display.update()
    if first == True:
        pygame.time.wait(1000)
        first = False