import sys

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
#print(("(1):add (2):subtract (3):multiply (4):divide "))
option = int(input("(1):addition (2):subtract (3):multiply (4):divide (5):Exit"))

def addition(a,b):
    x = a + b
    print("The answe is:",x)

def subtract(a,b):
    x = a - b
    print("The answe is:",x)

def multiply(a,b):
    x = a * b
    print("The answe is:",x)

def divide(a,b):
    x = a / b
    print("The answe is:",x)

if option == 1:
    addition(a,b)
elif option == 2:
    subtract(a,b)
elif option == 3:
    multiply(a,b)
elif option == 4:
    divide(a,b)
else:
    sys.exit()
