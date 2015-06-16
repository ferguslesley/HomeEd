# Quiz
import signal

def clear():
    for line in range(0,100):
        print("\n")

def ouch(sig, frame):
    print("Hey! That HURT!")
signal.signal(signal.SIGINT, ouch)

score = 0
clear()
print("Welcome, To The Minecraft Quiz! With Your Host, Beep Boop The Robot!")

print("\n\n\n")

print("Now, On To The First Question:")
# Question 1
print("In Peacefull Mode, Do You Starve?")
answer = input("> ")
# Checks answer, adds/takes away score
if answer in ["No", "no"]:
    print("Correct! Congratulations!")
    score = score + 1
else:
    print("Oh Noes! You got it wrong D:")
    score = score - 1

print("\n\n\n")
# Question 2
print("Now, The Next Question:")

print("Which of These Can Kill You?")
print("A: Poison  B: Starving On Normal Mode  C: Falling 23 Blocks")

answer = input("> ")
# Checks answer, adds/takes away score
if answer in ["C", "c"]:
     print("Correct! Congratulations!")
     score = score + 1
else:
    print("Oh Noes! You got it wrong D:")
    score = score - 1

print("\n\n\n")
# Question 3
print("Question 3:")

print("How Many Blocks Do Endermen Have To Fall To Die?")
answer = input("> ")
# Checks answer, adds/takes away score
if int(answer) == 43:
    print("Correct! Congratulations!")
    score = score + 1
else:
    print("Oh Noes! You got it wrong D:")
    score = score - 1

print("\n\n\n")

print("Final Question! Worth 2 Points! Its A Tricky On Though!")

print("How Many Bookshelves Are Needed For A Level 30 Enchantment?")
answer = input("> ")
# Checks answer, adds/takes away score
try:
    if int(answer) == 15:
        print("Correct! Congratulations!")
        score = score + 2
    else:
        print("Oh Noes! You got it wrong D:")
        score = score - 1
except ValueError:
    print("That's not a number!")
    score = score -1


# prints score
if score >= 1:
    print("Great Job! Your Score Is:" ,score)

if score < 1:
    print("Better Luck Next Time! Your Score Is:" , score)
