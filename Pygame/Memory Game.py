#This is an experiment for the Memory Game

import pygame, sys
from pygame.locals import *
import time
from random import random, shuffle

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
#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'd'
SQUARE = 's'
DIAMOND = 'D'
LINES = 'l'
OVAL = 'o'

ALLCOLOURS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLOURS) * len(ALLSHAPES) * 2 >= ROWS * COLS, "Board is too big for the number of shapes/colors defined."

#################################################
# drawcell - draw the cell and fill it with a number
def drawcell(row, column, content):
    # draw the cell
    rect = cellrect(row, column)
    pygame.draw.rect(DISPLAYSURF, WHITE, rect)
    # ... and fill it!
    shape = content[0]
    colour = content[1]
    '''
    cell_text = shape  #"{}".format(content)
    textSurfaceObj = fontObj.render(cell_text, True, BLACK, colour)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = rect.center
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    '''
    drawIcon(shape, colour, rect)
    

#################################################
def drawcellempty(row, column, content):
    # draw the cell
    rect = cellrect(row, column)
    pygame.draw.rect(DISPLAYSURF, WHITE, rect)
    # ... and fill it!
    shape = content[0]
    colour = content[1]
#################################################
# cellrect - calculate the Rect for the cell

def cellrect(row, column):
    x = MARGINX + (CELLW * column)
    y = MARGINY + (CELLH * row)
    return Rect(x , y, CELLW - 1, CELLH - 1)

#################################################
# find_cell(x, y) - work out which grid cell the x and y is in

def find_cell(x, y):
    column = (x - MARGINX) / CELLW
    row = (y - MARGINY) / CELLH
    return row, column
    
#################################################   
def drawIcon(shape, color, rect):
    #quarter = int(BOXSIZE * 0.25) # syntactic sugar
    #half =    int(BOXSIZE * 0.5)  # syntactic sugar
    quarterx = rect.width * 0.25
    quartery = rect.height * 0.25
    halfx = rect.width * 0.5
    halfy = rect.height * 0.5
    half = int(min(halfx, halfy))
    quarter = int(min(quarterx, quartery))

    #left, top = leftTopCoordsOfBox(boxx, boxy) # get pixel coords from board coords
    left = rect.left
    top = rect.top

    BOXSIZE = min(rect.width, rect.height)

    # Draw the shapes
    if shape == DONUT:
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)
        pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top + half), quarter - 5)
    elif shape == SQUARE:
        pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))
    elif shape == DIAMOND:
        pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))
    elif shape == LINES:
        for i in range(0, BOXSIZE, 4):
            pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))
            pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOXSIZE - 1), (left + BOXSIZE - 1, top + i))
    elif shape == OVAL:
        pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, BOXSIZE, half))

#################################################
# build_grid - set up the grid data

def build_grid(rows, cols):
#build a list of all shape/colour combinations
    shapecolours = []
    for shape in ALLSHAPES:
        for colour in ALLCOLOURS:
            shapecolours.append((shape, colour))
    #get the right ammount of shapes in a random order
    shuffle(shapecolours)
    numshapes = int(ROWS * COLS / 2)
    shapes = shapecolours[:numshapes] * 2
    shuffle(shapes)
    #build the grid
    data = []
    for row in range(rows):
        new_row = []
        for column in range(cols):
            new_row.append(shapes.pop())
        data.append(new_row)
    return data

#################################################
# get a random number in a specified range

def random_between(MIN,MAX) :
    a=int(random() * (MAX - MIN + 1)) + MIN
    return a

#################################################


pygame.init()


DISPLAYSURF = pygame.display.set_mode((SCREENW, SCREENH))
pygame.display.set_caption('Memory Game')

fontObj = pygame.font.Font('freesansbold.ttf', 16)

grid = build_grid(ROWS, COLS)

for row in range(ROWS):
    for column in range(COLS):
        drawcell(row, column, grid[row][column])
        pygame.display.update()
time.sleep(0.05)
for row in range(ROWS):
    for column in range(COLS):
        drawcellempty(row,column, grid[row][column])
        pygame.display.update()

        
    

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        if event.type == MOUSEBUTTONUP:
            row, column = find_cell(mousex, mousey)
            drawcell(row, column, grid[row][column])

    pygame.display.update()

