#Author: Ryan Su
x = int(input("Give me a number:"))
y = x

while y > 0:
    if x % y == 0:
        print(y)
    y -= 1
