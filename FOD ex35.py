import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv('customer_transactions.csv')

# Select features
X = df[['total_spent', 'visit_frequency']]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow method to find optimal k
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot the elbow curve
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()

# Choose optimal k (e.g., from elbow curve we assume k=3)
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df['Segment'] = kmeans.fit_predict(X_scaled)

# Analyze the segments
print("\n📊 Segment Summary:")
print(df.groupby('Segment')[['total_spent', 'visit_frequency']].mean())

# Visualize the clusters
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='total_spent', y='visit_frequency', hue='Segment', palette='Set2', s=100)
plt.title('Customer Segmentation based on Spending Patterns')
plt.xlabel('Total Amount Spent')
plt.ylabel('Visit Frequency')
plt.grid(True)
plt.show()
