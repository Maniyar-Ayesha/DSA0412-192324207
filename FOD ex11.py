import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend

import matplotlib.pyplot as plt

# Sample data
days = list(range(1, 31))
sales = [50, 45, 60, 70, 90, 85, 75, 100, 110, 95,
         80, 65, 60, 70, 100, 120, 130, 125, 110, 105,
         115, 120, 140, 135, 125, 110, 90, 95, 100, 105]

# Line plot
plt.figure(figsize=(10, 5))
plt.plot(days, sales, marker='o', color='blue')
plt.title('Line Plot of Sales')
plt.xlabel('Day')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('line_plot.png')

# Scatter plot
plt.figure(figsize=(10, 5))
plt.scatter(days, sales, color='green')
plt.title('Scatter Plot of Sales')
plt.xlabel('Day')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('scatter_plot.png')

# Bar plot
plt.figure(figsize=(12, 6))
plt.bar(days, sales, color='orange')
plt.title('Bar Plot of Sales')
plt.xlabel('Day')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('bar_plot.png')
