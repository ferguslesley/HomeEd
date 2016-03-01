import random

def CtoF(TempC):
    F = TempC * 9 / 5 + 32
    return F

'''
F = C * 9 / 5 + 32
... let's subtract 32
F - 32 = C * 9 / 5 + 32 - 32
... so
F - 32 = C * 9 / 5
... lets multiply by 5
5 * (F - 32) = C * 9 / 5 * 5
... so
5 * (F - 32) = C * 9
... let's divide by 9
5 * (F - 32) / 9 = C * 9 / 9
... so
5 * (F - 32) / 9 = C
'''

def FtoC(TempF):
    C = 5 * (TempF - 32) / 9
    return C

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

print("Do you want to calculate a C (Centigrade) or a F (Farenheit) number?")

CorF = input("> ")

if CorF in ["C","c"]:
    print("Please type a number in Degrees Centigrade")
    TemperatureC = safe_input("> ")
    print(CtoF(TemperatureC))
if CorF in["F","f"]:
    print("Please type a number in Degrees Farenheit")
    TemperatureF = safe_input("> ")
    print(FtoC(TemperatureF))


listofstuff = []
for number in range(100):
    listofstuff.append(random.randint(-40,100))

for num in listofstuff:
    if (abs(CtoF(FtoC(num)) - num) > 0.1):
        print("CtoF(FtoC(%d)) = %d" % (num, CtoF(FtoC(num))))
