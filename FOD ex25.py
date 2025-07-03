from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Step 1: Load the Iris dataset
iris = load_iris()
X = iris.data  # Features: Sepal and Petal measurements
y = iris.target  # Target: Species (0 = setosa, 1 = versicolor, 2 = virginica)
species_names = iris.target_names

# Step 2: Preprocess the data (optional: scaling)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 4: Train the Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Step 5: Get user input
try:
    print("Enter the measurements of the new Iris flower:")
    sepal_length = float(input("Sepal Length (cm): "))
    sepal_width = float(input("Sepal Width (cm): "))
    petal_length = float(input("Petal Length (cm): "))
    petal_width = float(input("Petal Width (cm): "))

    # Step 6: Make prediction
    new_flower = [[sepal_length, sepal_width, petal_length, petal_width]]
    new_flower_scaled = scaler.transform(new_flower)
    prediction = clf.predict(new_flower_scaled)

    # Step 7: Output result
    print(f"\n🌸 Predicted Species: {species_names[prediction[0]]}")
except Exception as e:
    print("❌ Error:", e)
