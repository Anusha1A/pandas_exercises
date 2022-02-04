
import pandas as pd
data = pd.read_csv("employee_filled_missing_values.csv")
fill_missing_values=data.fillna("N/A")
print(fill_missing_values)
