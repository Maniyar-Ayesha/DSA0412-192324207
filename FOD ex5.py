import numpy as np

# Example fuel efficiency data in miles per gallon (mpg)
fuel_efficiency = np.array([25, 30, 28, 35, 40])  # Replace with actual data

# Step 1: Calculate average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# Step 2: Calculate percentage improvement between two car models
# Let's say we compare the 2nd model (index 1) and the 5th model (index 4)
model_old = fuel_efficiency[1]  # e.g., 30 mpg
model_new = fuel_efficiency[4]  # e.g., 40 mpg

percentage_improvement = ((model_new - model_old) / model_old) * 100

# Display results
print(f"Average Fuel Efficiency: {average_efficiency:.2f} mpg")
print(f"Percentage Improvement (Model 2 to Model 5): {percentage_improvement:.2f}%")
