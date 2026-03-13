import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import json


df = pd.read_csv('users.csv')


print(df.head())     
print(df.info())     
print(df.describe())


print("\nMissing values per column:")
print(df.isnull().sum())


duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")


#df = df.dropna(subset=['maidenName'])


# if 'maidenName' in df.columns:
#     df['maidenName'].fillna('Unknown', inplace=True)

def parse_address(addr_str):
    try:
        addr_dict = json.loads(addr_str.replace("'", "\""))  # fix single quotes to double
        return addr_dict.get('city', 'Unknown') 
    except:
        return 'Unknown'

df['city'] = df['address'].apply(parse_address)


country_counts = df.groupby('city').size().reset_index(name='User_Count')

country_counts = country_counts.sort_values('User_Count', ascending=False)

print(country_counts.head(10))



plt.figure(figsize=(12, 8))

sns.barplot(data=country_counts.head(15),          
            x='User_Count', 
            y='city', 
            palette='viridis')

plt.title('Number of Users by Country (Top 15)', fontsize=16)
plt.xlabel('Number of Users', fontsize=12)
plt.ylabel('Country', fontsize=12)


plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()