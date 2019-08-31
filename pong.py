# Created by Kushal Kanodia on Mar 21, 2016

from random import randrange

import os
import pygame
import sys
from pygame.locals import *

print("PONG\n")
mode = False
game_mode = False
player1mode = False
player2mode = False
enemy_mode = False
track_distance = False
spec_mode = False
turns = False
while not game_mode:
    game_mode = input("Game Mode: SinglePlayer(1), MultiPlayer(2), or Spectate(3)? ")
    if game_mode == "1":
        while not enemy_mode:
            enemy_mode = input("Enemy Mode: Easy(1), Hard(2), Wall(3), or Mirror(4)? ")
            if enemy_mode == "1" or enemy_mode == "2":
                if enemy_mode == "1":
                    enemy_speed = 1.5
                elif enemy_mode == "2":
                    enemy_speed = 2.0
            elif enemy_mode != "1" and enemy_mode != "2" and enemy_mode != "3" and enemy_mode != "4":
                enemy_mode = False

    elif game_mode == "2":
        while not player2mode:
            player2mode = input("Player 2 Mode: Control(1) or Constant(2)? ")
            if player2mode != "1" and player2mode != "2":
                player2mode = False

    elif game_mode == "3":
        while not spec_mode:
            spec_mode = input("Player Modes: Easy(1) or Hard(2)? ")
            if spec_mode == "1":
                tracker = 300
                tracker2 = 900
                enemy_speed = 1.5
                enemy_mode = "1"
            elif spec_mode == "2":
                tracker = 1200
                tracker2 = 0
                enemy_speed = 2
                enemy_mode = "2"
            elif spec_mode != "1" and spec_mode != "2":
                spec_mode = False
    while track_distance is False and (enemy_mode == "1" or enemy_mode == "2" or game_mode == "3"):
        track_distance = input("Enemy Vision Distance: 300(1), 600(2), 900(3), or 1200(4)? ")
        if track_distance == "1":
            tracker, tracker2 = 300, 900
        elif track_distance == "2":
            tracker, tracker2 = 600, 600
        elif track_distance == "3":
            tracker, tracker2 = 900, 300
        elif track_distance == "4":
            tracker, tracker2 = 1200, 0
        else:
            track_distance = False

    if game_mode != "1" and game_mode != "2" and game_mode != "3":
        game_mode = False
while player1mode is False and game_mode != "3":
    player1mode = input("Player 1 Mode: Control(1) or Constant(2)? ")
    if player1mode != "1" and player1mode != "2":
        player1mode = False
while turns is False and enemy_mode != "4":
    turns = input("Turns: Yes(1) or No(2)? ")
    if turns != "1" and turns != "2":
        turns = False

print("\n\n")

paddle_img = r"Images/PongPaddle.png"
ball_img = r"Images/PongBall.png"
bg_img = r"Images/PongBG.jpg"

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)
pygame.init()
screen = pygame.display.set_mode((1200, 600), 0, 32)
pygame.display.set_caption("Pong")
background = pygame.image.load(bg_img).convert()
char = pygame.image.load(paddle_img).convert_alpha()
enemy = pygame.image.load(paddle_img).convert_alpha()
ball = pygame.image.load(ball_img).convert_alpha()
pygame.mouse.set_visible(False)
pygame.display.set_icon(ball)
ball_speed = 1
x, y = 1190, 260
move_y1 = 0
move_y2 = 0
ex, ey = 0, 260
bx, by = 595, 275
bmx, bmy = randrange(-1, 1), randrange(-10, 10) / 10
if bmx == 0:
    bmx = 1
    p_turn = True
else:
    p_turn = False
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
        if event.type == KEYDOWN and game_mode != "3":
            if event.key == K_UP:
                move_y1 = -1.5
            if event.key == K_DOWN:
                move_y1 = +1.5
        if event.type == KEYDOWN and game_mode != "3":
            if event.key == K_q and game_mode == "2":
                move_y2 = -1.5
            if event.key == K_a and game_mode == "2":
                move_y2 = +1.5

        if event.type == KEYUP:
            if (event.key == K_UP or event.key == K_DOWN) and player1mode == "1":
                move_y1 = 0
            if (event.key == K_q or event.key == K_a) and player2mode == "1":
                move_y2 = 0

    if y <= 20:
        move_y1 = 0
        y = 21
    if y >= 541:
        move_y1 = 0
        y = 540
    if (turns == "1" and p_turn) or turns != "1":
        y += move_y1

    bx += bmx
    by += bmy

    if bx + 10 > x > bx - 10 and by + 10 > y > by - 40:
        p_turn = False
        bmx += .1
        bmx *= -1
        if bmy > 0:
            bmy = randrange(1, 16) / 10 - bmx - 1
        elif bmy < 0:
            bmy = randrange(-15, 0) / 10 + bmx + 1
        score1 += 1
    if by < 20 or by > 570:
        bmy *= -1
    if game_mode == "1" or game_mode == "3":
        if enemy_mode == "1" or enemy_mode == "2":
            if (turns == "1" and not p_turn) or turns != "1":
                if ey + 15 < by and bx < tracker and ey < 539:
                    ey += enemy_speed
                if ey + 15 > by and bx < tracker and ey > 21:
                    ey -= enemy_speed
        elif enemy_mode == "3":
            if ey + 15 < by and ey < 539:
                ey = by - 15
            if ey + 15 > by and ey > 21:
                ey = by - 15
        elif enemy_mode == "4":
            ey = y
    if game_mode == "3":
        if spec_mode == "1" or spec_mode == "2":
            if (turns == "1" and p_turn) or turns != "1":
                if y + 15 < by and bx + 10 > tracker2 and y < 539:
                    y += enemy_speed
                if y + 15 > by and bx + 10 > tracker2 and y > 21:
                    y -= enemy_speed
    elif game_mode == "2":
        if (turns == "1" and not p_turn) or turns != "1":
            ey += move_y2
            if ey > 539:
                ey = 539
            if ey < 21:
                ey = 21
    if bx + 10 > ex > bx - 10 and by + 10 > ey > by - 40:
        p_turn = True
        bmx *= -1
        bmx += .1
        if bmy > 0:
            bmy = randrange(1, 16) / 10 + bmx - 1
        elif bmy < 0:
            bmy = randrange(-15, 0) / 10 - bmx + 1
        score2 += 1
    if bx > 1190 and (by + 10 < y or by > y + 40):
        if game_mode == "1":
            if enemy_mode != "4":
                print("You lose! Your score was", score1)
            elif enemy_mode == "4":
                print("You lose! Your score was", score1 + score2)
        elif game_mode == "2" or game_mode == "3":
            print("Player 2 wins!\nPlayer 1 score:  ", score1, "\nPlayer 2 score:  ", score2)
        pygame.quit()
        sys.exit()
    if bx < 0 and (by + 10 < ey or by > ey + 40):
        if game_mode == "1":
            if enemy_mode != "4":
                print("You win! Your score was", score1)
            elif enemy_mode == "4":
                print("You lose! Your score was", score1 + score2)
        elif game_mode == "2" or game_mode == "3":
            print("Player 1 wins!\nPlayer 1 score:  ", score1, "\nPlayer 2 score:  ", score2)
        pygame.quit()
        sys.exit()

    screen.blit(background, (0, 0))
    screen.blit(char, (x, y))
    screen.blit(enemy, (ex, ey))
    screen.blit(ball, (bx, by))
    pygame.display.update()
    if first:
        pygame.time.wait(1000)
        first = False
