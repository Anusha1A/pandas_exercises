import pandas as pd
data = pd.read_csv("employees.csv")
percent_missing = data.isnull().sum() * 100 / len(data)
print(percent_missing)