from pandas import read_csv
import re
import math
import collections

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
# print(dataset.describe())

# next, use mean imputation or some sort of regression to impute values for age

# There appears to be a trend when it comes to the honorific used, so let's try and see

for index, row in dataset.iterrows():
    tmp = row.copy()
    fullname = re.split(', ', tmp['Name'])[1]
    dataset['Name'][index] = re.split('. ', fullname)[0]

# this next piece of code isolates honorifics with missing age values. We might be able to guess age based on avg values
# for a particular honorific

# s = set() #  used to figure out what honorifics need ages imputed
avg_ages = collections.defaultdict(list)

# Assembling some data to get average ages for each honorific.
# The first value is the total sum, the second is the count. The third is the average calculated at the end.
avg_ages['Miss'] = [0, 0, 0]
avg_ages['Mr'] = [0, 0, 0]
avg_ages['Mrs'] = [0, 0, 0]
avg_ages['Master'] = [0, 0, 0]
avg_ages['Dr'] = [0, 0, 0]

for index, row in dataset.iterrows():
    if math.isnan(row['Age']):
        pass
        # s.add(row['Name'])
    elif row['Name'] in avg_ages:
        avg_ages[row['Name']][0] += row['Age']
        avg_ages[row['Name']][1] += 1

for honorific in avg_ages:
    # print(honorific)
    avg_ages[honorific][2] = avg_ages[honorific][0] / avg_ages[honorific][1]  # calculate average
    # print(avg_ages[honorific][2])  # print average

# impute average age based on the honorific used
for index, row in dataset.iterrows():
    if math.isnan(row['Age']):
        dataset['Age'][index] = avg_ages[row['Name']][2]

# then normalize linear values and figure out how to transform categorical values

# figure out how to make some kind of ensemble method to integrate all of these values
#  into a vector or some kind of binary prediction

# refer to the MOOC for information on how to do the above.

