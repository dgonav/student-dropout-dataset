# Activity I - Supervised vs Unsupervised Learning
# Data Mining - Universidad de la Costa
# Professor: José Escorcia-Gutierrez, Ph.D.
# Group: Diego Navarro, Dinelis García, Juan Félix, Kimberly Ochoa

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

n = 500  # 500 students

# demographic data
age = np.random.randint(16, 30, n)
gender = np.random.choice(["Male", "Female"], n)
origin = np.random.choice(["Urban", "Rural"], n)

# academic data
high_school_avg = np.random.uniform(2.0, 5.0, n)   # colombian scale goes up to 5
admission_result = np.random.uniform(0, 100, n)
first_semester_grades = np.random.uniform(0, 5, n)

# financial data
socioeconomic_level = np.random.randint(1, 7, n)   # colombia has strata 1 to 6
scholarships = np.random.choice(["Yes", "No"], n)
loans = np.random.choice(["Yes", "No"], n)
financial_aid = np.random.choice(["Yes", "No"], n)

# we dont want dropout to be completely random
# so we calculate a probability based on the students situation
dropout_probability = np.zeros(n)

dropout_probability += np.where(first_semester_grades < 2.5, 0.4, 0.0)  # bad grades = more risk
dropout_probability += np.where(socioeconomic_level <= 2, 0.3, 0.0)     # low income = more risk
dropout_probability += np.where(high_school_avg < 3.0, 0.2, 0.0)        # weak background
dropout_probability += np.where(scholarships == "No", 0.05, 0.0)
dropout_probability += np.where(financial_aid == "No", 0.05, 0.0)

dropout_probability = np.clip(dropout_probability, 0, 1)
dropout = np.where(np.random.rand(n) < dropout_probability, "Yes", "No")

# put everything together
data = pd.DataFrame({
    "Age": age,
    "Gender": gender,
    "Origin": origin,
    "High School Average": high_school_avg,
    "Admission Result": admission_result,
    "First Semester Grades": first_semester_grades,
    "Socioeconomic Level": socioeconomic_level,
    "Scholarships": scholarships,
    "Loans": loans,
    "Financial Aid": financial_aid,
    "Dropout": dropout
})

# add null values (10% per column to simulate missing data)
for col in data.columns:
    data.loc[data.sample(frac=0.10).index, col] = np.nan

print("=== First 5 rows ===")
print(data.head(5))

print("\n=== Missing values ===")
print(data.isnull().sum())

# add some outliers to make it more realistic
data.loc[np.random.choice(data.index, 5), "First Semester Grades"] = 10  # impossible grade (max is 5)
data.loc[np.random.choice(data.index, 5), "High School Average"] = 0     # extremely low

print("\n=== Outlier check ===")
print(data[["First Semester Grades", "High School Average"]].describe())

# boxplots to visualize the outliers
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

sns.boxplot(x=data["First Semester Grades"], ax=axes[0], color="tomato")
axes[0].set_title("Outliers - First Semester Grades")

sns.boxplot(x=data["High School Average"], ax=axes[1], color="steelblue")
axes[1].set_title("Outliers - High School Average")

plt.tight_layout()
plt.savefig("outliers_boxplots.png", dpi=150)
plt.close()
print("\nPlot saved as outliers_boxplots.png")

# save the dataset
data.to_csv("student_dropout_dataset.csv", index=False)
print("Dataset saved as student_dropout_dataset.csv")
print(f"Total records: {len(data)}")
print(f"\nDropout distribution:")
print(data["Dropout"].value_counts())
