import pandas as pd

# Example data
data = {
    'product_name': ['Headphones', 'Mobile', 'Laptop', 'Headphones', 'Mobile'],
    'quantity_sold': [10, 5, 2, 8, 7],
    'sale_date': ['2025-06-01', '2025-06-02', '2025-06-03', '2025-06-10', '2025-06-15']
}

# Create DataFrame
sales_data = pd.DataFrame(data)

# Convert 'sale_date' to datetime
sales_data['sale_date'] = pd.to_datetime(sales_data['sale_date'])

# Filter for sales in the last month (optional if the data is already for one month)
# For example, filter June 2025:
sales_data_filtered = sales_data[
    (sales_data['sale_date'] >= '2025-06-01') &
    (sales_data['sale_date'] <= '2025-06-30')
]

# Group by product and sum quantity sold
product_sales = sales_data_filtered.groupby('product_name')['quantity_sold'].sum()

# Sort and get top 5
top_5_products = product_sales.sort_values(ascending=False).head(5)

# Display results
print("Top 5 Best-Selling Products:")
print(top_5_products)
