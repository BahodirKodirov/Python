Homework 1:

Using chinook.db write pandas code.

Customer Purchases Analysis:
Find the total amount spent by each customer on purchases (considering invoices).
Identify the top 5 customers with the highest total purchase amounts.
Display the customer ID, name, and the total amount spent for the top 5 customers.
Album vs. Individual Track Purchases:
Determine the percentage of customers who prefer to buy individual tracks instead of full albums.
A customer is considered to prefer individual tracks if they have purchased only a subset of tracks from an album.
Provide a summary of the percentage of customers who fall into each category (individual tracks vs. full albums).

import sqlite3
import pandas as pd

# Connect to the Chinook database
conn = sqlite3.connect('task\\chinook.db')

# SQL query to calculate total amount spent by each customer (sum of invoice amounts)
query = """
SELECT c.CustomerId, c.FirstName || ' ' || c.LastName AS CustomerName, SUM(i.Total) AS TotalSpent
FROM customers c
JOIN invoices i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId
ORDER BY TotalSpent DESC;
"""

# Execute the query and load the result into a DataFrame
customer_spending_df = pd.read_sql_query(query, conn)

# Display the top 5 customers based on total amount spent
top_5_customers = customer_spending_df.head(5)

print("Top 5 Customers by Total Amount Spent:")
print(top_5_customers)

# Close the connection
conn.close()


# Connect to the Chinook database again
conn = sqlite3.connect('task\\chinook.db')

# SQL query to get the track purchases by customer and album
query = """
SELECT i.CustomerId, t.AlbumId, COUNT(t.TrackId) AS TracksPurchased, COUNT(DISTINCT t.TrackId) AS DistinctTracksPurchased
FROM invoices i
JOIN invoice_items ii ON i.InvoiceId = ii.InvoiceId
JOIN tracks t ON ii.TrackId = t.TrackId
GROUP BY i.CustomerId, t.AlbumId;
"""

# Execute the query and load the result into a DataFrame
track_purchases_df = pd.read_sql_query(query, conn)

# Now, let's classify customers into 'Full Album' or 'Individual Tracks' based on their purchases
def classify_purchase(row):
    if row['TracksPurchased'] == row['DistinctTracksPurchased']:
        return 'Full Album'
    else:
        return 'Individual Tracks'

# Apply the classification function to each row
track_purchases_df['PurchaseType'] = track_purchases_df.apply(classify_purchase, axis=1)

# Group by CustomerId and count the number of 'Full Album' and 'Individual Tracks' purchases
purchase_type_summary = track_purchases_df.groupby(['CustomerId', 'PurchaseType']).size().unstack(fill_value=0)

# Calculate the percentage of customers who prefer individual tracks vs. full albums
purchase_type_percentage = purchase_type_summary.div(purchase_type_summary.sum(axis=1), axis=0) * 100

# Display the summary
print("Percentage of Customers Who Prefer Individual Tracks vs Full Albums:")
print(purchase_type_percentage)

# Close the connection
conn.close()
