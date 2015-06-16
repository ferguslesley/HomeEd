import tkinter
# import tkMessageBox

top = tkinter.Tk()

C = tkinter.Canvas(top, bg="white", height=250, width=300)

coord = 0, 0, 300, 250
arc = C.create_line(coord, fill="black", width=5)

C.pack()
top.mainloop()

from tkinter import *

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

w.create_rectangle(50, 20, 150, 80, fill="#476042")
w.create_rectangle(65, 35, 135, 65, fill="yellow")
w.create_line(0, 0, 50, 20, fill="#476042", width=3)
w.create_line(0, 100, 50, 80, fill="#476042", width=3)
w.create_line(150,20, 200, 0, fill="#476042", width=3)
w.create_line(150, 80, 200, 100, fill="#476042", width=3)

mainloop()

from tkinter import *

canvas_width = 200
canvas_height = 100

colours = ("#476042", "yellow")
box=[]

for ratio in ( 0.2, 0.3 ):
   box.append( (canvas_width * ratio,
                canvas_height * ratio,
                canvas_width * (1 - ratio),
                canvas_height * (1 - ratio) ) )

master = Tk()

w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack()

for i in range(2):
   w.create_rectangle(box[i][0], box[i][1],box[i][2],box[i][3], fill=colours[i])

w.create_line(0, 0,                 # origin of canvas
              box[0][0], box[0][1], # coordinates of left upper corner of the box[0]
              fill=colours[0], 
              width=3)
w.create_line(0, canvas_height,     # lower left corner of canvas
              box[0][0], box[0][3], # lower left corner of box[0]
              fill=colours[0], 
              width=3)
w.create_line(box[0][2],box[0][1],  # right upper corner of box[0] 
              canvas_width, 0,      # right upper corner of canvas
              fill=colours[0], 
              width=3)
w.create_line(box[0][2], box[0][3], # lower right corner pf box[0]
              canvas_width, canvas_height, # lower right corner of canvas
              fill=colours[0], width=3)

w.create_text(canvas_width / 2,
              canvas_height / 2,
              text="SURPRISE!")
mainloop()


