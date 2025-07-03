from sklearn.datasets import load_breast_cancer, load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import pandas as pd

# Load a sample dataset
print("Available datasets: 'iris', 'breast_cancer'")
dataset_choice = input("Enter dataset name: ").strip().lower()

if dataset_choice == 'iris':
    data = load_iris(as_frame=True)
elif dataset_choice == 'breast_cancer':
    data = load_breast_cancer(as_frame=True)
else:
    print("Invalid dataset name. Exiting.")
    exit()

df = data.frame
print("\nAvailable columns:")
print(df.columns.tolist())

# Ask user for feature and target variable
features_input = input("\nEnter feature names separated by commas: ")
target_input = input("Enter the target variable name: ")

features = [f.strip() for f in features_input.split(',')]
target = target_input.strip()

# Split the dataset
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)

print("\n📊 Evaluation Metrics:")
print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred, average='weighted'):.4f}")
print(f"Recall:    {recall_score(y_test, y_pred, average='weighted'):.4f}")
print(f"F1-score:  {f1_score(y_test, y_pred, average='weighted'):.4f}")

print("\n📋 Classification Report:")
print(classification_report(y_test, y_pred))
