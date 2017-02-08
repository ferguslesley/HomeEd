## Question 6 Week 3
import time
print("\n" * 50)
print("How many books are on my shelf?")
time.sleep(2)

BooksOnShelf = 32
print(BooksOnShelf)
time.sleep(1)

print("What if I double it? Then double it again? Then again and again 10 times!?")
time.sleep(2)

for count in range(1,10):
    BooksOnShelf = BooksOnShelf * 2
    print(BooksOnShelf)
    time.sleep(0.5)
time.sleep(1)

print("That's a lot of books!")
time.sleep(1)

print("What if I take away 1, then another then another 10 times!?")
time.sleep(2)
for count in range(1,10):
    BooksOnShelf = BooksOnShelf - 1
    print(BooksOnShelf)
    time.sleep(0.5)

time.sleep(2)
print("Neat!")
