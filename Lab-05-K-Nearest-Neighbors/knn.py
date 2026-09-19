# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the k-NN classifier (k=3)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Make predictions on the test data
y_pred = knn.predict(X_test)

# Print accuracy
print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%\n")

# Print correct and wrong predictions
print("=== Correct Predictions ===")
for i in range(len(y_test)):
    if y_test[i] == y_pred[i]:
        print(f"Sample {i}: Predicted = {iris.target_names[y_pred[i]]}, Actual = {iris.target_names[y_test[i]]}")

print("\n=== Wrong Predictions ===")
for i in range(len(y_test)):
    if y_test[i] != y_pred[i]:
        print(f"Sample {i}: Predicted = {iris.target_names[y_pred[i]]}, Actual = {iris.target_names[y_test[i]]}")
