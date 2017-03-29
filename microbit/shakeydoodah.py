from microbit import *
import random

six = Image( "90009:"
             "00000:"
             "90009:"
             "00000:"
             "90009" )

five = Image("90009:"
             "00000:"
             "00900:"
             "00000:"
             "90009" )

four = Image("90009:"
             "00000:"
             "00000:"
             "00000:"
             "90009" )

three =Image("00009:"
             "00000:"
             "00900:"
             "00000:"
             "90000" )

two  = Image("00009:"
             "00000:"
             "00000:"
             "00000:"
             "90000" )

one  = Image("00000:"
             "00000:"
             "00900:"
             "00000:"
             "00000" )

dice = (one, two, three, four, five, six)

while True:
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(1000)
        display.show(random.choice(dice))
