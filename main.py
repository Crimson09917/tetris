# Patrick Russell
# 14/06/2022
# Tetris

import pygame
from pygame.locals import *
import sys
from os import system

from piece import Piece
from board import Board
from border import Border


def checkPiece(piece):
    global board
    global movePace
    global spaceTriggered
    if board.checkCollision(piece):
        board.placePiece(piece)
        print("ALERT")
        piece.__init__(window, board, 40, False, [200, 40], walls)
        spaceTriggered = False
        movePace = 300


system('cls')

pygame.init()

dimension = 40
windowWidth = 800
windowHeight = 880
movePace = 300
spaceTriggered = False

window = pygame.display.set_mode((windowWidth, windowHeight))

board = Board(dimension)
border = Border(window, 40)
walls = [border.lWall, border.tWall, border.rWall, border.bWall]

controlledPiece = Piece(window, board, 40, False, [200, 40], walls)
controlledPiece.placePiece()


mainLoop = True
timer = 0
while mainLoop:
    pygame.time.delay(1)
    timer += 1

    window.fill((0, 0, 0))
    board.display(window)
    border.display()
    controlledPiece.placePiece()

    checkPiece(controlledPiece)

    if timer % movePace == 0:
        controlledPiece.move("DOWN")

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainLoop = False
            if event.key == pygame.K_r:
                controlledPiece.rotate()
            if event.key == K_DOWN:
                controlledPiece.move("DOWN")
            if event.key == K_LEFT:
                controlledPiece.move("LEFT")
            if event.key == K_RIGHT:
                controlledPiece.move("RIGHT")
            if event.key == K_SPACE:
                if not spaceTriggered:
                    print("Toggle space ON")
                    spaceTriggered = True
                    movePace = 1
                elif spaceTriggered:
                    print("Toggle space OFF")
                    spaceTriggered = False
                    movePace = 300

    pygame.display.update()

print(board.score)
pygame.quit()
print("You scored", board.score)
sys.exit()
