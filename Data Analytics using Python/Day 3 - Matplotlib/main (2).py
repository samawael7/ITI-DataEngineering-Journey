import pandas as pd

# Example: students DataFrame
df = pd.read_csv('students.csv', parse_dates=['Score Date'])
print(list(df.groupby('Subject')))
# Average grade per subject
print(df.groupby('Subject')['Grade'].mean())

# Number of students per city
print(df.groupby('City').size())

# Count of passed/failed per subject
print(df.groupby(['Subject', 'Passed']).size())


# Multiple stats for Grade per Subject
print(df.groupby('Subject')['Grade'].agg(['mean', 'median', 'min', 'max', 'count', 'std']))

# Different stats for different columns
print(df.groupby('City').agg({
    'Grade': ['mean', 'max'],
    'Age': 'mean',
    'Student ID': 'count'
})
)


# Count unique values
print(df.groupby('City')['Subject'].nunique())

# First / last row in each group
print(df.groupby('City').first())
print(df.groupby('City').last())

# Transform → same shape as original, group-wise calculation
df['Avg_Grade_in_City'] = df.groupby('City')['Grade'].transform('mean')

# Filter groups (keep only groups that meet condition)
print(df.groupby('City').filter(lambda x: x['Grade'].mean() > 75))



# Top subjects by average grade
print(df.groupby('Subject')['Grade'].mean().sort_values(ascending=False))

# Best student per subject
best_students = df.loc[
    df.groupby('Subject')['Grade'].idxmax(skipna=True).dropna()
]
print(best_students[['Name', 'Subject', 'Grade']])

############################################################

import pandas as pd

# Example: two small DataFrames
df1 = pd.DataFrame({
    'Name': ['Ahmed', 'Sara', 'Omar'],
    'Grade': [88, 92, 65]
})

df2 = pd.DataFrame({
    'Name': ['Lina', 'Khaled'],
    'Grade': [78, 55]
})

# Concat vertically (append rows) – default
pd.concat([df1, df2], ignore_index=True)

# Concat horizontally (side by side)
pd.concat([df1, df2], axis=1)



#####################################

# Two DataFrames with common key
students = pd.DataFrame({
    'Student_ID': [1, 2, 3, 4],
    'Name': ['Ahmed', 'Sara', 'Omar', 'Lina'],
    'Age': [25, 32, 19, 28]
})

scores = pd.DataFrame({
    'Student_ID': [1, 2, 3, 5],
    'Grade': [88, 92, 65, 78],
    'Subject': ['Math', 'Physics', 'Math', 'Chemistry']
})

# Inner join (default) – only matching IDs
print("Inner join")
print(pd.merge(students, scores, on='Student_ID', how='inner'))

# Left join – keep all from left (students), NaN where no match
print("Left join")
print(pd.merge(students, scores, on='Student_ID', how='left'))

# Right join – keep all from right
print("Right join")
print(pd.merge(students, scores, on='Student_ID', how='right'))
# Outer join – keep all from both
print("Outer join")
print(pd.merge(students, scores, on='Student_ID', how='outer'))



# Different column names
#pd.merge(students, scores, left_on='Student_ID', right_on='ID')

# Suffixes when columns have same name
pd.merge(students, scores, on='Student_ID', suffixes=('_student', '_score'))

# Merge on index
print(pd.merge(students.set_index('Student_ID'),
               scores.set_index('Student_ID'), 
               left_index=True, right_index=True))


print(students.set_index('Student_ID').join(scores.set_index('Student_ID'), how='left'))


#######################################################################

# Average grade per subject
pd.pivot_table(df, values='Grade', index='Subject', aggfunc='mean')

# Multiple aggregations
pd.pivot_table(df,
               values='Grade',
               index='Subject',
               aggfunc=['mean', 'max', 'min', 'count'])



# Average grade by Subject (rows) and City (columns)
pd.pivot_table(df,
               values='Grade',
               index='Subject',
               columns='City',
               aggfunc='mean',
               fill_value=0)   # replace NaN with 0

# Add totals (margins)
pd.pivot_table(df,
               values='Grade',
               index='Subject',
               columns='City',
               aggfunc='mean',
               margins=True,          # adds All row & column
               margins_name='Total')