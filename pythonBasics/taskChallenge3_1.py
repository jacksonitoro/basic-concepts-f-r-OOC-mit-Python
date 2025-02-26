"""
modified version where the user inputs sales values instead of automatically increasing by 500 each step.
"""

sales = 0

target = 2500

while sales < target:
    print(f"Current Sales: €{sales}")

    increment = float(input("Enter sales amount to add €: ")) # User inputs sales value
    sales += increment # Add user input to sales

print(f"Target reached! Total Sales: €{sales}")