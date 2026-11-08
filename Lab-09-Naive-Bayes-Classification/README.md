# Lab 09 - Naive Bayes Classification

## Aim
To implement the Gaussian Naive Bayes classification algorithm using the Iris dataset and study the effect of different parameters on classification accuracy.

## Dataset
The Iris dataset from Scikit-learn is used.

- Total samples: 150
- Total features: 4
- Target classes: Setosa, Versicolor, Virginica

## Libraries Used
- Python
- Scikit-learn
- NumPy

## Algorithm
Gaussian Naive Bayes Classifier.

## Experiments Performed

1. Changing random_state to 0, 1 and 125.
2. Changing test_size to 0.3 and 0.4.
3. Building the model using different combinations of two features:
   - Sepal Length and Sepal Width
   - Petal Length and Petal Width
   - Sepal Length and Petal Length
   - Sepal Width and Petal Width
4. Changing stratify from `y` to `None`.

## Results

| Experiment | Modification | Accuracy |
|---|---|---:|
| 1 | Random State = 0 | 96.67% |
| 2 | Random State = 1 | 96.67% |
| 3 | Random State = 125 | 90.00% |
| 4 | Test Size = 0.3 | 91.11% |
| 5 | Test Size = 0.4 | 93.33% |
| 6 | Sepal Length + Sepal Width | 70.00% |
| 7 | Petal Length + Petal Width | 96.67% |
| 8 | Sepal Length + Petal Length | 90.00% |
| 9 | Sepal Width + Petal Width | 90.00% |
| 10 | Stratify = None | 100.00% |

## Conclusion
The Gaussian Naive Bayes classifier was successfully implemented. The experiments demonstrate how changing random state, test size, feature selection and stratification affects classification accuracy.
