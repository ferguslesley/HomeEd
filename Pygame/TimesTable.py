'''
Created on Mar 15, 2016

@author: fergus
'''

def CalculateTable(number):
    for num in range(1,13,1):
        sumnum = num * number
        if sumnum % 3 == 0 and sumnum % 5 == 0:
            print "BANG!", 
        elif sumnum % 3 == 0:
            print "FIZZ!",
        elif sumnum % 5 == 0:
                print "BUZZ!",   
        else:
            print "{:5d}".format(sumnum),


    print ""

count = 1
while count < 13:
    CalculateTable(count)
    count = count + 1
