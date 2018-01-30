import csv
from collections import defaultdict

data = defaultdict(list)
dataReader = csv.reader(open('data/train.csv', newline=''))

"""
Data will be stored in a dictionary of lists.
Key = Passenger ID
Value = [Survived, Class, Sex, Age, SibSp, ParCh, Fare, Port]
"""

for row in dataReader:
    print('passenger ID: ' + row[0])
    print('Survived: ' + ('yes' if (row[1] == '1') else 'no'))
    print('Passenger Class: ' + row[2])
    print('Sex: ' + ('male' if (row[4] == 'male') else 'female'))
    print('Age: ' + row[5])
    print('Siblings and spouses: ' + row[6])
    print('Parents and children: ' + row[7])
    print('Ticket fare: ' + row[9])
    print('Cabin number: ' + row[10])
    print('Port embarked: ' + row[11])