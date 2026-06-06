import pandas as pd

df = pd.read_csv('/Users/irisli/PSTAT_134/project/netflix_reviews.csv')

# Total missing values in the entire dataset
print(df.isnull().sum().sum())

# Count of missing values per column
print(df.isnull().sum())

# Percentage of missing values per column
print(df.isnull().mean() * 100)
