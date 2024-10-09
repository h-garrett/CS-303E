# File: ComputeTaxes.py
# Student: Garrett Howard
# UT EID: ghh425
# Course Name: CS303E
# 
# Date: 09/23/2024
# Description of Program: Computes ones taxes owed based on taxable income and marital status.

print("Welcome to our friendly tax computing program.")
print("Please follow the directions.")
print()

mStatus = input("Enter your marital status (s or m): ")

if not ((mStatus == "s") or (mStatus == "m")):
    print("Bad marital status entered! Try again later.")
    exit()

elif mStatus == "s":
    shownMStatus = "Single"

elif mStatus == "m":
    shownMStatus = "Married"

tI = float(input("Enter your taxable income: "))
if (tI < 0):
    print("Negative income reported! Try again later.")
    exit()

if (mStatus == "s") and (tI <= 8000):
    taxesOwed = float(tI * 0.1)
if (mStatus == "s") and (8000 < tI <= 32000):
    taxesOwed = float(800 + 0.15 * (tI - 8000))
if (mStatus == "s") and (tI > 32000):
    taxesOwed = float(4400 + (0.25 * (tI - 32000)))

if (mStatus == "m") and (tI <= 16000):
    taxesOwed = float(tI * 0.1)
if (mStatus == "m") and (16000 < tI <= 64000):
    taxesOwed = float(1600 + 0.15 * (tI - 16000))
if (mStatus == "m") and (tI > 64000):
    taxesOwed = float(8800 + (0.25 * (tI - 64000)))

print()
print("Marital Status:",shownMStatus)
print("Taxable Income: $",format(tI, "<0.2f"), sep="")
print("Taxes Owed: $",format(taxesOwed, "<0.2f"), sep="") 
print()