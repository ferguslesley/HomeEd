#This is an experiment for the Memory Game

import pygame, sys
from pygame.locals import *
import time

SCREENW = 400
SCREENH = 300

MARGINX = SCREENW / 20
MARGINY = SCREENH / 20

ROWS = 8
COLS = 8

CELLW = (SCREENW - MARGINX * 2) / COLS
CELLH = (SCREENH - MARGINY * 2) / ROWS

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

#################################################
# drawcell - draw the cell and fill it with a number
def drawcell(row, column, content):
    # draw the cell
    rect = cellrect(row, column)
    pygame.draw.rect(DISPLAYSURF, WHITE, rect)
    # ... and fill it!
    cell_text = "{}".format(content)
    textSurfaceObj = fontObj.render(cell_text, True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = rect.center
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

#################################################
# cellrect - calculate the Rect for the cell

def cellrect(row, column):
    x = MARGINX + (CELLW * column)
    y = MARGINY + (CELLH * row)
    return Rect(x , y, CELLW - 1, CELLH - 1)

#################################################
# build_grid - set up the grid data

def build_grid(rows, cols):
    data = []
    for row in range(rows):
        new_row = []
        for column in range(cols):
            new_row.append(random_between(1,64))
        data.append(new_row)
    return data

#################################################
# get a random number in a specified range
from random import random
def random_between(MIN,MAX) :
    a=int(random() * (MAX - MIN + 1)) + MIN
    return a
#################################################




pygame.init()


DISPLAYSURF = pygame.display.set_mode((SCREENW, SCREENH))
pygame.display.set_caption('Drawing')

fontObj = pygame.font.Font('freesansbold.ttf', 16)

grid = build_grid(ROWS, COLS)

for row in range(ROWS):
    for column in range(COLS):
        drawcell(row, column, grid[row][column])
        # and pause
        pygame.display.update()
        time.sleep(0.05)
    #raw_input("next!")
        
    

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
