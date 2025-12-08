"""
Purpose: Load monthly sales data from CSV into a dictionary.
Demonstrates converting CSV rows into a dictionary for easy lookup by month.
"""
import csv

monthly_sales = {}

# Read CSV and build dictionary with month as key and sales as value
with open('monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['Month']
        sales = int(row['Sales'])
        monthly_sales[month] = sales

print(monthly_sales)
