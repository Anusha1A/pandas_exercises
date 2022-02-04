import pandas as pd
data = pd.read_csv("student_details_highest_score.csv")

highest_score=data[['1st_sem_gpa','2nd_sem_gpa','3rd_sem_gpa','4th_sem_gpa','5th_sem_gpa','6th_sem_gpa','7th_sem_gpa','8th_sem_gpa']].max(axis=1)
print(highest_score)
#data[highest_score_sem]=data.idxmax(axis="rows")
highest_score_sem=data[['1st_sem_gpa','2nd_sem_gpa','3rd_sem_gpa','4th_sem_gpa','5th_sem_gpa','6th_sem_gpa','7th_sem_gpa','8th_sem_gpa']].idxmax(axis=1)
print(highest_score_sem)
data={'Highest_score_of_a_student':highest_score,
      'Highest_score_of_student_in_a_sem':highest_score_sem

}
df=pd.DataFrame(data)

df.to_csv("student_detail_highest_score.csv",index=False)