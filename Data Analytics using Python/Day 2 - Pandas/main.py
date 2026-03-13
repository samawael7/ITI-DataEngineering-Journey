# Regular Python
names = ["Ahmed", "Sara", "Omar"]
ages  = [25, 32, 19]

# Pandas Series
import pandas as pd

s = pd.Series([25, 32, 19], index=["Ahmed", "Sara", "Omar"])
print(s)

# Pandas DataFrame (most common use)
df = pd.DataFrame({
    "name": ["Ahmed", "Sara", "Omar"],
    "age":  [25, 32, 19],
    "city": ["Cairo", "Alex", "Giza"]
})
print(df)


########################################################

import pandas as pd

# 1. From a list (default integer index)
s1 = pd.Series([10, 25, 18, 42])
print(s1)
# 0    10
# 1    25
# 2    18
# 3    42
# dtype: int64

# 2. With custom index
s2 = pd.Series([85, 92, 78, 95],
               index=['Ahmed', 'Sara', 'Omar', 'Lina'])
print(s2)
# Ahmed    85
# Sara     92
# Omar     78
# Lina     95
# dtype: int64

# 3. From a dictionary (keys become index)
scores = {'Math': 88, 'Physics': 75, 'Chemistry': 92, 'English': 80}
s3 = pd.Series(scores)
print(s3)

print(s2.index)      # Index(['Ahmed', 'Sara', 'Omar', 'Lina'], dtype='object')
print(s2.values)     # array([85, 92, 78, 95])
print(s2.dtype)      # int64
print(s2.shape)      # (4,)
print(s2.size)       # 4
print(s2.name)       # None (you can set it: s2.name = 'Midterm Scores')

# By position (like list / NumPy)
print(s2.iloc[0])          # 85
print(s2.iloc[-1])         # 95

# By label (preferred way)
print(s2['Sara'])     # 92
print(s2[['Omar', 'Lina']])   # returns a new Series

# Slicing (works with labels too!)
print(s2['Ahmed':'Omar'])     # includes both ends when using labels


print(s2 + 5)                # adds 5 to every value
print(s2 * 1.1)              # 10% bonus
print(s2 > 85)               # boolean Series
print(s2[s2 > 85])           # filter high scores

##########################################################


import pandas as pd

# 1. From a dictionary (most common & recommended)
df1 = pd.DataFrame({
    'name':    ['Ahmed', 'Sara', 'Omar', 'Lina', 'Khaled'],
    'age':     [25, 32, 19, 28, 45],
    'city':    ['Cairo', 'Alex', 'Giza', 'Cairo', 'Mansoura'],
    'score':   [88.5, 92.0, 78.0, 85.5, 67.0]
})

print(df1)



# 2. From a list of dictionaries
data = [
    {'name': 'Ali', 'age': 22, 'score': 79},
    {'name': 'Nour', 'age': 31, 'score': 91},
    {'name': 'Yara', 'age': 27, 'score': 84}
]
df2 = pd.DataFrame(data)
print("df2",df2)
# 3. From NumPy array + column names
import numpy as np
arr = np.random.randint(50, 100, (5, 3))
df3 = pd.DataFrame(arr, columns=['Math', 'Physics', 'Chemistry'])
print("arr" , arr)
print("df3", df3)
# 4. Empty DataFrame (you can add columns later)
df_empty = pd.DataFrame()
df_empty['id'] = [1, 2, 3]
df_empty['value'] = [10.5, 20.1, 15.3]
print("df_empty",df_empty)


print(df1.shape)         # (5, 4) → rows, columns
print(df1.index)         # RangeIndex(start=0, stop=5, step=1)
print(df1.columns)       # Index(['name', 'age', 'city', 'score'], dtype='object')
print(df1.dtypes)        # data type of each column
print(df1.info())        # very useful summary
print(df1.head(3))       # first 3 rows (default 5)
print(df1.tail(2))       # last 2 rows



# Select one column → returns Series
print(df1['name'])

# Select multiple columns
print(df1[['name', 'age']])

# Select row by position
print(df1.iloc[0])       # first row

###################################################

# Useful parameters
import pandas as pd


df = pd.read_csv('students.csv')


print("the first 5 lines : ")
print(df.head())

print("\ninformation")
print(df.info())

print("\nstatistics")
print(df.describe())

print("\nthe nums of missing values in each column:")
print(df.isna().sum())


import pandas as pd

# ==============================================
#  Reading the students.csv file
# ==============================================
df = pd.read_csv('students.csv',
                 na_values=['', 'NA', 'missing'],     # Treat empty strings and 'missing' as NaN
                 parse_dates=['Score Date'])          # Automatically convert 'Score Date' to datetime

# ==============================================
#  Basic overview of the data
# ==============================================
print("=== Full Data Preview ===")
print(df.to_string(index=False))                    # Print all rows without index column

print("\n=== DataFrame Info ===")
print(df.info())                                    # Shows columns, data types, and missing values count

print("\n=== Descriptive Statistics (numeric columns) ===")
print(df.describe())                                # Summary stats: count, mean, std, min, max, quartiles

# ==============================================
#  Missing values check
# ==============================================
print("\n=== Number of Missing Values per Column ===")
print(df.isna().sum())

# ==============================================
#  Filtering examples
# ==============================================
print("\n=== Students who Passed ===")
print(df[df['Passed'] == True])

print("\n=== Students with Missing Grade ===")
print(df[df['Grade'].isna()])

# ==============================================
#  Simple calculations and aggregations
# ==============================================
print("\n=== Average Grade ===")
print("Average Grade:", df['Grade'].mean())


print("\n=== Grade Statistics (min, max, mean, count) ===")
print(df['Grade'].agg(['min', 'max', 'mean', 'count']))

# ==============================================
#  Bonus: Sorting by grade (descending)
# ==============================================
print("\n=== Top Students by Grade ===")
print(df.sort_values(by='Grade', ascending=False))

# ==============================================
#  Bonus: Count students per city
# ==============================================
print("\n=== Number of Students per City ===")
print(df['City'].value_counts())


#######################################################

import pandas as pd

# Assume we have already loaded:
df = pd.read_csv('students.csv', parse_dates=['Score Date'])

print(df.shape)           # (rows, columns) e.g. (8, 8)
print(df.columns)         # list of column names
print(df.index)           # row labels (usually RangeIndex)

df.head(5)                # first 5 rows (default)
df.tail(3)                # last 3 rows
df.sample(4)              # random 4 rows (good for variety)


df.info()                 # most important!
# Shows: column names, non-null count, dtype, memory usage

df.dtypes                 # data types of each column

df.describe()             # statistics for numeric columns only
df.describe(include='object')   # for categorical/string columns




df.isna().sum()           # number of missing values per column
df.isna().mean() * 100    # percentage of missing values

df.duplicated().sum()     # number of duplicate rows
df.duplicated(subset=['Name', 'Age']).sum()   # check specific columns




df['City'].value_counts()          # frequency of each city
df['Subject'].value_counts(normalize=True)   # proportions

df['Grade'].nunique()               # number of unique values
df['Grade'].unique()                # list of unique values (may be long)



# Single column → returns a Series
df['Name']
df.Name               # dot notation (only if column name is valid identifier)

# Multiple columns → returns a DataFrame
df[['Name', 'Grade', 'City']]

# All columns except one or two
df.drop(columns=['Student ID', 'Score Date'])
#df.drop(columns=['Student ID', 'Score Date'], inplace=True)
# or
df.loc[:, ~df.columns.isin(['Student ID', 'Score Date'])]



# .loc  → label-based (uses index labels and column names)
df.loc[0]                     # row with index label 0
df.loc[2:5]                   # rows 2 to 5 (inclusive!)
df.loc[:, 'Name':'City']      # all rows, columns from Name to City (inclusive)
df.loc[df['Grade'] > 80, ['Name', 'Grade']]   # rows where Grade > 80 + specific columns

# .iloc → position-based (integer position, like NumPy)
df.iloc[0]                    # first row
df.iloc[2:5]                  # rows 2,3,4 (stop is exclusive)
df.iloc[:, 1:4]               # columns 1,2,3 (Name, Age, Grade)
df.iloc[-3:]                  # last 3 rows





# Recommended for single value access (faster & cleaner)
df.at[3, 'Name']           # label-based
df.iat[3, 1]               # position-based (row 3, column 1)

# Avoid this in loops (slow)
df.loc[3]['Name']


# Change single value
df.at[3, 'Grade'] = 82

# Change multiple values with condition
df.loc[df['City'] == 'Cairo', 'City'] = 'Cairo (Capital)'

# Add new column
df['Status'] = df['Grade'].apply(lambda x: 'Pass' if x >= 70 else 'Fail')



# Single condition
high_grade = df['Grade'] >= 80
df[high_grade]                 # same as:
df[df['Grade'] >= 80]

# Show only names and grades of students with high grades
df[df['Grade'] >= 80][['Name', 'Grade']]


# AND → &
df[(df['Grade'] >= 80) & (df['City'] == 'Cairo')]

# OR → |
df[(df['Grade'] >= 90) | (df['Passed'] == True)]

# NOT → ~
df[~(df['City'] == 'Cairo')]          # everyone NOT from Cairo

# Combine all
df[(df['Grade'] > 75) & (df['Passed'] == True) & (df['City'].isin(['Cairo', 'Alexandria']))]



# isin() - multiple exact matches
df[df['Subject'].isin(['Math', 'Physics'])]

# str methods (great for text columns)
df[df['Name'].str.startswith('A')]           # names starting with A
df[df['Name'].str.contains('ar', case=False)] # contains "ar" anywhere (case insensitive)

# between() - range check
df[df['Grade'].between(70, 89)]             # grades from 70 to 89 inclusive

# isnull() / notnull()
df[df['Grade'].isnull()]                    # students with missing grade
df[df['Score Date'].notnull()]


# Best practice: use loc to avoid SettingWithCopyWarning
df.loc[df['Grade'] >= 85, ['Name', 'Grade', 'Subject']]

# Sort the result
df.loc[df['Grade'] >= 85, ['Name', 'Grade']].sort_values('Grade', ascending=False)


df.query("Grade >= 80 and City == 'Cairo'")

min_grade = 75
df.query("Grade > @min_grade and Passed == True")


# BAD – may not change the original DataFrame
df[df['Grade'] < 70]['Grade'] = 70

# Correct ways:
df.loc[df['Grade'] < 70, 'Grade'] = 70

# or
low = df['Grade'] < 70
df.loc[low, 'Grade'] = 70


#########################################################

df.isna()               # returns boolean DataFrame (True where missing)
df.notna()              # opposite

df.isna().sum()         # count of missing values per column
df.isna().sum().sum()   # total missing values in the whole DataFrame

df.isna().mean() * 100  # percentage of missing values per column



# Drop any row with at least one missing value
df.dropna()

# Drop rows only if all values are missing
df.dropna(how='all')

# Drop columns that have missing values
df.dropna(axis=1)

# Drop rows only if certain columns have missing values
df.dropna(subset=['Grade', 'Score Date'])




# Fill with a constant value
df['Grade'].fillna(0)
df.fillna(0)                # fill entire DataFrame

# Fill with mean / median (common for numeric columns)
df['Grade'].fillna(df['Grade'].mean())
df['Grade'].fillna(df['Grade'].median())

# Forward fill / backward fill (good for time series)
df['Score Date'].ffill()    # use previous valid value
df['Score Date'].bfill()    # use next valid value

# Fill with value from another column
df['Age'].fillna(df['Age'].mean())

# Fill different columns with different values
df.fillna({'Grade': 60, 'City': 'Unknown'})



# Linear interpolation (great for numeric sequences)
df['Grade'].interpolate()

# Or on whole DataFrame for numeric columns
#df.interpolate()


# Replace weird placeholders with NaN during loading or after
df.replace(['N/A', '-', '?', 'missing'], pd.NA, inplace=True)



# Typical cleaning sequence
df = df.replace(['', 'NA', 'N/A', '-'], pd.NA)     # standardize missing
df = df.dropna(subset=['Name', 'Student ID'])      # critical columns
df['Grade'] = df['Grade'].fillna(df['Grade'].mean())  # numeric imputation
df['City'] = df['City'].fillna('Unknown')          # categorical imputation



#########################################################################

# Constant value
df['School'] = 'Cairo University'

# From existing columns (vectorized – fastest)
df['Age_in_5_years'] = df['Age'] + 5

# Using calculation
df['Grade_Percent'] = df['Grade'] / 100

# Conditional column (very common)
df['Status'] = df['Grade'].apply(lambda x: 'Pass' if x >= 70 else 'Fail')

# Using np.where (faster than apply for simple cases)
import numpy as np
df['Excellent'] = np.where(df['Grade'] >= 90, 'Yes', 'No')




# Using map / replace
def map_grade(x):
    if 90 <= x <= 100:
        return 'A'
    elif 80 <= x < 90:
        return 'B'
    elif 70 <= x < 80:
        return 'C'
    else:
        return 'F'

df['Grade_Letter'] = df['Grade'].apply(map_grade)
# More practical with pd.cut
df['Grade_Letter'] = pd.cut(df['Grade'],
                            bins=[0, 70, 80, 90, 100],
                            labels=['F', 'C', 'B', 'A'],
                            include_lowest=True)


# Drop one column
df = df.drop(columns='School')

# Drop multiple columns
df.drop(columns=['Age_in_5_years', 'Grade_Percent'], inplace=True)

# Drop columns by condition (e.g. almost empty)
df = df.loc[:, df.notna().mean() > 0.5]   # keep columns with >50% non-missing



# Drop rows with any missing values
df.dropna()

# Drop rows based on condition
df = df[df['Grade'] >= 50]                 # keep only passing grades
df = df[~df['City'].isin(['Unknown', 'N/A'])]  # exclude bad cities

# Drop duplicate rows
df = df.drop_duplicates(subset=['Name', 'Age'], keep='first')



# Add single row
new_row = {'Student ID': 9, 'Name': 'Ziad', 'Age': 24, 'Grade': 87, 'Subject': 'Math',
           'City': 'Cairo', 'Passed': True, 'Score Date': pd.Timestamp('2025-04-01')}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

####################################################################################

# Examples
df['Grade'] = df['Grade'] + 5                  # add bonus to all
df['Age_Next_Year'] = df['Age'] + 1

df['Grade_Percent'] = df['Grade'] / 100
df['Final_Score'] = df['Grade'] * 0.6 + 40     # weighted + base

# Conditional vectorized with np.where
import numpy as np
df['Result'] = np.where(df['Grade'] >= 70, 'Pass', 'Fail')

# Multiple conditions with np.select
conditions = [
    df['Grade'] >= 90,
    df['Grade'] >= 80,
    df['Grade'] >= 70
]
choices = ['A', 'B', 'C']
df['Letter'] = np.select(conditions, choices, default='D')



# Replace values using dictionary
city_map = {'Cairo': 'Cairo Capital', 'Alexandria': 'Alex', 'Giza': 'Giza'}
df['City_Short'] = df['City'].map(city_map)

# Or function
df['Name_Upper'] = df['Name'].map(str.upper)

# With get() – safe for missing keys
df['City_Type'] = df['City'].map({'Cairo': 'Big', 'Alexandria': 'Big'}).fillna('Small')


# Apply function to each value in a column
def grade_category(g):
    if g >= 90: return 'Excellent'
    elif g >= 75: return 'Good'
    elif g >= 60: return 'Average'
    else: return 'Needs Work'

df['Category'] = df['Grade'].apply(grade_category)

# Apply to entire row (axis=1)
def student_summary(row):
    return f"{row['Name']} - {row['Grade']} ({row['Subject']})"

df['Summary'] = df.apply(student_summary, axis=1)


#################################

# Sort by one column (ascending by default)
df.sort_values('Grade')

# Descending order
df.sort_values('Grade', ascending=False)

# Sort by multiple columns
df.sort_values(['City', 'Grade'], ascending=[True, False])
# → first by City A→Z, then inside each city highest Grade first


# Keep the sorted order (inplace or assign)
df = df.sort_values('Grade', ascending=False)

# Show top 5 students
df.sort_values('Grade', ascending=False).head(5)

# Sort by index (useful after filtering/grouping)
df.sort_index()

# Sort by column names (alphabetically)
df.sort_index(axis=1)


# Add a rank column (1 = highest)
df['Rank'] = df['Grade'].rank(ascending=False)

# Handle ties (different methods)
df['Rank_dense']   = df['Grade'].rank(ascending=False, method='dense')    # 1,2,2,4
df['Rank_min']     = df['Grade'].rank(ascending=False, method='min')      # 1,2,2,4
df['Rank_max']     = df['Grade'].rank(ascending=False, method='max')      # 1,3,3,4
df['Rank_average'] = df['Grade'].rank(ascending=False, method='average')  # 1,2.5,2.5,4



# Top 3 highest grades
df.nlargest(3, 'Grade')

# Bottom 3 lowest grades
df.nsmallest(3, 'Grade')

# Top 3 per group (very powerful)
df.nlargest(3, 'Grade').groupby('Subject')


