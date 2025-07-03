import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Sample housing dataset
data = {
    'area': [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700],
    'bedrooms': [3, 3, 3, 4, 2, 3, 4, 4, 3, 3],
    'price': [245000, 312000, 279000, 308000, 199000, 219000, 405000, 324000, 319000, 255000]
}

df = pd.DataFrame(data)

# Features and target
X = df[['area', 'bedrooms']]
y = df['price']

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# User input for new house
try:
    area = float(input("Enter the area of the house (in sq ft): "))
    bedrooms = int(input("Enter the number of bedrooms: "))

    new_data = np.array([[area, bedrooms]])
    new_data_scaled = scaler.transform(new_data)

    # Predicting price
    predicted_price = model.predict(new_data_scaled)
    print(f"\n💰 Predicted House Price: ${predicted_price[0]:,.2f}")
except Exception as e:
    print("❌ Error in input:", e)
