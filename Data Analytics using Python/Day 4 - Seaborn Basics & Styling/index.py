# Small sample dataset (copy-paste this first to try all examples)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Name': ['Ahmed', 'Sara', 'Omar', 'Lina', 'Khaled', 'Nour', 'Yara', 'Mohamed', 'Hassan', 'Mona',"essa"],
    'Age': [25, 32, 19, 28, 45, 22, 30, 27, 24, 21,23],
    'Grade': [88, 92, 65, 78, 55, 85, 89, 72, 95, 82,45],
    'Subject': ['Math', 'Physics', 'Math', 'Chemistry', 'Physics', 'English', 'Math', 'Chemistry', 'Physics', 'Math','Math'],
    'City': ['Cairo', 'Alexandria', 'Giza', 'Cairo', 'Mansoura', 'Alexandria', 'Cairo', 'Giza', 'Cairo', 'Alexandria','Alexandria'],
    'Passed': [True, True, False, True, False, True, True, True, True, True, False],
    'Study_Hours': [5.2, 7.8, 3.1, 6.5, 2.8, 5.9, 8.1, 4.3, 9.0, 6.2,3.0]
}

df = pd.DataFrame(data)

