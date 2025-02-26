"""
Write a function to calculate total sales

Create a function sum_sales(sales_list) that takes a list of sales and returns the total.
"""

def sum_sales(sales_list):
    return sum(sales_list)

today_sales = [2500, 1500, 500, 1200]
total_sum = sum_sales(today_sales)
print(f"Total Sales Today: €{total_sum}")