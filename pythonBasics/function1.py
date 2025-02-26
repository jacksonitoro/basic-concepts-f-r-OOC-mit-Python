def calculate_total_sales(sales_list): # Function to calculate daily sales
    return sum(sales_list)

#Test function

daily_sales = [1500, 2000, 1750]
total = calculate_total_sales(daily_sales)

print(f"Total Sales: €{total}")