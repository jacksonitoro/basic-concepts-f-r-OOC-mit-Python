"""
Write a loop that stops when sales reach a target

Start with sales = 0.
Use a while loop to increase sales by 500 each step.
Stop when sales reaches or exceeds 2500.
"""

sales = 0

while sales < 2500: # Runs until sales reaches 2500
    print(f"Sales is {sales}")
    sales += 500 # Increase sales by 500 each step

print("Target reached!")
