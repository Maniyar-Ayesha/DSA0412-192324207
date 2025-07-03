import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Sample customer churn dataset
data = {
    'usage_minutes': [200, 450, 300, 150, 400, 500, 100, 120, 350, 250],
    'contract_months': [12, 24, 18, 6, 24, 36, 3, 6, 12, 18],
    'churn': [0, 0, 0, 1, 0, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

# Features and label
X = df[['usage_minutes', 'contract_months']]
y = df['churn']

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# User input for prediction
try:
    usage = float(input("Enter average monthly usage in minutes: "))
    contract = int(input("Enter contract duration in months: "))

    new_customer = np.array([[usage, contract]])
    new_customer_scaled = scaler.transform(new_customer)

    # Predict churn
    prediction = model.predict(new_customer_scaled)
    probability = model.predict_proba(new_customer_scaled)[0][1]

    print(f"\n🧾 Predicted Churn Status: {'Churn' if prediction[0] == 1 else 'Not Churn'}")
    print(f"📊 Churn Probability: {probability * 100:.2f}%")
except Exception as e:
    print("❌ Error in input:", e)
