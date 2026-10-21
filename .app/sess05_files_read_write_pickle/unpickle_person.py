# Python script to unpickle the person's details from the 'person.txt' file and display them

# import the required module(s)
import pickle, os # import two or more modules in one line by separating them with commas(,)

# Variable to hold the path to the 'person.txt' file
file_path = os.path.abspath(os.path.join(os.getcwd(),"..","files","person.txt"))

# List taht will hold the 'Person' objects from the 'person.txt' file
persons = []

# Open the 'person.txt' file and read its contents
with open(file_path,'rb') as f:
   while True:
      try:
         unpicked_person = pickle.load(f)
         persons.append(unpicked_person)
      except EOFError:
         break # End of file reached

# Access and display the picked person's details/attributes
if persons:
   print("Details of the persons i the 'person.txt' file")
   print(f"-" * 60)
   for index, person in enumerate(persons, start=1):
      print(f"Person {index}. Name: {person.name}, Age: {person.age}, Gender: {person.gender}")
   print(f"-" * 60)
else:
   print("There are no persons in the 'person.txt' file")

