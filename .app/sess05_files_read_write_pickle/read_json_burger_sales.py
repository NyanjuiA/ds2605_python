# Python script/file to demonstrate how to read and display a JSON file's data/contents

# Import the required modules
import json

# Open the 'burger_sales.json' file in read mose and display its contents
with open('../files/burger_sales.json',"r") as json_file:
   burger_sales = json.load(json_file)
   # Use a for loop to display the sales in the files
   for sale in burger_sales:
      print(f"{sale}")