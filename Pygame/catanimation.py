import pygame, sys
from pygame.locals import *

pygame.init()

START_FPS = 30
MAX_FPS = 500
FPS = START_FPS # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'

while True: # the main game loop
    

    keys = pygame.key.get_pressed()
    if not keys[K_LCTRL]:
        FPS = FPS
    else:
        FPS = FPS - 1
    if FPS > MAX_FPS:
        FPS = MAX_FPS

    if not keys[K_LSHIFT]:
        FPS = FPS
    else:
        FPS = FPS + 1
    if FPS > MAX_FPS:
        FPS = MAX_FPS

    if not keys[K_RIGHT]:
        direction = direction
    else:
        direction = 'right'

    if not keys[K_LEFT]:
        direction = direction
    else:
        direction = 'left'

    if not keys[K_UP]:
        direction = direction
    else:
        direction = 'up'

    if not keys[K_DOWN]:
        direction = direction
    else:
        direction = 'down'
    
    


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'
            
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(catImg, (catx, caty))



    pygame.display.update()
    fpsClock.tick(FPS)
