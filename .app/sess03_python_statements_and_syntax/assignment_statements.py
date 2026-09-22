# Python scripts to demonstrate the various assignment statements

# Basic assignment
num1 = 5
spam = 'Yum'
print(f"The contents of 'num1' and 'spam' variables are: {num1} and {spam}.")

# Tuple assignment (positional)
spam, ham = 'Spam','YUM'
print(f"The contents of 'spam' and 'ham' variables after tuple assignment are: {spam} and {ham}")

# List assignment (positional)
[car, drink] = ["CX-5", 'Milk']
print(f"The contents of the 'car' and 'drink' variables are: {car} and {drink}")

# Sequence assignment for numeric values (used on iterables & strings)
first_num, second_num, third_num, fourth_num = [5, 8, 4, 7]
print(f"The contents of the 'first_num', , 'second_num', 'third_num', and 'fourth_num' variables are: "
      f"{first_num, second_num, third_num, fourth_num} ")
print(f"The contents of the 'first_num', , 'second_num', 'third_num', and 'fourth_num' variables are: "
      f"{first_num}, {second_num}, {third_num}, and {fourth_num}.")

# Sequence assignment for alphanumeric
first_letter, second_letter, third_letter, fourth_letter = "CX-5"
print(f"The contents of the 'first_letter', , 'second_letter', 'third_letter', and 'fourth_letter' variables are: "
      f"{first_letter}, {second_letter}, {third_letter}, and {fourth_letter}.")

# Extended sequence assignment for numeric values (used on iterables & strings)
first_num, second_num, *other_nums, eighth_num = [5, 8, 4, 7, 12, 3, 9, 2]
print(f"The contents of the 'first_num', , 'second_num', 'other_nums', and 'eighth_num' variables are: "
      f"{first_num, second_num, third_num, eighth_num} ")
print(f"The contents of the 'first_num', , 'second_num', 'other_nums', and 'eighth_num' variables are: "
      f"{first_num}, {second_num}, {third_num}, and {eighth_num}.")

# Sequence assignment for alphanumeric
first_letter, second_letter, *other_letters, eighth_letter = "Meatball"
print(f"The contents of the 'first_letter', , 'second_letter', '*other_letters', and 'eighth_letter' variables are: "
      f"\n{first_letter}, {second_letter}, {other_letters}, and {eighth_letter}.")

# Multiple target assignment
print("fThe contents of 'first_num', 'second_num', and 'third_num' variables before multiple "
      f"target assignment are: {first_num}, {second_num}, and {third_num}.")
first_num = second_num = third_num = 8
print("fThe contents of 'first_num', 'second_num', and 'third_num' variables before multiple "
      f"target assignment are: {first_num}, {second_num}, and {third_num}.")

# Augmented assignment
second_num += 2 # same as second_num = second_num + 2
print(f"After incrementing/adding 'second_num' by 2 using augmented assignment, we get:{second_num}")
