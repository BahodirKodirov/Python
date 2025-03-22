Homework:
DataFrame 1: Student Grades
import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
Exercise 1: Calculate the average grade for each student.

Exercise 2: Find the student with the highest average grade.

Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.

Exercise 4: Plot a bar chart to visualize the average grades in each subject.

DataFrame 2: Sales Data
import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)
Exercise 1: Calculate the total sales for each product.

Exercise 2: Find the date with the highest total sales.

Exercise 3: Calculate the percentage change in sales for each product from the previous day.

Exercise 4: Plot a line chart to visualize the sales trends for each product over time.

DataFrame 3: Employee Information
import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)
Exercise 1: Calculate the average salary for each department.

Exercise 2: Find the employee with the most experience.

Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe.

Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments.

DataFrame 4: Customer Orders
import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)
Exercise 1: Calculate the total revenue from all orders.

Exercise 2: Find the most ordered product.

Exercise 3: Calculate the average quantity of products ordered.

Exercise 4: Plot a pie chart to visualize the distribution of sales across different products.

import pandas as pd
import matplotlib.pyplot as plt

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

# Exercise 1: Calculate the average grade for each student
df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis=1)

# Exercise 2: Find the student with the highest average grade
highest_avg_student = df1.loc[df1['Average'].idxmax()]

# Exercise 3: Create a new column 'Total' representing the total marks obtained by each student
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)

# Exercise 4: Plot a bar chart to visualize the average grades in each subject
subject_avg = df1[['Math', 'English', 'Science']].mean()
subject_avg.plot(kind='bar', title="Average Grades in Each Subject")
plt.ylabel("Average Grade")
plt.show()

# Print results
print("Highest Average Grade Student:")
print(highest_avg_student)
print("\nUpdated DataFrame with Total and Average:")
print(df1)


import pandas as pd
import matplotlib.pyplot as plt

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

# Exercise 1: Calculate the total sales for each product
total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()

# Exercise 2: Find the date with the highest total sales
df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
highest_sales_date = df2.loc[df2['Total_Sales'].idxmax()]

# Exercise 3: Calculate the percentage change in sales for each product from the previous day
sales_pct_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100

# Exercise 4: Plot a line chart to visualize the sales trends for each product over time
df2.set_index('Date')[['Product_A', 'Product_B', 'Product_C']].plot(kind='line', title="Sales Trends Over Time")
plt.ylabel("Sales")
plt.show()

# Print results
print("Total Sales for Each Product:")
print(total_sales)
print("\nDate with Highest Total Sales:")
print(highest_sales_date)
print("\nSales Percentage Change:")
print(sales_pct_change)


import pandas as pd
import matplotlib.pyplot as plt

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

# Exercise 1: Calculate the average salary for each department
avg_salary_by_dept = df3.groupby('Department')['Salary'].mean()

# Exercise 2: Find the employee with the most experience
most_experienced_employee = df3.loc[df3['Experience (Years)'].idxmax()]

# Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe
min_salary = df3['Salary'].min()
df3['Salary Increase'] = ((df3['Salary'] - min_salary) / min_salary) * 100

# Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments
department_counts = df3['Department'].value_counts()
department_counts.plot(kind='bar', title="Employee Distribution Across Departments")
plt.ylabel("Number of Employees")
plt.show()

# Print results
print("Average Salary by Department:")
print(avg_salary_by_dept)
print("\nEmployee with Most Experience:")
print(most_experienced_employee)
print("\nUpdated DataFrame with Salary Increase:")
print(df3)


import pandas as pd
import matplotlib.pyplot as plt

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

# Exercise 1: Calculate the total revenue from all orders
total_revenue = df4['Total_Price'].sum()

# Exercise 2: Find the most ordered product
most_ordered_product = df4['Product'].mode()[0]

# Exercise 3: Calculate the average quantity of products ordered
avg_quantity_ordered = df4['Quantity'].mean()

# Exercise 4: Plot a pie chart to visualize the distribution of sales across different products
product_sales = df4.groupby('Product')['Total_Price'].sum()
product_sales.plot(kind='pie', autopct='%1.1f%%', title="Sales Distribution by Product")
plt.ylabel("")  # Remove y-axis label
plt.show()

# Print results
print(f"Total Revenue from all Orders: ${total_revenue}")
print(f"Most Ordered Product: {most_ordered_product}")
print(f"Average Quantity of Products Ordered: {avg_quantity_ordered}")

