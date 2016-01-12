# The Super Intense Awesome Guessing Game Of Intense Awesomeness
print("\n" * 200)
print("Think of a number and I will guess it!")


biggest = int(input("Enter the largest number in the range! > "))
smallest = int(input("Enter the smallest number in the range! > "))

while True:
    guess = int((biggest + smallest) / 2)
    print("I guess...", guess, "!")
    hint = input("please type 'high', 'low' or 'correct' > ")
    if hint in ["high", "High"]:
        biggest = guess - 1
    if hint in ["low", "Low"]:
        smallest = guess + 1
    if hint in ["correct", "Correct"]:
        print("Haha! I knew I would win!")
        break
    if biggest == smallest:
        guess = biggest
        print("Oh!! I know it! It's", guess, "!")
        break
    
        
    
    
