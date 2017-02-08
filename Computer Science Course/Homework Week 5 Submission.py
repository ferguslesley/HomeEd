Keeprunning = True

while Keeprunning == True:
    user_quit = input("Do you want to quit? (Y, N) > ")
    if user_quit in("Y","y"):
        break
    else:
        print("\n")
    number_1 = int(input("Enter your first number > "))
    symbol = input("Enter the thing you want to do! (/, *, +, -) > ")
    number_2 = int(input("Enter your second number > "))

    if symbol in("/", "*", "+", "-"):
        if symbol== "/":
            answer = number_1 / number_2
        elif symbol == "*":
           answer = number_1 * number_2
        elif symbol == "+":
            answer = number_1 + number_2
        elif symbol == "-":
           answer = number_1 - number_2
        print(answer)
    else:
        print("Operator not valid! Please enter '/' '*' '+' or '-' !")
    
