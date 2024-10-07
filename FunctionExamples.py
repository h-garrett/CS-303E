# File: FunctionExamples.py
# Student: Garrett Howard
# UT EID: ghh425
# Course Name: CS303E
# 
# Date Created: 10/4/2024
# Description of Program: Collection of simple functions.



# adds 3 numbers
def sum3Numbers( x, y, z):
    """Return the sum of three parameters."""
    return x + y + z

# multiplies 3 numbers
def multiply3Numbers( x, y, z):
    """Return the product of three parameters"""
    return (x * y * z)

# adds up to three numbers
def sumUpTo3Numbers(x, y = 0, z = 0):
    """Return the sum of up to three numbers"""
    return x + y + z

# multiplies up to 3 numbers
def multiplyUpTo3Numbers(x=1, y=1, z=1):
    """Return the product of up to three numbers"""
    return (x * y * z)

# prints 2 numbers in order
def printInOrder (x, y):
    if x <= y:
        print (x, y)
    else:
        print (y, x)

# calculates area of a square based on side length
def areaOfSquare( side ):
    """return the area of a square based on its side length"""
    if side < 0:
        print ("Error. Negative Side Length")
    else:
        area = (side ** 2)
        return area

# calculates perimeter of a square based on side length
def perimeterOfSquare( side ):
    """return the perimeter of a square based on its side length"""
    if side < 0:
        print ("Error. Negative Side Length")   
    else:
        perimeter = side  * 4
        return perimeter

import math

# calculates area of a cicle based on radius
def areaOfCircle( radius ):
    """return the area of a circle based on its radius"""
    if radius < 0:
        print ("Error. Radius cannot be negative.")
    else:
        area = math.pi * (radius ** 2)
        return area

# calculates circumference of a circle based on radius
def circumferenceOfCircle( radius ):
    """return the circumference of a circle based on its radius"""
    if radius < 0:
        print ("Error. Radius cannot be negative.")
    else:
        circumference = 2 * math.pi * radius
        return circumference

# determines if two values are both factors of x
def bothFactors( d1, d2, x):
    "return whether d1 and d2 are both factors of x"
    return bool((x % d1 == 0) and (x % d2 == 0))
    
    
# finds the circumference and area of a circle with radius x, and the area and perimeter of a square with side length x.
def squareAndCircle( x ):
    """determine the circumference and area of a circle with radius x, and the area and perimeter of a square with side length x."""
    circleArea = areaOfCircle(x)
    cirumference = circumferenceOfCircle(x)
    perimeter = perimeterOfSquare(x)
    squareArea = areaOfSquare(x) 
    print()
    print("A circle with radius",x,"has:")
    print("Area:",circleArea)
    print("Circumference: ",cirumference)
    print()
    print("A square with side length",x,"has:")
    print("Perimeter:",perimeter)
    print("Area:",squareArea)
    print()

# calculates n factorial
def factorial (n):
    """return n! (factorial)."""
    if n < 1:
        print("Error. Non-positive input")
        return None
    else:
        i = n - 1
        while i > 0:
            n *= i
            i -= 1
        return n

# determines how many digits are in a value (n)
def numberLength(n):
    """return the number of digits that make up a positive value, n."""
    d = 1
    while n >= 10:
        n //= 10
        d += 1
    return d

# adds any amount of positive numbers until 0 is entered
def sumPositiveNumbers():
    """return the sum of any amount of positive numbers."""
    x = float(input("Enter a positive number."))
    sum = 0
    while x != 0:
        if x > 0:
            sum += x
        else: 
            print ("Negative number entered, not included in sum.")
        
        x = float(input("Enter another positive number."))
    
    return sum       











    


    
        

