# Hang-man by Ferg and Dad

import tkinter

window = tkinter.Tk()

canvas = tkinter.Canvas(window, bg="white", height=600, width=800)

arc = canvas.create_line(0, 150, 800, 150, fill="black", width=5)
canvas.pack()

