#This is an experiment for the Memory Game

import pygame, sys
from pygame.locals import *
import time
from random import random, shuffle

##########################################################
# Game constants

DEBUG = False
if __debug__:
    DEBUG = True

SCREENW = 400
SCREENH = 400

MARGINX = SCREENW / 20
MARGINTOP = SCREENH / 20
MARGINBOTTOM = MARGINTOP * 2
if DEBUG:
    ROWS = 4
    COLS = 4
else:
    ROWS = 8
    COLS = 8
assert (ROWS * COLS) % 2 == 0, 'must have an even number of cells!'
MAXSCORE = ROWS * COLS / 2

CELLW = (SCREENW - MARGINX * 2) / COLS
CELLH = (SCREENH - MARGINTOP - MARGINBOTTOM) / ROWS

#            R    G    B
WHITE    = (255, 255, 255)
BLACK    = (  0,   0,   0)
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 165,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
BGCOLOR = BOXCOLOR
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

def Debug(text):
    if DEBUG:
        print text

Debug("DEBUG MODE")

#################################################
# drawcell - draw the cell and fill it with a number
#     row
#     column
#     content - tuple of: (shape, colour)

def drawcell(row, column, content):
    # draw the cell
    rect = cellrect(row, column)
    pygame.draw.rect(DISPLAYSURF, WHITE, rect)

    # ... and fill it!
    shape = content[0]
    colour = content[1]
    drawIcon(shape, colour, rect)
    

#################################################
def drawcellempty(row, column, content):
    # draw the cell
    rect = cellrect(row, column)
    pygame.draw.rect(DISPLAYSURF, WHITE, rect)

################################################# 

def highlight_cell(row, column):
    rect = cellrect(row, column)
    rect = rect.inflate(-2, -3)  # .move(1, 1)
    pygame.draw.rect(DISPLAYSURF, RED, rect, 3)
    


#################################################
# cellrect - calculate the Rect for the cell

def cellrect(row, column):
    x = MARGINX + (CELLW * column)
    y = MARGINTOP + (CELLH * row)
    return Rect(x , y, CELLW - 1, CELLH - 1)

#################################################
# find_cell(x, y) - work out which grid cell the x and y is in
# returns row, column

def find_cell(x, y):
    column = (x - MARGINX) / CELLW
    row = (y - MARGINTOP) / CELLH
    return row, column
    
#################################################  
# draws shapes
#              shape - constants at beginning
#              color - constants at beginning
#              rect  - Rect of drawing area
 
def drawIcon(shape, color, rect):
    quarterx = rect.width * 0.25
    quartery = rect.height * 0.25
    halfx = rect.width * 0.5
    halfy = rect.height * 0.5
    half = int(min(halfx, halfy))
    quarter = int(min(quarterx, quartery))

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
    # build a list of all shape/colour combinations
    shapecolours = []
    for shape in ALLSHAPES:
        for colour in ALLCOLOURS:
            shapecolours.append((shape, colour, False))

    # get the right amount of shapes in a random order
    shuffle(shapecolours) # one of each in random order
    numshapes = int(ROWS * COLS / 2) # half of the shapes
    shapes = shapecolours[:numshapes] * 2 # get doubled
    shuffle(shapes) # and randomised again

    # build the grid
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

def guessed(cell):
    if cell[2] == True:
        return True
    else:
        return False

#################################################

def draw_text(text, x, y, size):
    font = pygame.font.Font('freesansbold.ttf', size)
    rendered = font.render(text, True, WHITE)
    displayRect = rendered.get_rect()
    displayRect.center = (x, y)
    DISPLAYSURF.blit(rendered, displayRect)


#################################################

def end_game():
    area = Rect(0, 0, SCREENW, SCREENH)
    pygame.draw.rect(DISPLAYSURF, BLACK, area)
    statusmessage = 'Score = {}  Misses = {}  Time = {}:{}:{}'.format(score, guesses, int(hours), int(minutes), int(seconds))
    draw_text(statusmessage, SCREENW / 2, SCREENH / 2, MARGINBOTTOM * 2/5)
    pygame.display.update()  
    

#################################################


pygame.init()


DISPLAYSURF = pygame.display.set_mode((SCREENW, SCREENH))
pygame.display.set_caption('Memory Game')

grid = build_grid(ROWS, COLS)

for row in range(ROWS):
    for column in range(COLS):
        drawcell(row, column, grid[row][column])
        pygame.display.update()
time.sleep(1)
for row in range(ROWS):
    for column in range(COLS):
        drawcellempty(row,column, grid[row][column])
        pygame.display.update()



oldx, oldy = -1, -1
oldrow, oldcol = -1, -1
firstclick = True    
score = 0
guesses = 0
elapsed_time = 0
start_time = 0
the_clocks_running = False
finished = False

# run the game loop
while True:
    if score >= MAXSCORE:
        finished = True
        the_clocks_running = False
        end_game()
    elif the_clocks_running:
        elapsed_time = time.time() - start_time
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if finished:
            pass

        elif event.type == MOUSEBUTTONUP:
            if not the_clocks_running:
                Debug("start the clock")
                start_time = time.time()
                the_clocks_running = True
            mousex, mousey = event.pos
            row, column = find_cell(mousex, mousey)
            if row < ROWS and column < COLS and row >= 0 and column >=0: # on the grid ...
                cell = grid[row][column]
                
                if guessed(cell):
                    pass
                elif oldrow == row and oldcol == column:
                    pass
    
                elif firstclick:
                    # draw cell contents
                    drawcell(row, column, grid[row][column])
                    highlight_cell(row, column)
                    # and remember which cell
                    oldx, oldy = mousex, mousey
                    oldrow, oldcol = row, column
                    oldcell = cell
                    firstclick = False
                else:
                    drawcell(row, column, cell)
                    highlight_cell(row, column)
                    if oldcell == cell:
                        score = score + 1
                        # they match
                        # so mark them as Found
                        grid[row][column] = (cell[0], cell[1], True) 
                        grid[oldrow][oldcol] = (oldcell[0], oldcell[1], True)
                        # and clear highlights
                        pygame.display.update()
                        pygame.time.wait(1000)
                        drawcell(oldrow,oldcol, oldcell)
                        drawcell(row,column, cell)
                    else:
                        # different - so reset
                        pygame.display.update()
                        pygame.time.wait(1000)
                        drawcellempty(oldrow,oldcol, oldcell)
                        drawcellempty(row,column, cell)
                        oldrow = -1
                        oldcol = -1
                        guesses = guesses + 1
                    firstclick = True


    if not finished:
        #Updating Status and Refreshing Screen
        statusrect = Rect(0, SCREENH - MARGINBOTTOM, SCREENW, MARGINBOTTOM)
        pygame.draw.rect(DISPLAYSURF, BLACK, statusrect)
        hours, rem = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(rem, 60)
        statusmessage = 'Score = {}  Misses = {}  Time = {}:{}:{}'.format(score, guesses, int(hours), int(minutes), int(seconds))
        draw_text(statusmessage, SCREENW / 2, SCREENH - MARGINBOTTOM / 2, MARGINBOTTOM * 2/5)
        pygame.display.update()

