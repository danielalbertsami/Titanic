from pandas import read_csv

dataset = read_csv('data/train.csv')

"""
Dataset is absorbed as follows:
[ID, Survived, Class, Name, Sex, Age, SibSp, ParCh, Ticket #, Fare, Cabin #, Port]
"""

"""
Out of the data used in this model, there are missing values for age and port embarked.
For port embarked, there are only two missing values, so we just drop those rows. 
"""
dataset = dataset.dropna(subset=['Embarked'], how='all')  # drop ports of embarkation that are N/A
print(dataset.describe())

# next, use mean imputation or some sort of regression to impute values for age

# then normalize linear values and figure out how to transform categorical values

# figure out how to make some kind of ensemble method to integrate all of these values
#  into a vector or some kind of binary prediction

# refer to the MOOC for information on how to do the above.

