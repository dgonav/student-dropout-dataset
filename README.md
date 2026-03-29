# Student Dropout Dataset

This is the dataset we created for Activity I of Data Mining at Universidad de la Costa. The idea was to simulate a real case where a university wants to predict which students are at risk of dropping out during their first year.

We generated 500 fictional student records using Python and included the variables the activity asked for: demographic, academic, and financial data, plus the dropout variable as the output.

---

## What's in the dataset

Each row represents a student. These are the columns:

**Demographic**
- `Age` — between 16 and 30 years old
- `Gender` — Male or Female
- `Origin` — Urban or Rural

**Academic**
- `High School Average` — GPA from high school, from 2.0 to 5.0 (Colombian grading scale)
- `Admission Result` — score on the university admission test, from 0 to 100
- `First Semester Grades` — average grade during the first semester, from 0.0 to 5.0

**Financial**
- `Socioeconomic Level` — Colombian stratum from 1 (lowest) to 6 (highest)
- `Scholarships` — Yes or No
- `Loans` — Yes or No
- `Financial Aid` — Yes or No

**Output**
- `Dropout` — Yes or No (this is what a model would try to predict)

---

## How we decided who drops out

We didn't want this to be completely random because that wouldn't make sense for a prediction problem. So we assigned dropout based on a probability model:

- First semester grades below 2.5 → +40% chance of dropping out
- Socioeconomic level 1 or 2 → +30%
- High school average below 3.0 → +20%
- No scholarship → +5%
- No financial aid → +5%

That way the output variable actually makes sense with the rest of the data.

---

## Null values

We set 10% of values in each column to null to simulate incomplete records, which is something that happens a lot in real university databases.

---

## Outliers

We added a few extreme values to simulate data entry errors:

- 5 rows where `First Semester Grades` is 10 (impossible, max is 5)
- 5 rows where `High School Average` is 0 (extremely low)

The script also generates a boxplot image called `outliers_boxplots.png` so you can see them visually.

---

## How to run it

```bash
pip install numpy pandas matplotlib seaborn
python "SUPERVISED vs UNSUPERVISED LEARNING.py"
```

It will generate two files in the same folder:
- `student_dropout_dataset.csv`
- `outliers_boxplots.png`

---

## Authors

- Diego Navarro Gómez — Systems Engineering, Universidad de la Costa
- Dinelis García — Systems Engineering, Universidad de la Costa
- Juan Félix — Systems Engineering, Universidad de la Costa
- Kimberly Ochoa — Systems Engineering, Universidad de la Costa
