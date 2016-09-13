from microbit import *

xpos = 1
maxx = 4
minx = 0
oldpos = 0

display.set_pixel(xpos,2,8)
while True:
    while xpos < maxx:
        display.set_pixel(xpos,2,8)
        display.set_pixel(oldpos,2,0)
        sleep(100)
        oldpos = xpos
        xpos = xpos + 1
    while xpos > minx:
        display.set_pixel(xpos,2,8)
        display.set_pixel(oldpos,2,0)
        sleep(100)
        oldpos = xpos
        xpos = xpos - 1


