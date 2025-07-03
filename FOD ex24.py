import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Step 1: Simulated dataset (you can replace this with loading your CSV file)
# Sample dataset with 4 symptom features and 0/1 label
data = {
    'fever': [101, 99, 100, 98, 102, 97, 99, 100],
    'cough': [1, 0, 1, 0, 1, 0, 1, 0],
    'fatigue': [1, 1, 0, 0, 1, 0, 1, 0],
    'headache': [1, 0, 1, 0, 1, 0, 1, 0],
    'condition': [1, 0, 1, 0, 1, 0, 1, 0]  # 1 = has condition, 0 = no condition
}

df = pd.DataFrame(data)

# Step 2: Split features and label
X = df.drop('condition', axis=1)
y = df['condition']

# Step 3: Normalize the feature data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Split data for training
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=42)

# Step 5: Input from user
try:
    print("Enter the new patient's symptoms:")
    fever = float(input("Fever (°F): "))
    cough = int(input("Cough (1 for yes, 0 for no): "))
    fatigue = int(input("Fatigue (1 for yes, 0 for no): "))
    headache = int(input("Headache (1 for yes, 0 for no): "))
    k = int(input("Enter the value of k (e.g., 3): "))

    new_patient = [[fever, cough, fatigue, headache]]
    new_patient_scaled = scaler.transform(new_patient)

    # Step 6: Train the model
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    # Step 7: Prediction
    prediction = knn.predict(new_patient_scaled)
    print("\n🔍 Prediction Result:")
    if prediction[0] == 1:
        print("🩺 The patient is likely to have the medical condition.")
    else:
        print("✅ The patient is unlikely to have the medical condition.")

except Exception as e:
    print("❌ Error:", e)
