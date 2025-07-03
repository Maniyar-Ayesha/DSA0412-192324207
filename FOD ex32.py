import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv('housing_data.csv')

# Select relevant feature for bivariate analysis (e.g., house_size_sqft)
feature = 'house_size_sqft'
target = 'price'

# Scatter plot for bivariate analysis
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x=feature, y=target)
plt.title(f'Bivariate Analysis: {feature} vs {target}')
plt.xlabel('House Size (sq ft)')
plt.ylabel('House Price')
plt.grid(True)
plt.show()

# Prepare data for modeling
X = df[[feature]]
y = df[target]

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print evaluation metrics
print("\n📈 Model Performance:")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Plot regression line
plt.figure(figsize=(8, 5))
sns.scatterplot(x=X_test[feature], y=y_test, label="Actual")
sns.lineplot(x=X_test[feature], y=y_pred, color='red', label="Predicted")
plt.title("Linear Regression: Actual vs Predicted")
plt.xlabel('House Size (sq ft)')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()
