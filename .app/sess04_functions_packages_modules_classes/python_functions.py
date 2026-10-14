# This script/file demonstrates defining and calling/invoking user
# defined functions in Python

# Define a function to display a greeting message when called/invoked
def greeting(): # Does not take any parameters
   print(f"Hello from 'greeting()' function!")

# Call the 'greeting()' function
greeting()

# Define a function that accepts a parameter (user's name) and greets the user
def greet_user(username: str) -> None: # Add type hinting for username and function's return type
   print(f"Hello {username} from Python functions!")

# Prompt the user for their name
name = input("Please enter your name: \n")

# Call the 'greet_user()' function and pass the user's name as a parameter
greet_user(name)

# Define a function that accepts two numbers and a '+' ( -> default) or 'x' operator
# to add or multiply them respectively
def add_or_multiply(first_num: int, second_num: int, operation: str = '+') -> int:
   """
   This function adds or multiplies two numbers depending on the operation specified.

   :param first_num(int): The first number to be used in the calculation
   :param second_num(int): The second number to be used in the calculation
   :param operation(str,optional): The operation to be performed on the numbers(operands). Defaults to '+'.
   :return int: The sum or product of the operation

   :raises
      None

   Examples:
      >>> add_or_multiply(1, 2)
      3
      >>> add_or_multiply(2, 2, operation='*')
      4
      >>> add_or_multiply(8,5,operation='x')
      40
      >>> add_or_multiply(2,2,operation='/')
      Invalid operation!\nPlease use "+" or "x"
   """
   if operation == '+':
      return first_num + second_num
   elif operation == '*' or operation == 'x':
      return first_num * second_num
   else:
      print("Invalid operation!\nPlease use '+' or 'x'")
      return # User gave us an invalid operator, we stop further processing/execution

# Invoke the 'add_or_multiply()' function
print(f"The sum of 3 and 5 is {add_or_multiply(3, 5)}")
print("The product of %d and %d is %d" % (3, 5, add_or_multiply(3, 5,'*')))

# Display the documentation string of the 'add_or_multiply()' function
print(f"The documentation string of the 'add_or_multiply' function is:\n'{add_or_multiply.__doc__}'")

# Anonymous function(s)
# An anonymous/lambda function is a way to write small compact functions quickly. They are often
# used when you need a simple function for a short period and don't want to write a full function
# using the 'def' keyword

plus_five = lambda num: num + 5 # use lambda to add 5 to a number
print(f"The sum of 7 and 5 using a lambda function is: {plus_five(7)}")

# The same functionality above using a normal function
def add_five(num):
   return num + 5 # define a function to add 5 to the number/value passed in

# Call/invoke the 'add_five()' function
print(f"The sum of 2 and 5 using a normal function is: {add_five(2)}")

# Anonymous/lambda function to get the difference between 2 numbers
difference = lambda num1, num2: num1 - num2

# Sample usage of the 'difference' lambda
print(f"The difference of 3 and 5 using a lambda is: {difference(3,5)}")

# Function with variable parameters
# Define a function that accepts a varying number of parameters
def get_sum(*values):
   # sum = 0
   # for value in values:
   #    sum += value
   # return sum
   try:
      return sum(values) # Succint code that does the same thing as the 4 lines above
   except TypeError:
      print("All values provided must be numbers/numeric values.")
      return None

# Create a list of numbers
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
print(f"The sum of the first ten numbers is: {get_sum(*num_list)}")
nums_with_decimals = [4.5,1.2, 2.0]
print(f"The sum of 4.5,1.2, and 2.0 is: {get_sum(*nums_with_decimals)}")
mixed_nums = [2, 5, '7']
print(f"The sum of 2, 5, and '7' is: {get_sum(*mixed_nums)}")

print("Function program ends...")

