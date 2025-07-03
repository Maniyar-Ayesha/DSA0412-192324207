import numpy as np

# Example sales data for 4 quarters
sales_data = np.array([15000, 18000, 21000, 25000])  # Replace with actual data

# Total sales for the year
total_sales = np.sum(sales_data)

# Percentage increase from Q1 to Q4
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print(f"Total Sales for the Year: ₹{total_sales}")
print(f"Percentage Increase from Q1 to Q4: {percentage_increase:.2f}%")
