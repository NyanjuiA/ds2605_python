"""
Python tuples
A tuple is a built in data type that represents an ordered collection of elements of the same type.
Tuples allow duplicates and are immutable (their elements cannot be modified).
Tuples are created using () rounded brackets/parentheses or the tuple() function.
Tuples are generally faster that lists as Python doesn't have to worry about growing or shrinking tuples.
Some tuple operations are given below:
"""

# Create a tuple of fruits
fruits = ('blueberry',"orange", 'apple',"banana", "avocado", "guava",'blueberry')

# Display the length i.e. number of fruits in the fruits tuple
print(f"The number of elements/items in the fruit tuple is: {len(fruits)}")

# Get and display the names of the fruits in the tuple
print(f"The fruits in the tuple are:\n{fruits}")

# Get and display the index of an item/element in the tuple
print(f"The index of 'avocado' in the 'fruits' tuple is: {fruits.index('avocado')}")

# Get and display the number of occurrences of 'blueberry'
print(f"'Blueberry' appears {fruits.count('blueberry')} times in the fruits tuple")

# Combine two tuples to create a third one and display its contents
combined_fruits = fruits + ('kiwi','watermelon', 'pineapple', 'dragon fruit')
print(f'Combined fruits tuple contains:\n{combined_fruits}')

# Create a tuple that repeats the fruit tuple twice
fruits_repeated = fruits * 2
print(f"The 'fruits repeated' tuple contains:\n{fruits_repeated}")

# Create a sorted tuple of fruits
sorted_fruits = sorted(fruits)
print(f"The 'sorted_fruits' tuple contains:\n{sorted_fruits}")

# Display the minimum and maximum items in the fruits tuple (least & highest fruits letterwise)
print(f"The least fruit letterwise is: {min(fruits)}."
      f"\nThe highest fruit letterwise is: {max(fruits)}.")

# Declare a tuple of numbers
numbers = (1,2,3,4,5)

# Display the tuple numbers and its sum
print(f"The 'numbers' tuple contains:\n{numbers} and their sum is: {sum(numbers)}")

# Display the first 3 numbers in the 'numbers' tuple using slice
print(f"The first 3 number in the 'numbers' tuple are: {numbers[:3]}") # same as {numbers[0:3]}

# Display only the odd numbers in the 'numbers' tuple using slice
print(f"The odd numbers in the 'numbers' tuple are: {numbers[::2]}") # same as {numbers[0::2]}

# Use the 'any()' function to check if any elemet in the 'numbers' tuple is true
# In Python, non-zero numbers are considered true. Since all the number in the tuple are non-zero,
# 'any(numbers) will return true
any_true = any(numbers)
print(any_true) # This prints 'True' since there are non-zero values/elements in the numbers tuple

# Use the 'all()' function to check if all elements in the 'numbers' tuple are true.
# Since all elements (1,2,3,4,5) are all non-zero, they are all considered true, so
# 'all(numbers)' will also return True
all_true = all(numbers)
print(all_true) # This will print True because all elements in the tuple are non-zero

