import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Sample customer shopping behavior dataset
data = {
    'annual_spending': [500, 1500, 2000, 1000, 3000, 2500, 600, 700, 2600, 4000],
    'visit_frequency': [10, 40, 50, 30, 60, 55, 15, 20, 58, 70]
}

df = pd.DataFrame(data)

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Apply KMeans clustering
k = 3  # Number of customer segments
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
kmeans.fit(X_scaled)

# Cluster centers
print("📌 Cluster Centers (scaled):")
print(kmeans.cluster_centers_)

# User input for a new customer
try:
    spending = float(input("Enter annual spending (in currency units): "))
    visits = int(input("Enter visit frequency (number of purchases per year): "))

    new_customer = np.array([[spending, visits]])
    new_customer_scaled = scaler.transform(new_customer)

    # Predict customer segment
    cluster = kmeans.predict(new_customer_scaled)

    print(f"\n🧾 The new customer belongs to segment: Cluster {cluster[0]}")
except Exception as e:
    print("❌ Error in input:", e)
