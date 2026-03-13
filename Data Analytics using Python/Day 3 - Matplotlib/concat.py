import pandas as pd

jan_data = pd.DataFrame({
    'date': ['2025-01-01', '2025-01-02', '2025-01-03'],
    'sales': [1200, 1500, 1300],
    'product': ['A', 'B', 'A']
})
feb_data = pd.DataFrame({
    'date': ['2025-02-01', '2025-02-02'],
    'sales': [1800, 1600],
    'product': ['B', 'C']
})
mar_data = pd.DataFrame({
    'date': ['2025-03-01', '2025-03-02', '2025-03-03'],
    'sales': [1400, 1900, 1700],
    'product': ['A', 'C', 'B']
})
#  CSV 
jan_data.to_csv('jan.csv', index=False)
feb_data.to_csv('feb.csv', index=False)
mar_data.to_csv('mar.csv', index=False)

print(" jan.csv, feb.csv, mar.csv")
print()

# ────────────────────────────────────────────────
files = ['jan.csv', 'feb.csv', 'mar.csv']
dfs = [pd.read_csv(f) for f in files]
print(type(dfs))

all_data = pd.concat(dfs, ignore_index=True)

print("after concat :")
print(all_data)
print()

print("num of rows :", len(all_data))


########################################

