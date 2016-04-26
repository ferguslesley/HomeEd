'''
Created on Apr 26, 2016

@author: fergus
'''

DEBUG = False
def Debug(text):
    if DEBUG:
        print (text)

KeepEntering = True
numbers = []
print("Please enter at least 2 numbers, one at a time. To stop entering numbers, please type nothing and press enter")

while KeepEntering == True:
    #saves input as number_string
    number_string = raw_input("> ")
    Debug("got: " + number_string)
    #checks if you want to stop entering numbers
    if number_string == "":
        KeepEntering = False
    else:
    #converts number_string in to a number
        int_num = int(number_string)   
    #adds number_string to numbers list
        numbers.append(int_num)
        Debug(numbers.__repr__())



'''
if number1 > number2 and number1 > number3:
    print number1, "is the biggest"
elif number2 > number1 and number2 > number3:
    print number2, "is the biggest"
elif number3 > number1 and number3 > number2:
    print number3, "is the biggest" 
'''
    
numbers.sort()
Debug(numbers.__repr__())
print numbers[0], "is the smallest"
print numbers[-1], "is the biggest"
print float(sum(numbers)) / len(numbers), "is the average"