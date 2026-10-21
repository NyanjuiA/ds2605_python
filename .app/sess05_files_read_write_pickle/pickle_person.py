# Python script to get a person's details from the user and then store them in the
# 'person.txt' file in the 'files' folder/directory using the pickle module

# Import the required modules
import pickle
from pathlib import Path
from person import Person


def get_person_details() -> Person:
   """
   Prompt the user for their details and create a Person object.

   Returns:
       Person: An instance of the Person class containing user's
       name, age and binary gender.
   """
   name = input('Please enter your name: \n')
   age = input('Please enter your age: \n')
   gender = input("Please enter your binary gender 'm' for male "
                  "and 'f' for female: \n")

   return Person(name, age, gender)

def save_person(person: Person) -> Path:
   """
   Serialise a Person object and append it to a binary file.

   The file is created if it does not exist. Its parent
   directory must exist before the file can be opened.

   Args:
      person (Person): An instance of the Person object to serialise

   Returns:
      Path (Path): Absolute path to the file containing the object
   """
   file_path = (
      Path(__file__).resolve().parent.parent
      / "files"
      / "person.txt"
   )

   # Ensure the destination directory exists
   file_path.parent.mkdir(parents=True, exist_ok=True)

   # Append the serialised object to the file.
   with file_path.open('ab') as file:
      pickle.dump(person, file)

   return file_path

def main() -> None:
   """Collect the user's details and save the Person object."""
   user = get_person_details()
   file_path = save_person(user)

   print("The 'user' object has been successfully picked to:\n"
         f"{file_path}")

# Start the application
if __name__ == '__main__':
   main()


