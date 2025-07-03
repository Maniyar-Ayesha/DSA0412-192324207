import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv('transactions.csv')

# Select relevant features for clustering
X = df[['TotalAmount', 'ItemsPurchased']]

# Standardize the data for better clustering performance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine optimal number of clusters using the Elbow Method
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot Elbow Curve
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--', color='blue')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.grid(True)
plt.tight_layout()
plt.show()

# Fit KMeans with optimal number of clusters (let’s assume K=3 based on Elbow)
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Show sample with cluster labels
print("\n🧾 Sample Data with Cluster Labels:")
print(df.head())

# Visualize Clusters
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='TotalAmount', y='ItemsPurchased', hue='Cluster', palette='Set1', s=100)
plt.title('Customer Segments based on Spending and Purchase Behavior')
plt.xlabel('Total Amount Spent')
plt.ylabel('Items Purchased')
plt.grid(True)
plt.tight_layout()
plt.show()
