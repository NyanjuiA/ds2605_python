# Python script to demonstrate the various number/numeric types supported by Python

# Get the code to make the Decimal numbers work
from decimal import Decimal, getcontext, ROUND_DOWN
# Get the code to make Fraction numbers work
from fractions import Fraction

# Demonstrate integers (whole numbers, both +ve and -ve)
int_value = 8
print("Integer Demonstration")
print("-" * 32)
print(f"The value of the variable 'int_value' is {int_value}")
print(f"The type of the variable in 'int_value' is {type(int_value)}\n")

# Demonstrate floats/floating-point numbers (numbers with decimal places, both +ve and -ve)
float_value = 3.141592653
print("Floating Point Number Demonstration")
print("-" * 32)
print(f"The value of the variable 'float_value' is {float_value}")
print(f"The type of the variable in 'float_value' is {type(float_value)}\n")

# Demonstrate Decimal (numbers with decimal places and a fixed precision, both +ve and -ve)
# Set the precision for decimal operations
getcontext().prec = 7 # Set the precision. You can set this to a higher number to maintain precision
# for rounding numbers with lots of decimal place e.g. Decimal(345.23456789012345678)
decimal_value = Decimal(8.141592654)
print("Decimal Number Demonstration")
print("-" * 32)
print(f"The original value of the variable 'decimal_value' is {decimal_value}")
# Use ROUND_DOWN to ensure no rounding up takes place
decimal_value = Decimal('1.2345789012345789').quantize(Decimal('0.0001'), rounding=ROUND_DOWN)
print(f"The modified value of 'decimal_value' correct to 4 d.p. is {decimal_value}")
print(f"The type of the variable in 'decimal_value' is {type(decimal_value)}\n")

# Demonstrate complex numbers (numbers with real and imaginary part)
complex_value = 3 + 4j
print("Complex Number Demonstration")
print("-" * 32)
print(f"The value of the variable 'complex_value' is {complex_value}")
print(f"The type of the variable in 'complex_value' is {type(complex_value)}")
print(f"Real part: {complex_value.real}")
print(f"Imaginary part: {complex_value.imag}\n")

# Demonstrate floats/floating-point numbers (numbers with decimal places, both +ve and -ve)
fraction_value = Fraction(7,3)
print("Fraction Number Demonstration")
print("-" * 32)
print(f"The value of the variable 'fraction_value' is {fraction_value}")
print(f"The type of the variable in 'fraction_value' is {type(fraction_value)}\n")

# Demonstrating Boolean (True or False)
true_value = True
false_value = False; n = 5; a = 8 # Declare multiple variable in a single line
print(f"Demonstrating Boolean values")
print('-' * 32)
print(f"The value in the boolean variable 'true_value' is {true_value}")
print(f"The value in the boolean variable 'false_value' is {false_value}")
print(f"The type of the boolean variable 'true_value' is {type(true_value)}")
print('-' * 32)
print(f"Using booleans in arithmetic operations")
print(f"True + True = {true_value + true_value}")
print(f"True + False = {true_value + false_value}")
print(f"False + False = {false_value + false_value}")
print(f"False + n(5) is: {false_value + n}")
print(f"True + a(8) is: {true_value + a}")
print(f"True x a(8) is: {true_value * a}")
print(f"(n < a) x 10 + (n == a) x 20 is: {(n < a) * 10 + (n == a) * 20}")