# File: ConvertUnits.py
# Student: Garrett Howard
# UT EID: ghh425
# Course Name: CS303E
# 
# Date: 9/16/2024
# Description of Program: Converts a number of feet + inches to a variety of English and metric units.

inputFeet = int(input("Enter number of feet: "))
inputInches = int(input("Enter number of inches: "))

inches = ((inputFeet * 12) + (inputInches))
feet = inches/12
yards = feet/3
miles = feet/5280
meters = feet * 0.3048
centimeters = meters * 100
millimeters = centimeters * 10
kilometers = meters/1000

print()
print(inputFeet, "feet and", inputInches, "inches equals:")
print()
print("English Units")
print("  feet:", feet)
print("  inches:", inches)
print("  yards:", yards)
print("  miles:", miles)
print()
print("Metric Units")
print("  meters:", meters)
print("  centimeters:", centimeters)
print("  millimeters:", millimeters)
print("  kilometers", kilometers)
print()
