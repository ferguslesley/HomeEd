import pygame, sys
from pygame.locals import *

pygame.init()

START_FPS = 30
MAX_FPS = 500
MIN_FPS = 15
FPS = START_FPS # frames per second setting
fpsClock = pygame.time.Clock()
SCREEN_W = 800
SCREEN_H = 600

# set up the window
DISPLAYSURF = pygame.display.set_mode((SCREEN_W, SCREEN_H), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('mariokart.png')
catx = 10
caty = 10
direction = 'right'

while True: # the main game loop
    

    keys = pygame.key.get_pressed()
    if keys[K_LCTRL]:
        FPS = FPS - 1

    if keys[K_LSHIFT]:
        FPS = FPS + 1

    if keys[K_RIGHT]:

        direction = 'right'

    if keys[K_LEFT]:
        direction = 'left'

    if keys[K_UP]:
        direction = 'up'

    if keys[K_DOWN]:
        direction = 'down'

    if FPS < MIN_FPS:
        FPS = MIN_FPS
    if FPS > MAX_FPS:
        FPS = MAX_FPS
    


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    if direction == 'right':
        catx += 5
        if catx >= SCREEN_W - 120:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty >= SCREEN_H - 80:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx <= 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty <= 10:
            direction = 'right'
            
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(catImg, (catx, caty))



    pygame.display.update()
    fpsClock.tick(FPS)
