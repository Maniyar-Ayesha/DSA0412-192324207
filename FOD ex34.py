import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# Load dataset
df = pd.read_csv('patients_data.csv')

# Encode categorical variables
le_gender = LabelEncoder()
df['gender'] = le_gender.fit_transform(df['gender'])  # M=1, F=0

# Encode target label
le_response = LabelEncoder()
df['response'] = le_response.fit_transform(df['response'])  # Good=1, Bad=0

# Features and target
features = ['age', 'gender', 'blood_pressure', 'cholesterol']
X = df[features]
y = df['response']

# Normalize features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train KNN classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predict on test data
y_pred = knn.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Output evaluation metrics
print("📊 Model Evaluation Metrics:")
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")
print("\nDetailed Classification Report:\n", classification_report(y_test, y_pred, target_names=['Bad', 'Good']))

# Show test set results
results_df = pd.DataFrame(X_test, columns=features)
results_df['Actual'] = le_response.inverse_transform(y_test)
results_df['Predicted'] = le_response.inverse_transform(y_pred)
print("\n🔍 Predictions on Test Set:\n", results_df.head())
