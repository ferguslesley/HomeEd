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
RED   = (255,   0,   0)
TankImgUp = pygame.image.load('TankSpriteForward.png',)
TankImgRight = pygame.image.load('TankSpriteRight.png',)
TankImgDown = pygame.image.load('TankSpriteBackwards.png',)
TankImgLeft = pygame.image.load('TankSpriteLeft.png',)
Tankx = 10
Tanky = 10
direction = 'right'
TankImg = TankImgRight
lasers = []
firing = False
MAXLASERS = 5

def fire_laser():
    global lasers
    lasers.append((Tankx, Tanky + 50))

while True: # the main game loop
    

    keys = pygame.key.get_pressed()
    if keys[K_LCTRL]:
        FPS = FPS - 1

    if keys[K_LSHIFT]:
        FPS = FPS + 1

    if keys[K_SPACE]:
        if not firing and len(lasers) < MAXLASERS:
            fire_laser()
            firing = True
    else:
        firing = False

    if keys[K_RIGHT]:
        direction = 'right'
        TankImg = TankImgRight

    if keys[K_LEFT]:
        direction = 'left'
        TankImg = TankImgLeft

    if keys[K_UP]:
        direction = 'up'
        TankImg = TankImgUp
        
    if keys[K_DOWN]:
        direction = 'down'
        TankImg = TankImgDown
    if FPS < MIN_FPS:
        FPS = MIN_FPS
    if FPS > MAX_FPS:
        FPS = MAX_FPS
    


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    # move Tank
    if direction == 'right':
        Tankx += 5
        if Tankx >= SCREEN_W - 120:
            #direction = 'down'
            Tankx = SCREEN_W - 120
    elif direction == 'down':
        Tanky += 5
        if Tanky >= SCREEN_H - 80:
            #direction = 'left'
            Tanky = SCREEN_H - 80
    elif direction == 'left':
        Tankx -= 5
        if Tankx <= 10:
            #direction = 'up'
            Tankx = 10
    elif direction == 'up':
        Tanky -= 5
        if Tanky <= 10:
            #direction = 'right'
            Tanky = 10

    # move the laser bolts
    for laseridx in range(len(lasers)-1, -1, -1):
        lasers[laseridx] = (lasers[laseridx][0] - 20, lasers[laseridx][1])
        if lasers[laseridx][0] < 0:
            lasers.pop(laseridx)
            
    # draw the screen
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(TankImg, (Tankx, Tanky))
    for laser in lasers:
        pygame.draw.line(DISPLAYSURF, RED, (laser[0], laser[1]), (laser[0] -40, laser[1]), 2)
        


    pygame.display.update()
    fpsClock.tick(FPS)
