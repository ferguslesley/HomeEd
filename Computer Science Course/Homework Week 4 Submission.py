import time

time.sleep(2)
print("Question 2, 1, a")
time.sleep(2)

count = 0
maxcount = 300
step = 3

while count <= maxcount:
    print(count)
    count = count + step

time.sleep(2)
print("Question 2, 1, b")
time.sleep(2)

count = 0
maxcount = 100
step = 5

while count <= maxcount:
    print(count)
    count = count + step

time.sleep(2)
print("Question 2, 1, c")
time.sleep(2)

count = 100
maxcount = 0
step = -1

while count >= maxcount:
    print(count)
    count = count + step
