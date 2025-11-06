import math

try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError("Cannot find square of a negative number.")
    print("Square root is:", math.sqrt(num))
except ValueError as a:
    print(a)