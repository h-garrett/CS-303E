# File: Karatsuba.py
# Student: Garrett Howard
# UT EID: ghh425
# Course Name: CS303E
# 
# Date: 9/8/2024
# Description of Program: Multiplies two 4-digit numbers using the Karatsuba method.

n1 = input("Enter a 4-digit integer: ")
n2 = input("Enter a 4-digit integer: ")

# Breaks down n1 and n2 into n/100 and its remainder.
a, b = int (n1) // 100, int (n1) % 100
c, d = int (n2) // 100, int (n2) % 100

# Multiplying the integer quotients and their remianders
e = a * c
f = b * d

# Qutient of n1 plus its remainder, times the quotient of n2 times its remainder.
g = ((a + b) * (c + d))

# Subtracting the products of the quotients and remainders
h = g - (e + f)

# Multiplying the product of the quotient of n1/100 times the remainder of n2/100 by 10000. (ac * 10000)
i = e * (10 ** 4)

# Multiplying the product of the quotient of n2/100 times the remainder of n1/100 by 100. (bd * 100)
j = h * (10 ** 2)

# Final Product found by adding previously computed values together.
k = i + j + f

# Expected Product calculated "normally"
ans = int(n1) * int(n2)

print ("Computed Product:", k )
print ( "Expected Product:", ans)





      