#Syntetic dataset creation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Number of records generated
n=500

#Generate variables indicated in the statement
#Demographic Data
age=np.random.randint(16,30,n)
gender=np.random.choice(["Male","Female"],n)
origin=np.random.choice(["Urban","Rural"],n)

#Academic Data
high_school_avg=np.random.uniform(2.0,5.0,n)
admission_result=np.random.uniform(0,100,n)
first_semester_grades=np.random.uniform(0,5,n)

#Financial Data
socioeconomic_level=np.random.randint(1,7,n)
scholarships=np.random.choice(["Yes","No"],n)
loans=np.random.choice(["Yes","No"],n)
financial_aid=np.random.choice(["Yes","No"],n)
dropout=np.random.choice(["Yes","No"],n)

#Final Dataset
data=pd.DataFrame({
    "Age": age,
    "Gender":gender,
    "Origin":origin,
    "High School Average":high_school_avg,
    "Admission Result":admission_result,
    "First Semester Grades":first_semester_grades,
    "Socioeconomic Level":socioeconomic_level,
    "scholarships":scholarships,
    "Loans":loans,
    "Financial Aid":financial_aid,
    "Dropout":dropout
})

#Add null values
for col in data.columns:
    data.loc[data.sample(frac=0.10).index, col]=np.nan #This code allows to generate Null values in a rate of 10% per every column

print(data.head(5))

print("\n Missing values")
print(data.isnull().sum())

#Outliers
data.loc[np.random.choice(data.index, 5), "First Semester Grades"]=10
data.loc[np.random.choice(data.index, 5), "High School Average"]=0

sns.boxplot(x=data["First Semester Grades"])
plt.title("Outliers - First Semester Grades")
plt.show

sns.boxplot(x=data["High School Average"])
plt.title("Outliers - High School Average")
plt.show

#Save the Dataset into a .CSV file
data.to_csv("student_dropout_dataset.csv", index=False)