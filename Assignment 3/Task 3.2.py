#using the math module for calculations
#sin(x, /)- Return the sine of x (measured in radians).
#log(...)- Return the logarithm of x to the given base.
#sqrt(x, /)-Return the square root of x.
#to check these i have used
# help(sin)
# help(log)
# help(sqrt)

from math import sin, log, sqrt
num = int(input("Enter a number: "))
square_root = sqrt(num)
Logarithm = log(num)
Sine = sin(num)
print(f"Square root:{square_root}")
print(f"Logarithm: {Logarithm}")
print(f"Sine: {Sine}")

