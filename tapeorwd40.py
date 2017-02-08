#Ultimate Answer To All Problems!

def clear():
    for line in range(0,100):
        print("\n")

clear()

#Title
print("Welcome to the ULTIMATE ANSWER TO ALL PROBLEMS")
print("\n\n\n")

#Question
print("Does It Move?")
answer1 = input("> ")
if answer1 in ["y", "Y", "Yes", "yes"]:
    it_moves = True
else:
    it_moves = False

#Question2
print("Should It?")
answer2 = input("> ")
if answer2 in ["y", "Y", "Yes", "yes"]:
    it_should = True
else:
    it_should = False

if (it_moves):
    if (it_should):
        print("No Problem!")
    else:
        print("Duct Tape")
else:
    if (it_should):
        print("WD40")
    else:
        print("No Problem!")
