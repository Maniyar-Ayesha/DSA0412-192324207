import numpy as np

# Sample house_data array: [bedrooms, square_footage, sale_price]
house_data = np.array([
    [3, 1500, 250000],
    [5, 3000, 450000],
    [4, 1800, 300000],
    [6, 3500, 500000],
    [2, 1200, 200000]
])

# Step 1: Filter rows where number of bedrooms > 4
filtered_houses = house_data[house_data[:, 0] > 4]

# Step 2: Extract the sale prices (column index 2)
sale_prices = filtered_houses[:, 2]

# Step 3: Calculate average sale price
average_price = np.mean(sale_prices)

# Output
print("Average sale price of houses with more than 4 bedrooms:", average_price)
