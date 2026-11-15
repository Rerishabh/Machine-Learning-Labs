# Lab 10 - Support Vector Machine (SVM)

## Aim
To implement Support Vector Machine classification using different kernels and perform hyperparameter tuning to identify the best model.

## Dataset
Breast Cancer Wisconsin Dataset from Scikit-learn.

- Total samples: 569
- Number of features: 30
- Target classes: Malignant and Benign

## Libraries Used
- Python
- Scikit-learn
- NumPy

## Algorithms and Techniques
- Support Vector Machine (SVM)
- Linear Kernel
- RBF (Radial Basis Function) Kernel
- Feature Scaling using StandardScaler
- Hyperparameter Tuning

## Experiments Performed

1. Implemented the basic Polynomial SVM classifier using the Iris dataset.
2. Changed the kernel to Linear.
3. Changed the kernel to RBF.
4. Tested C values: 0.01, 1, 10, 100.
5. Tested Gamma values: 0.01, 1, 10, 100.
6. Evaluated 16 combinations for each kernel, making 32 combinations in total.
7. Selected the best-performing model and evaluated it using the Breast Cancer dataset.

## Best Results

| Parameter | Value |
|---|---|
| Best Kernel | Linear |
| C | 1 |
| Gamma | 0.01 |
| Accuracy | 98.25% |

The RBF kernel also achieved 98.25% accuracy with C = 10 and Gamma = 0.01.

## Confusion Matrix

```text
[[62  2]
 [ 1 106]]
```

## Conclusion

SVM classification was successfully implemented using Linear and RBF kernels. Different combinations of C and Gamma were tested using a for loop. The best accuracy obtained was 98.25% using the Breast Cancer dataset.
