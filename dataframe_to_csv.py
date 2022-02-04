# importing pandas as pd
import pandas as pd


nme = ["abc", "def", "ghi", "jkl"]
sal = [10000,20000,30000,40000]



dict = {'name': nme, 'salary': sal}

df = pd.DataFrame(dict)


df.to_csv('employee_details.csv')
