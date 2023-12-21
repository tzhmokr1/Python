"""Exercise 1:
1.)
Write code that takes an integer number and prints True if:
- The number is greater than 10 or less than 0
Else: print False

2.)
Write code that takes two floats (x, y) and computes:
- x^2 + x*y + y^2
"""

# exercise1
number = 11

if number < 0 or number > 10:
    print(True)
else:
    print(False)


# exercise2
x = 3.0
y = 2.0

print(x * x + x * y + y * y)
