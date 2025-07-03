import pandas as pd
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('car_data.csv')

# Encode categorical features
label_encoders = {}
for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Features and target
X = df.drop('price', axis=1)
y = df['price']

# Split data (optional - you can skip this if you're training on all data)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train CART model
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# Get input from user
print("\nEnter the following details of the car to predict price:")
input_data = []
for col in X.columns:
    if col in label_encoders:
        categories = list(label_encoders[col].classes_)
        print(f"{col} options: {categories}")
        value = input(f"Enter {col}: ")
        encoded_val = label_encoders[col].transform([value])[0]
        input_data.append(encoded_val)
    else:
        value = float(input(f"Enter {col}: "))
        input_data.append(value)

# Predict price
predicted_price = model.predict([input_data])[0]
print(f"\n💰 Predicted Car Price: ₹{predicted_price:.2f}")

# Display decision path
print("\n📊 Decision Path to Prediction:")
tree_rules = export_text(model, feature_names=list(X.columns))
print(tree_rules)
