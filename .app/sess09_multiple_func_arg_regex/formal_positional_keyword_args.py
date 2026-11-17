# Python script to demonstrate the use of formal, positional and keyword
# arguments in a function.

# Function definition
def profile(name, *args, **kwargs) -> None:
   """
       Display a person's name, hobbies and additional profile information.

       This function demonstrates the use of positional arguments (*args)
       and keyword variable arguments (**kwargs) to accept a flexible
       number of arguments.

       Args:
           name (str): The person's name.
           *args: Variable positional arguments representing the person's
               hobbies or interests.
           **kwargs: Variable keyword arguments containing additional
               profile information, such as gender, age, occupation,
               city, county and country.

       Returns:
           None: The function prints the person's profile information
           to the standard output.

       Example:
           >>> profile(
           ...     "Nyanjui",
           ...     "Reading, Travelling, Cooking, Basketball",
           ...     gender="Male",
           ...     age=16,
           ...     job="IT Lecturer",
           ...     city="Mombasa",
           ...     county="Kiambu",
           ...     country="Kenya"
           ... )
           Name: Nyanjui
           Hobbies:
           - Reading, Travelling, Cooking, Basketball
           Other info.:
           - gender: Male
           - age: 16
           - job: IT Lecturer
           - city: Mombasa
           - county: Kiambu
           - country: Kenya
       """
   print(f"Name: {name}") # Formal argument
   if args: # Positional variable arguments(s)
      print(f"Hobbies: ")
      for hobby in args:
         print(f"- {hobby}")

   if kwargs: # Keyword variable argument(s)
      print(f"Other info. :")
      for key, value in kwargs.items():
         print(f"- {key}: {value}")

# Function call/invocation
profile("Nyanjui", "Reading, Travelling, Cooking, Basketball", gender="Male", age=16,
        job="IT Lecturer", city="Limuru", county="Kiambu", country="Kenya")

# NB:
# 1. Formal arguments :- are defined in the function signature(name in profile function)
# 2. *args  :- collects positional arguments as a tuple
# 3. **kwargs :- collects keyword arguments as a dictionary