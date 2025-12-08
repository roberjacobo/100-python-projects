"""
Purpose: Read and display all rows from products.csv as dictionaries.
Uses csv.DictReader to access CSV data by column names.
"""
import csv

# Read CSV file and print each row as a dictionary
with open('products.csv', mode='r') as file:
  csv_reader = csv.DictReader(file)
  for row in csv_reader:
    print(row)

# Alternative: Display specific columns only
"""with open('products.csv', mode='r') as file:
  csv_reader = csv.DictReader(file)
  for row in csv_reader:
    print(f"Producto: {row['name']}, Precio: {row['price']}")"""
