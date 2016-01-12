import turtle
t = turtle.Pen()
t.clear()
t.reset()


def draw_poly(sides):
    angle =  360 / sides
    length =  500 / sides
    count = 0
    t.speed(sides * 2)
    while count < sides:
        t.forward(length)
        t.right(angle)
        count = count + 1

while True:
    print("Enter The Number of Sides!, Type 0 to Exit!")
    sides = int(input("> "))
    t.clear()
    t.reset()
    t.down()

    if sides == 0:
        break

    draw_poly(sides)
    t.up()
    t.left(90)
    t.forward(50)
    

