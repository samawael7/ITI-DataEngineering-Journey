# Small sample dataset (copy-paste this first to try all examples)
import pandas as pd

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

print("Sample Students DataFrame (first 5 rows):")
print(df.head())


#################

import seaborn as sns
import matplotlib.pyplot as plt

# Scatter plot: Study Hours vs Grade, colored by Passed
sns.scatterplot(data=df, 
                x='Study_Hours', 
                y='Grade', 
                hue='Passed', 
                size='Age', 
                palette='deep',
                sizes=(50, 200))

plt.title("Grade vs Study Hours (Size = Age, Color = Passed)")
plt.xlabel("Study Hours per Week")
plt.ylabel("Grade")
plt.grid(True, alpha=0.5)
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Most common & clean style
sns.set_style("whitegrid")      # adds light grid, white background

# Other popular options
# sns.set_style("darkgrid")     # dark background with grid
# sns.set_style("white")        # clean, no grid
# sns.set_style("dark")         # dark background, no grid
# sns.set_style("ticks")        # small ticks on axes


# Best for presentations / notebooks
sns.set_context("talk", font_scale=1.3)

# Options:
# "paper"    → smallest (default for publications)
# "notebook" → good for Jupyter
# "talk"     → larger fonts for presentations
# "poster"   → largest


# Set once for all plots
sns.set_palette("husl")          # bright, distinct colors

# Popular palettes you’ll use a lot
# "deep"      → strong, professional
# "muted"     → soft, elegant
# "Set2"      → nice for categories
# "viridis"   → sequential gradient (great for heatmaps)
# "coolwarm"  → diverging (good for correlations)


####################################

# Apply the same style & palette from the example
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.2)
sns.set_palette("husl")

# Boxplot: Grade by City, colored by Passed (instead of day/time)
sns.boxplot(data=df, 
            x="City", 
            y="Grade", 
            hue="Passed")

plt.title("Grade Distribution by City (Passed vs Not Passed)")
plt.xlabel("City")
plt.ylabel("Grade")
plt.xticks(rotation=45)  # rotate city names if long
plt.show()

######################################

# Scatter: Study Hours vs Grade, colored by Passed, sized by Age
sns.scatterplot(data=df, 
                x="Study_Hours", 
                y="Grade", 
                hue="Passed", 
                size="Age", 
                sizes=(50, 200), 
                alpha=0.8,
                edgecolor="black")

plt.title("Grade vs Study Hours (Color = Passed, Size = Age)")
plt.xlabel("Weekly Study Hours")
plt.ylabel("Grade")
plt.grid(True, alpha=0.5)
plt.show()




# Line plot: Average Grade by Age (sorted for trend)
sns.lineplot(data=df.sort_values("Age"), 
             x="Age", 
             y="Grade", 
             hue="City", 
             marker="o", 
             err_style="bars")

plt.title("Grade Trend by Age (Colored by City)")
plt.xlabel("Age")
plt.ylabel("Grade")
plt.show()



# relplot: Grade vs Study Hours, faceted by Subject, colored by Passed
sns.relplot(data=df, 
            x="Study_Hours", 
            y="Grade", 
            hue="Passed", 
            col="Subject",          # one subplot per subject
            kind="scatter", 
            height=3,               # size of each facet
            aspect=1.2, 
            palette="Set2")

plt.suptitle("Grade vs Study Hours by Subject", y=1.02)
plt.show()





# Apply style from previous slides (for consistency)
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.2)
sns.set_palette("Set2")

# Barplot: Average Grade by City, colored by Subject
sns.barplot(data=df, 
            x="City", 
            y="Grade", 
            hue="Subject", 
            errorbar="ci")  # confidence interval

plt.title("Average Grade by City (Grouped by Subject)")
plt.xlabel("City")
plt.ylabel("Average Grade")
plt.xticks(rotation=45)
plt.legend(title="Subject", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()





# Boxplot: Grade by Subject, colored by Passed
sns.boxplot(data=df, 
            x="Subject", 
            y="Grade", 
            hue="Passed", 
            palette="Set2")

plt.title("Grade Distribution by Subject (Passed vs Not Passed)")
plt.xlabel("Subject")
plt.ylabel("Grade")
plt.xticks(rotation=45)
plt.show()





# Violin plot: Grade by City, split by Passed
sns.violinplot(data=df, 
               x="City", 
               y="Grade", 
               hue="Passed", 
               split=True, 
               inner="quartile", 
               palette="husl")

plt.title("Grade Distribution by City (Split by Passed)")
plt.xlabel("City")
plt.ylabel("Grade")
plt.xticks(rotation=45)
plt.show()




# Apply style from previous slides (for consistency)
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.2)
sns.set_palette("Set2")

# Histogram: Distribution of Grades
sns.histplot(data=df, 
             x="Grade", 
             hue="Passed", 
             multiple="stack", 
             bins=10, 
             kde=True)   # add density curve # Kernel Density Estimate

plt.title("Grade Distribution (Stacked by Passed)")
plt.xlabel("Grade")
plt.ylabel("Count")
plt.show()