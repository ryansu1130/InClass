#Author: Ryan Su
import random

x = int(input("Enter a number:"))

password = []

while x > 0:
    password.append(random.randint(0,9))
    x -= 1

print(tuple(password))
