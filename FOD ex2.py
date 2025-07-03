import numpy as np

# Sample 3x3 matrix: each row = a product, each column = a sale
sales_data = np.array([
    [200, 220, 250],  # Product 1
    [180, 210, 240],  # Product 2
    [160, 190, 230]   # Product 3
])

# Step 1: Calculate the average price of all products sold
average_price = np.mean(sales_data)

# Output
print("Average price of all products sold:", average_price)
