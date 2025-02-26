"""
Filter High Sales Days

Given a list [2500, 700, 3400, 1900], print only the sales above 2000.
"""

sales_list = [2500, 700, 3400, 1900]

for sale in sales_list:
    if sale > 2000:
        print(f"Sales: €{sale}")