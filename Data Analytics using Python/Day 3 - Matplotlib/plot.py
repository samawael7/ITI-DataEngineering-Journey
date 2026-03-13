import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [10, 20, 25, 30, 15]

plt.plot(x, y)
plt.title("Quick Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()


fig, ax = plt.subplots()              # fig = whole figure, ax = the plot area
ax.plot(x, y, color='teal', marker='o', linestyle='--')
ax.set_title("Object-Oriented Style")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True)
plt.show()



###############################################################

import matplotlib.pyplot as plt

days = ['Sat', 'Sun', 'Mon', 'Tue']
temps = [28, 32, 25, 30]

plt.plot(days, temps, marker='s', color='orange', linestyle='--', linewidth=2)
plt.title("Weekly Temperatures")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()


########################################################

categories = ['Math', 'Physics', 'Chemistry', 'English']
grades = [88, 75, 92, 80]

plt.bar(categories, grades, 
        color=['skyblue', 'lightgreen', 'salmon', 'lightcoral'],
        edgecolor='black')

plt.title("Average Grades by Subject")
plt.xlabel("Subject")
plt.ylabel("Grade")
plt.ylim(0, 100)       # set y-axis range
plt.show()

plt.barh(categories, grades, color='teal')
plt.title("Horizontal Bar Plot")
plt.xlabel("Grade")
plt.show()


###############################################################

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


###########################################

import numpy as np

np.random.seed(42)
x = np.random.rand(50) * 10
y = np.random.rand(50) * 10 + 5

plt.scatter(x, y,
            color='red',
            s=80,             # marker size
            alpha=0.7,        # transparency
            edgecolors='black')

plt.title("Scatter Plot – Random Points")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()


#########################################

categories = ['Math', 'Physics', 'Chemistry', 'English']
grades = [88, 75, 92, 80]

plt.bar(categories, grades,
        color=['skyblue', 'lightgreen', 'salmon', 'lightcoral'],
        edgecolor='black')

plt.title("Average Grades by Subject")
plt.xlabel("Subject")
plt.ylabel("Grade")
plt.ylim(0, 100)          # set y-axis range
plt.show()


############################################

plt.barh(categories, grades, color='teal')
plt.title("Horizontal Bar Plot")
plt.xlabel("Grade")
plt.show()