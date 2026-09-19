# Lab 05 - K-Nearest Neighbors (KNN)

Implementation of the **K-Nearest Neighbors (KNN)** classification algorithm using the Iris dataset.

## Objective

The objectives of this lab are:

1. Implement KNN without using the KNN library function.
2. Calculate distances using:
   - Euclidean Distance
   - Manhattan Distance
   - Minkowski Distance
3. Allow the user to select the distance measure and value of `K`.
4. Evaluate the model using accuracy.
5. Display correct and wrong predictions.

## Dataset

The **Iris dataset** from Scikit-learn is used.

- Total samples: 150
- Features: 4
- Training samples: 120
- Testing samples: 30
- Classes:
  - Setosa
  - Versicolor
  - Virginica

The dataset is divided into **80% training data and 20% testing data**.

## Technologies Used

- Python
- NumPy
- Scikit-learn
- Google Colab
- Jupyter Notebook

## KNN Implementation

The KNN algorithm is implemented manually without using the `KNeighborsClassifier` function.

The implementation follows these steps:

1. Calculate the distance between the test sample and every training sample.
2. Sort the training samples according to distance.
3. Select the `K` nearest neighbors.
4. Collect their class labels.
5. Apply majority voting.
6. Assign the most frequent class as the prediction.
7. Calculate the model accuracy.

## Distance Measures

### 1. Euclidean Distance

Euclidean distance is calculated as:

```text
d = √(Σ(xᵢ - yᵢ)²)
