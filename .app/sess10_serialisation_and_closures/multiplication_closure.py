# Python script to demonstrate the use of a closure to multiply a parameter with a second value

# Define enclosing function
def multiplier(n):
   def inner(x): # inner function
      return x * n
   return inner

# Create 2 multiplier functions
triple = multiplier(3)
quadruple = multiplier(4)

# Use the above closures to triple 5 and quadruple 8
print(f"5 trippled is:{triple(5)}")
print(f"8 quadrupled is:{quadruple(8)}")