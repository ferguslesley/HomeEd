Morning = True
Lazy = True

'''
if Lazy == True and Morning == True:
    print("5 More minutes!")
elif Morning == True and Lazy == False:
    print("Wake Up!!" * 50)
else:
    print("Go back to sleep!")

'''

user_age = int(input("Enter your age pls fam > "))

if user_age < 13:
    print("Hi, child!")
elif user_age < 18:
    print("'Sup, bro?")
elif user_age < 30:
    print("Hello, adult!")
elif user_age < 60:
    print("With age comes wisdom!")
elif user_age > 60:
    print("Dang these new fangled computer devices!")
