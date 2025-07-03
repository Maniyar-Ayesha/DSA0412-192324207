import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend

import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Age': [25, 30, 22, 25, 30, 28, 22, 40, 25, 30],
    'PurchaseAmount': [120, 300, 150, 200, 180, 210, 130, 300, 110, 160]
}

df = pd.DataFrame(data)

# Frequency distribution
age_distribution = df['Age'].value_counts().sort_index()
print("Frequency distribution of customer ages:\n")
print(age_distribution)

# Plot
plt.figure(figsize=(8, 5))
age_distribution.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Frequency Distribution of Customer Ages')
plt.xlabel('Age')
plt.ylabel('Number of Customers')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save plot to file
plt.savefig('customer_age_distribution.png')
print("Plot saved as 'customer_age_distribution.png'")
