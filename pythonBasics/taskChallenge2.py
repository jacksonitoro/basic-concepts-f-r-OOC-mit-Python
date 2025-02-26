"""
Use a dictionary to store sales per department
sales_data = {"Electronics": 1500, "Books": 800, "Toys": 1200}
Print the sales for "Books".
Add "Groceries": 2000 to the dictionary.
"""
sales_data = {"Electronics": 1500, "Books": 800, "Toys": 1200}

#To print the sales for Book
print("Sales for Books €",sales_data["Books"])

#To ADD "Groceries" with sales of 2000 to the sales_data dictionary
sales_data["Groceries"] = 2000

#Print the updated dictionary
print("Updated Sales Date", sales_data)
