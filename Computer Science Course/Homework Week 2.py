#Fergus's Homework Week 2
import time

def clear(lines):
    print("\n" * lines)

def evaluatege(numb1, numb2):
    if numb1 <= numb2:
        print("Duh!!")
    else: print("Wrong, sir wrong!")

def evaluatele(numb1, numb2):
    if numb1 >= numb2:
        print("Duh!!")
    else:
        print("Wrong, sir wrong!")
    
def evaluate(numb1, numb2):
    if numb1 > numb2:
        print("Duh!!")
    else: print("Wrong, sir, wrong!")

clear(50)
print("Fergus's Homework. After each section there will be a 5 second wait then it goes onto the next section")
time.sleep(5)
clear(50)
print("1. My favourite joke")
time.sleep(2)
print("A polar bear walked up to a bar and said: 'Could I please have a glass of'")
print("...","\n")
time.sleep(2)
print("...","\n")
time.sleep(2)
print("...","\n")
time.sleep(2)
print("The bartender said: 'Why the big pause?'")
time.sleep(1)
print("The polar bear replied: 'I was born with them!'")
time.sleep(5)


############################################################################
clear(50)
print("2. Division")
time.sleep(2)
print("Please enter 2 numbers and I will divide the first one by the other one")
print("Make sure it's a possible sum or it might break!")
num1 = int(input("First Number > "))
num2 = int(input("Second Number > "))

print(num1 , "Divided by", num2 , "Is", num1 / num2)
time.sleep(5)
############################################################################
clear(50)
print("Time for some simple evaluation. (Questions 3-6)")
time.sleep(2)
print("First Question: is 60 Greater than 70?")
time.sleep(1)
number1 = 60
number2 = 70
evaluate(number1, number2)
time.sleep(1)
print("Hmm. Didn't think so.")
time.sleep(2)

print("Is 8 equal to 9?")
time.sleep(1)
number1 = 8
number2 = 9
if 8 == 9:
    print("WE'RE ALL GOING TO DIE")
else: print("Wrong, sir wrong!")
time.sleep(2)

print("Is 5 not equal to 6?")
time.sleep(1)
if 5 != 6:
    print("Duh!")
else:
    print("AHHHHHH!")
time.sleep(2)

print("Is 10 greater than or equal to 7?")
time.sleep(1)
number1 = 10
number2 = 7
evaluatege(number1, number2)
time.sleep(5)
#############################################################################
clear(50)
print("Now for some sums (Question 7)")
time.sleep(2)
print("6 + 4 / 2 =")
time.sleep(1)
print(6+4/2)
time.sleep(1)
print("Whaaaat?!")
time.sleep(2)
print("4 / 2 + 6 =")
time.sleep(1)
print(4/2+6)
time.sleep(1)
print("Wooooah")
time.sleep(2)
print("Hey.. What does ** Do?")
time.sleep(1)
print("2**2?")
time.sleep(1)
print(2**2)
time.sleep(1)
print("cool!")
time.sleep(2)
print("3**3?")
time.sleep(1)
print(3**3)
time.sleep(1)
print("Hmm")
time.sleep(2)
print("9**9?")
time.sleep(1)
print(9**9)
time.sleep(1)
print("I think I've got it!")
time.sleep(1)
print("'**' is 'To the power of'")
time.sleep(5)
###############################################################################
clear(50)
print("That was Fergus' homework! It took me a while because I wanted to over complicate stuff!")

          



