# Python GUI App to accept an email address from the user and validate it using regex

# Import the required modules
import re
import tkinter as tk
from tkinter import messagebox, END

# Function to validate the email address
def validate_email():
   """
   Validate the email address entered by the user.

   Retrieves the email address from the entry field, removes any
   leading or trailing whitespace and checks whether it matches
   the specified regular expression.

   Displays an appropriate message box if the email address is
   valid, invalid or missing.
   """
   email = entry_email.get().strip()
   if email == "": # same as if not email
      tk.messagebox.showerror("Missing Email Address",
                              "Please enter an email address to be validated.")
      return
   pattern = r"^[a-zA-Z\d.+_-]+@[a-zA-Z\d._]+\.[a-zA-Z]+$"

   if re.match(pattern, email):
      tk.messagebox.showinfo("Valid Email",
                             f"Email address '{email}' is valid.")
   else:
      tk.messagebox.showerror("Invalid Email Address",
                              f"Sorry, email address '{email}' is invalid.")

# Function to clear the email entry/control widget
def clear_text():
   """
   Clear the email address entry field.

   Removes all text from the email address entry widget and
   returns keyboard focus to the entry field.
   """
   entry_email.delete(0, END)
   entry_email.focus()

# Set up the GUI
root = tk.Tk()
root.title("Validate Email Address")

# Label(s)
label_email= tk.Label(root, text="Email Address:")
label_email.grid(row=0, column=0, padx=10, pady=5)

# Entry Field(s)
entry_email= tk.Entry(root)
entry_email.grid(row=0, column=1, padx=10, pady=5)

# Button(s)
button_validate = tk.Button(root, text="Validate Email", command=validate_email)
button_validate.grid(row=1, column=0, padx=10, pady=5)

button_clear = tk.Button(root, text="Clear Email", command=clear_text)
button_clear.grid(row=1, column=1, padx=10, pady=5)

# Run the application
root.mainloop()