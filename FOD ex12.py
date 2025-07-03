import matplotlib
matplotlib.use('Agg')  # Use backend that doesn't require GUI (fixes TclError)

import matplotlib.pyplot as plt

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

temperature = [15, 17, 22, 28, 32, 35, 34, 33, 30, 25, 20, 16]  # in °C
rainfall = [45, 60, 80, 120, 200, 250, 300, 280, 180, 100, 60, 50]  # in mm

# -------- Line Plot for Temperature --------
plt.figure(figsize=(10, 5))
plt.plot(months, temperature, marker='o', color='red', linestyle='-')
plt.title('Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_temperature_plot.png")  # Saves plot to a file (no need for GUI)
print("✅ Line plot saved as: monthly_temperature_plot.png")

# -------- Scatter Plot for Rainfall --------
plt.figure(figsize=(10, 5))
plt.scatter(months, rainfall, color='blue', s=100)
plt.title('Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_rainfall_scatter.png")
print("✅ Scatter plot saved as: monthly_rainfall_scatter.png")
