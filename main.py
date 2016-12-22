#!/usr/bin/python3
import pygame
from pygame.locals import *
from sys import exit

import numpy as np

import math

class Piece:
    def __init__(self):
        self.loc = np.matrix([[0,0],[0,1],[1,0],[1,1]])

    def update(self):
        for i in range(self.loc.shape[0]):
            self.loc[i,1] = self.loc[i,1]+1
    def moveRight(self):
        for i in range(self.loc.shape[0]):
            self.loc[i,0] = self.loc[i,0]+1
    def moveLeft(self):
        for i in range(self.loc.shape[0]):
            self.loc[i,0] = self.loc[i,0]-1
    def newPiece(self):
        self.loc = np.matrix([[0,0],[0,1],[1,0],[1,1]])


def insertObject(matrix,piece):
    try:
        for x in range(piece.loc.shape[0]):
            matrix[piece.loc[x,0],piece.loc[x,1]] = 1
    except:
        piece.newPiece()

pygame.init()
screen = pygame.display.set_mode((480,640))


black = (0,0,0);
white = (255,255,255);
size = 15
boarder = 3
step = size+boarder
cubeColumns = 10
cubeLines = 15
# matrix = np.matrix(np.ones([cubeColumns,cubeLines]))
matrix = np.matrix(np.zeros([cubeColumns,cubeLines]))
auxMatrix = matrix.copy()
piece = Piece()

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    piece.moveLeft()
                if event.key == pygame.K_RIGHT:
                    piece.moveRight()
        if event.type == QUIT:
            pygame.quit(); exit();


    screen.fill(white);

    # Part of a red circle, arc from 0 to 90 degrees
    # Center is at 100,100, and radius is 50
    insertObject(auxMatrix,piece)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if auxMatrix[i,j] == 1:
                pygame.draw.rect(screen, black, (boarder+i*step,boarder+j*step,size,size), 0)

    piece.update()
    # print(matrix)
    # print(20*'-')
    # print(auxMatrix)
    auxMatrix = matrix.copy()

    pygame.display.update()
    pygame.time.wait(500)





# TO USE LATER WHEN YOU NEED KEY DETECTION
# events = pygame.event.get()
# for event in events:
#     if event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_LEFT:
#             location -= 1
#         if event.key == pygame.K_RIGHT:
#             location += 1
