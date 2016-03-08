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
pygame.display.set_caption('SUPER TANK MAX')

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
    global lasers, direction
    #lasers.append(dict(x=Tankx, y=Tanky + 50, direction=direction))
    if direction == 'up':
        lasers.append(dict(x=Tankx + 41, y=Tanky, direction=direction))
    elif direction == 'right':
        lasers.append(dict(x=Tankx + 82, y=Tanky + 41, direction=direction))
    elif direction == 'down':
        lasers.append(dict(x=Tankx + 41, y=Tanky + 82, direction=direction))
    elif direction == 'left':
        lasers.append(dict(x=Tankx, y=Tanky + 41, direction=direction))
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
        #lasers[laseridx] = (lasers[laseridx][0] - 20, lasers[laseridx][1])
        if lasers[laseridx]['direction'] == 'up':
            lasers[laseridx]['y'] -= 20
            if lasers[laseridx]['y'] < 0:
                lasers.pop(laseridx)
        elif lasers[laseridx]['direction'] == 'right':
            lasers[laseridx]['x'] += 20
            if lasers[laseridx]['x'] > SCREEN_W:
                lasers.pop(laseridx)
        elif lasers[laseridx]['direction'] == 'down':
            lasers[laseridx]['y'] += 20
            if lasers[laseridx]['y'] > SCREEN_H:
                lasers.pop(laseridx)
        elif lasers[laseridx]['direction'] == 'left':            
            lasers[laseridx]['x'] -=20
            if lasers[laseridx]['x'] < 0:
                lasers.pop(laseridx)
        
        

            
    # draw the screen
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(TankImg, (Tankx, Tanky))
    for laser in lasers:
        if laser['direction'] == 'up':
            pygame.draw.line(DISPLAYSURF, RED, (laser['x'], laser['y']), (laser['x'], laser['y'] - 20), 2)
        elif laser['direction'] == 'right':
            pygame.draw.line(DISPLAYSURF, RED, (laser['x'], laser['y']), (laser['x'] + 20, laser['y']), 2)
        elif laser['direction'] == 'down':
            pygame.draw.line(DISPLAYSURF, RED, (laser['x'], laser['y']), (laser['x'], laser['y'] + 20), 2)
        elif laser['direction'] == 'left':
            pygame.draw.line(DISPLAYSURF, RED, (laser['x'], laser['y']), (laser['x'] - 20, laser['y']), 2)


    pygame.display.update()
    fpsClock.tick(FPS)
