import pandas as pd
my_df = {'Roll_no': [1,2,3,4,5,6,7,8,9,10],
		'Student_Name': ['Anusha','kowsalya','Ramya','bavithra','Maneela','Balasri','Hema','Sona','Sowndarya','Dhivya'],
		'Year': [1,2,3,4,2,3,4,1,2,4],
         '1st_sem_gpa':[7,8,9,6,7,8,7,7,9,7.1],
         '2nd_sem_gpa':[8,6,7,8,7,6,7,8,8,9],
         '3rd_sem_gpa':[6,7,8,9,6,7,8,9,7,7],
         '4th_sem_gpa':[7.1,8.3,9,6,7.2,7.6,8.6,9.1,6.4,6.7],
         '5th_sem_gpa':[6.1,6.2,6.3,6.4,6.5,6.6,6.7,6.8,6.9,7],
         '6th_sem_gpa':[7.1,7.2,7.3,7.4,7.5,7.6,7.7,7.8,7.9,8],
         '7th_sem_gpa':[8.1,7.1,6.1,6.2,8.9,7.5,7.8,7.9,7,7.7],
         '8th_sem_gpa':[7.1,8.1,9.1,7.2,7.3,8.3,9.3,9.1,7.8,7.7]}
df = pd.DataFrame(my_df)
print('DataFrame:\n', df)
student_details_csv_data = df.to_csv('student_details.csv', index = False)
print('\nCSV String:\n', student_details_csv_data)
