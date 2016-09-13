from microbit import *

xpos = 1
maxx = 4
minx = 0
oldposx = 0
oldposy = 0
xstep = 1
ystep = 1
ypos = 0
maxy = 4
miny = 0


for i in range(1, 100):
        display.set_pixel(xpos,ypos,8)
        display.set_pixel(oldposx,oldposy,0)
        
        # move coords by step
        oldposx = xpos
        oldposy = ypos
        xpos += xstep
        ypos += ystep
        #check for edges

        sleep(100)
        
        if xpos >= maxx:
            # (change direction to "bounce")
            xpos = maxx
            xstep = -1
        if xpos <= minx:
            # (change direction to "bounce")
            xstep = minx
            xstep = 1
        if ypos >= maxy:
            ypos = maxy
            ystep = - 1
        if ypos <= miny:
            ypos = miny
            ystep = 1
        print(xpos, xstep)
