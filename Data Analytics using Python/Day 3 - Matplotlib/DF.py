import pandas as pd

# لو عايزين نرجع ننشئ الداتا سريعًا هنا
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

# حساب المتوسط لكل مادة
avg_grade_by_subject = df.groupby('Subject')['Grade'].mean()

plt.figure(figsize=(8, 5))
plt.bar(avg_grade_by_subject.index, avg_grade_by_subject.values, color='skyblue', edgecolor='black')

plt.title('Average Grade by Subject', fontsize=14)
plt.xlabel('Subject', fontsize=12)
plt.ylabel('Average Grade', fontsize=12)
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()


###########################################

city_counts = df['City'].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(city_counts.index, city_counts.values, color='lightcoral', edgecolor='black')

plt.title('Number of Students per City', fontsize=14)
plt.xlabel('City', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()





####################################################################
plt.figure(figsize=(8, 5))

plt.hist(df['Grade'].dropna(), 
         bins=10, 
         color='teal', 
         edgecolor='black', 
         alpha=0.8)

plt.title('Distribution of Grades', fontsize=14)
plt.xlabel('Grade', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

###################################################################

passed_counts = df['Passed'].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(passed_counts, 
        labels=['Passed', 'Failed'], 
        autopct='%1.1f%%', 
        colors=['#66b3ff', '#ff9999'],
        startangle=90,
        shadow=True)

plt.title('Pass/Fail Percentage', fontsize=14)
plt.axis('equal')  # دائرة متساوية
plt.show()