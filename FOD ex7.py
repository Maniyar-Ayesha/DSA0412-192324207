import pandas as pd

# Sample data
data = {
    'customer_id': ['C101', 'C102', 'C101', 'C103'],
    'order_date': ['2024-06-01', '2024-06-05', '2024-06-10', '2024-06-12'],
    'product_name': ['Mobile', 'Laptop', 'Mobile', 'Tablet'],
    'order_quantity': [2, 1, 1, 3]
}

# Convert to DataFrame
order_data = pd.DataFrame(data)

# Convert order_date column to datetime
order_data['order_date'] = pd.to_datetime(order_data['order_date'])

# 1. Total number of orders made by each customer
total_orders_per_customer = order_data['customer_id'].value_counts()

# 2. Average order quantity for each product
avg_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()

# 3. Earliest and latest order dates
earliest_date = order_data['order_date'].min()
latest_date = order_data['order_date'].max()

# Display results
print("1. Total Orders per Customer:")
print(total_orders_per_customer)
print("\n2. Average Order Quantity per Product:")
print(avg_quantity_per_product)
print("\n3. Earliest Order Date:", earliest_date)
print("   Latest Order Date:", latest_date)
