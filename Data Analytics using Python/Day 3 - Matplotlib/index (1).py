import pandas as pd


data = {
    'Name': ['Ahmed', 'Sara', 'Omar', 'Lina', 'Khaled', 'Nour', 'Yara', 'Mohamed', 'Hassan', 'Mona'],
    'Age': [25, 32, 19, 28, 45, 22, 30, 27, 24, 21],
    'Grade': [88, 92, 65, 78, 55, None, 89, 72, 95, 82],
    'Subject': ['Math', 'Physics', 'Math', 'Chemistry', 'Physics', 'English', 'Math', 'Chemistry', 'Physics', 'Math'],
    'City': ['Cairo', 'Alexandria', 'Giza', 'Cairo', 'Mansoura', 'Alexandria', 'Cairo', 'Giza', 'Cairo', 'Alexandria'],
    'Passed': [True, True, False, True, False, True, True, True, True, True]
}

df = pd.DataFrame(data)

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 3, 1, 8, 2, 6]

plt.plot(x, y,
         color='blue',
         marker='o',
         linestyle='-',
         linewidth=2,
         markersize=8)

plt.title("Line Plot Example")
plt.xlabel("Time")
plt.ylabel("Value")
plt.grid(True)
plt.show()
