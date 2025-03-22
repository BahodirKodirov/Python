Homework Assignment 1: Analyzing Sales Data

You are given a dataset containing sales data for an e-commerce website. The dataset (task\sales_data.csv) has the following columns:

Date: Date of the sale.
Product: Name of the product sold.
Category: Category to which the product belongs.
Quantity: Number of units sold.
Price: Price per unit.
Tasks:

Group the data by the Category column and calculate the following aggregate statistics for each category:
Total quantity sold.
Average price per unit.
Maximum quantity sold in a single transaction.
Identify the top-selling product in each category based on the total quantity sold.
Find the date on which the highest total sales (quantity * price) occurred.
Homework Assignment 2: Examining Customer Orders

You have a dataset (task\customer_orders.csv) containing information about customer orders. The dataset has the following columns:

OrderID: Unique identifier for each order.
CustomerID: Unique identifier for each customer.
Product: Name of the product ordered.
Quantity: Number of units ordered.
Price: Price per unit.
Tasks:

Group the data by CustomerID and filter out customers who have made less than 20 orders.
Identify customers who have ordered products with an average price per unit greater than $120.
Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.
Homework Assignment 3: Population Salary Analysis

"task\population.db" sqlite database has population table.
"task\population salary analysis.xlsx" file defines Salary Band categories.
Read the data from population table and calculate following measures:
Percentage of population for each salary category;
Average salary in each salary category;
Median salary in each salary category;
Number of population in each salary category;
Calculate the same measures in each State
Note: Use SQL only to select data from database. All the other calculations should be done in python.


import pandas as pd

# Load the sales data
sales_data = pd.read_csv('task\\sales_data.csv')

# Group the data by 'Category'
category_group = sales_data.groupby('Category')

# Calculate aggregate statistics
category_stats = category_group.agg(
    total_quantity_sold=('Quantity', 'sum'),
    average_price_per_unit=('Price', 'mean'),
    max_quantity_sold=('Quantity', 'max')
)

print("Category Statistics:")
print(category_stats)

# Find the top-selling product in each category based on the total quantity sold
top_selling_products = sales_data.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
top_selling_products = top_selling_products.loc[top_selling_products.groupby('Category')['Quantity'].idxmax()]

print("\nTop-Selling Products by Category:")
print(top_selling_products)

# Find the date with the highest total sales (quantity * price)
sales_data['Total_sales'] = sales_data['Quantity'] * sales_data['Price']
highest_sales_date = sales_data.groupby('Date')['Total_sales'].sum().idxmax()

print("\nDate with Highest Total Sales:")
print(highest_sales_date)

                  # Load the customer orders data
customer_orders = pd.read_csv('task\\customer_orders.csv')

# Group the data by 'CustomerID'
customer_group = customer_orders.groupby('CustomerID')

# Filter customers who have made less than 20 orders
customers_with_20_or_more_orders = customer_group.filter(lambda x: len(x) >= 20)

print("Customers with 20 or more orders:")
print(customers_with_20_or_more_orders)

# Identify customers who have ordered products with an average price per unit greater than $120
avg_price_per_customer = customer_group['Price'].mean()
customers_high_avg_price = avg_price_per_customer[avg_price_per_customer > 120]

print("\nCustomers who have ordered products with an average price > $120:")
print(customers_high_avg_price)

# Find total quantity and total price for each product ordered
product_stats = customer_orders.groupby('Product').agg(
    total_quantity_ordered=('Quantity', 'sum'),
    total_price_ordered=('Price', 'sum')
)

# Filter out products that have a total quantity less than 5 units
product_stats_filtered = product_stats[product_stats['total_quantity_ordered'] >= 5]

print("\nProducts with total quantity >= 5 units:")
print(product_stats_filtered)


import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('task\\population.db')

# SQL query to get data from the population table
query = """
SELECT * FROM population;
"""
# Load data into a DataFrame
population_df = pd.read_sql_query(query, conn)

# Load salary band categories from the Excel file
salary_bands = pd.read_excel('task\\population salary analysis.xlsx')

# Merge the population data with salary band categories
population_df = population_df.merge(salary_bands, on='Salary Band', how='left')

# Calculate percentage of population for each salary category
salary_category_counts = population_df['Salary Band'].value_counts()
total_population = len(population_df)
salary_category_percentage = (salary_category_counts / total_population) * 100

# Calculate average salary in each salary category
average_salary_by_category = population_df.groupby('Salary Band')['Salary'].mean()

# Calculate median salary in each salary category
median_salary_by_category = population_df.groupby('Salary Band')['Salary'].median()

# Calculate the number of population in each salary category
population_by_category = population_df['Salary Band'].value_counts()

# Calculate the same measures by State
salary_category_percentage_by_state = population_df.groupby('State')['Salary Band'].value_counts(normalize=True) * 100
average_salary_by_state = population_df.groupby('State')['Salary'].mean()
median_salary_by_state = population_df.groupby('State')['Salary'].median()
population_by_state = population_df['State'].value_counts()

# Display results
print("Salary Category Percentage:")
print(salary_category_percentage)

print("\nAverage Salary by Category:")
print(average_salary_by_category)

print("\nMedian Salary by Category:")
print(median_salary_by_category)

print("\nPopulation by Salary Category:")
print(population_by_category)

print("\nSalary Category Percentage by State:")
print(salary_category_percentage_by_state)

print("\nAverage Salary by State:")
print(average_salary_by_state)

print("\nMedian Salary by State:")
print(median_salary_by_state)

print("\nPopulation by State:")
print(population_by_state)

# Close the database connection
conn.close()

