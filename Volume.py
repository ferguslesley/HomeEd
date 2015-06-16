def volume(W,D,H):
    volume = (W*D*H)
    return volume

def safe_input(prompt):
    no_answer = True
    number = 0
    while no_answer:
        answer = input(prompt)
        try:
            number = int(answer)
            no_answer = False
        except ValueError:
            continue
    return number


print("The volume of a 3*3*3 CUBE is:", volume(3, 3, 3))

print("The volume of a 3*6*3 CUBOID is:", volume(3, 6, 3))

print("The volume of a 9*9*9 CUBE is:", volume(9, 9, 9))

print("The volume of a 3*3*1 SQUARE is:", volume(3, 3, 1))


print("Enter A WIDTH")
W = safe_input("> ")

print("Ender A DEPTH")
D = safe_input("> ") 

print("Enter A HEIGHT")
H = safe_input("> ")

print("The volume of your shape is:", volume(W, D, H))
print("The volume of your cube/cuboid({0},{1},{2}) is: {3}".format(W, D, H, volume(W, D, H)))
