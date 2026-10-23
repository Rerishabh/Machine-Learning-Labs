# Lab 08: Principal Component Analysis (PCA)

## Objective

To apply Principal Component Analysis (PCA) to the Housing dataset and reduce its dimensionality while preserving at least 90% of the total variance.

## Dataset

* **File:** `Housing.csv`
* **Number of rows:** 545
* **Number of columns:** 13

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib

## Methodology

1. Import the required Python libraries.
2. Load the Housing dataset.
3. Prepare and standardize the features.
4. Apply PCA with a 90% variance-retention threshold.
5. Calculate the explained variance of each principal component.
6. Visualize the reduced dataset using the first two principal components.
7. Export the transformed dataset to a CSV file.

## Results

* **Original dataset:** 545 rows and 13 columns.
* **Principal components retained:** 11.
* **Total variance preserved:** 92.64%.
* **Requirement:** At least 90% variance preserved.

## Output Files

* `Housing_PCA_Result.csv`: Reduced dataset produced by PCA.
* `Lab08_Principal_Component_Analysis.ipynb`: Notebook containing the implementation and outputs.

## Conclusion

PCA reduced the dimensionality of the standardized housing features from 13 to 11 principal components while preserving 92.64% of the total variance, satisfying the 90% variance-retention requirement.
