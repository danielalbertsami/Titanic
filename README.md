# Titanic Problem
## Preface
Given a CSV file of data containing varied pieces of information about passengers on the Titanic,
we seek a machine-learning-based approach to reliably predict whether or not
a given passenger survived.
## Intuition-Based Analysis
The following data points are given, with notes on how each might be used in a predictive model.
* **Passenger ID**: A unique identifier used as a dictionary key in this model.
* **Survived**: A binary result value used to determine whether the model is accurate.
* **Passenger Class**: Possible values are 1, 2, and 3 for first, second, and third class. In this model,
this will be interpreted as a categorical variable.
* **Name**: Names will be ignored in this model as intuition indicates there isn't a strong enough correlation for the data points to be useful.
* **Sex**: Assigned as a binary categorical variable.
* **Age**: Assigned as a linear variable.
* **Siblings and Spouses**: Assigned as a linear variable.
* **Parents and Children**: Assigned as a linear variable.
* **Ticket Number**: Ignored in this model and marked as arbitrary.
* **Passenger Fare**: Potentially considered as a linear variable, may be removed later if not found to be useful.
* **Cabin Number**: Many gaps in this data point exist, and while it might be useful to indicate position on the ship, will be ignored to avoid clouding results.
* **Port of Embarkation**: Used as a ternary categorical variable that may be ultimately ignored depending on model performance.
## Implementation
**TODO**