import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_csv("customer_data.csv")

# Drop customer_id if present
if 'customer_id' in df.columns:
    df = df.drop('customer_id', axis=1)

# Feature scaling
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df)

# Elbow method to determine optimal K
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    sse.append(kmeans.inertia_)

# Plot elbow curve
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), sse, marker='o')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of clusters')
plt.ylabel('SSE (Inertia)')
plt.grid(True)
plt.show()

# Fit KMeans with chosen K (e.g., 4)
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_features)

# Show sample with cluster labels
print("\n📊 Sample Data with Cluster Labels:")
print(df.head())

# Visualize clusters (using first two features for simplicity)
sns.pairplot(df, hue='Cluster', palette='Set1', diag_kind='kde')
plt.suptitle("Customer Segments", y=1.02)
plt.show()
