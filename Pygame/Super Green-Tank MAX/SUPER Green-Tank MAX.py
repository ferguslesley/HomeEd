import pygame, sys
from pygame.locals import *
from pygame import *

from pygame.time import set_timer
from GreenTankConfig import *

pygame.init()


def fire_laser():
    global lasers, direction
    # lasers.append(dict(x=Tankx, y=Tanky + 50, direction=direction))
    if direction == 'up':
        lasers.append(dict(x=Tankx + 41, y=Tanky, direction=direction))
    elif direction == 'right':
        lasers.append(dict(x=Tankx + 82, y=Tanky + 41, direction=direction))
    elif direction == 'down':
        lasers.append(dict(x=Tankx + 41, y=Tanky + 82, direction=direction))
    elif direction == 'left':
        lasers.append(dict(x=Tankx, y=Tanky + 41, direction=direction))


def move_tank():
    global Tankx, Tanky
    # move Tank
    if direction == 'right':
        Tankx += TankSpeed
        if Tankx >= SCREEN_W - 120:
            # direction = 'down'
            Tankx = SCREEN_W - 120
    elif direction == 'down':
        Tanky += TankSpeed
        if Tanky >= SCREEN_H - 80:
            # direction = 'left'
            Tanky = SCREEN_H - 80
    elif direction == 'left':
        Tankx -= TankSpeed
        if Tankx <= 10:
            # direction = 'up'
            Tankx = 10
    elif direction == 'up':
        Tanky -= TankSpeed
        if Tanky <= 10:
            # direction = 'right'
            Tanky = 10


def move_laser():
    # move the laser bolts
    for laseridx in range(len(lasers) - 1, -1, -1):
        # lasers[laseridx] = (lasers[laseridx][0] - 20, lasers[laseridx][1])
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
            lasers[laseridx]['x'] -= 20
            if lasers[laseridx]['x'] < 0:
                lasers.pop(laseridx)


def draw_screen():
    # draw the screen
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(BackroundWorld, (0, 0))
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


while True:  # the main game loop


    keys = pygame.key.get_pressed()
    if keys[K_LCTRL]:
        TankSpeed = MIN_SPEED

    if keys[K_LSHIFT]:
        TankSpeed = MAX_SPEED
        set_timer(USEREVENT, 1000)  # trigger speed reset

    if keys[K_SPACE]:
        if not firing and len(lasers) < MAXLASERS:
            fire_laser()
            firing = True
    else:
        firing = False

    if keys[K_RIGHT]:
        direction = 'right'
        TankImg = TankImgRight
        move_tank()

    elif keys[K_LEFT]:
        direction = 'left'
        TankImg = TankImgLeft
        move_tank()

    elif keys[K_UP]:
        direction = 'up'
        TankImg = TankImgUp
        move_tank()

    elif keys[K_DOWN]:
        direction = 'down'
        TankImg = TankImgDown
        move_tank()

    if FPS < MIN_FPS:
        FPS = MIN_FPS
    if FPS > MAX_FPS:
        FPS = MAX_FPS

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == USEREVENT:
            TankSpeed = NORM_SPEED
            set_timer(USEREVENT, 0)

    move_laser()
    draw_screen()

    pygame.display.update()
    fpsClock.tick(FPS)
