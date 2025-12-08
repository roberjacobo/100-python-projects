"""
Purpose: Read CSV and display specific columns (name and price).
Shows how to filter and format CSV data for display.
"""
import csv

# Alternative: Read entire rows
"""with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)"""

# Display specific columns with formatted output
with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")