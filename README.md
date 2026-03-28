# Student Dropout Dataset

This dataset was created as part of Activity I for the Data Mining course at Universidad de la Costa, where we had to generate a synthetic dataset simulating student dropout during the first academic year.

The idea behind the dataset is simple: given information about a student (their age, where they're from, their grades, their economic situation), can a machine learning model predict whether they'll drop out or not? That's a yes/no question, so we're dealing with a binary classification problem — which is why supervised learning makes sense here.

---

## About the data

The dataset has **500 records**, each one representing a fictional student. The columns are organized in three groups plus the output variable:

**Demographic**
- `Age` — student age, ranges from 16 to 30
- `Gender` — Male or Female
- `Origin` — where the student comes from: Urban, Rural, or Suburban

**Academic**
- `High_School_Average` — GPA from high school, on a 0.0 to 5.0 scale (Colombian grading system)
- `Admission_Result` — score on the university admission test, from 0 to 100
- `First_Semester_Grades` — average grade during the first semester, also 0.0 to 5.0

**Financial**
- `Socioeconomic_Level` — Colombian socioeconomic stratum, from 1 (lowest) to 6 (highest)
- `Scholarships` — Yes or No
- `Loans` — Yes or No
- `Financial_Aid` — Yes or No

**Output**
- `Dropout` — whether the student dropped out: **Yes** or **No**

---

## How we generated the dropout variable

We didn't want `Dropout` to be completely random because that wouldn't make sense for a real prediction problem. So we built a probability model where a student is more likely to drop out if:

- Their first semester grades are below 2.5 (adds 40% to dropout probability)
- Their socioeconomic level is 1 or 2 (adds 30%)
- Their high school average was below 3.0 (adds 20%)
- They have no scholarship (adds 10%)
- They have no financial aid (adds 10%)

This way the output variable actually has a logical relationship with the other columns, which is what you'd expect in a real dataset.

---

## Null values

We introduced null values randomly in all columns at a 10% rate. This simulates what happens in real university databases, where not every student has complete information on file — maybe they didn't fill out a form, or the data was never recorded.

```python
for col in data.columns:
    null_indices = data.sample(frac=0.10, random_state=42).index
    data.loc[null_indices, col] = np.nan
```

---

## Outliers

We added outliers in three numeric columns to simulate data entry errors:

| Column | What we did | Rows affected |
|---|---|---|
| `First_Semester_Grades` | Values between 8.0 and 12.0 (the max valid is 5.0) | 8 rows |
| `High_School_Average` | Values between 0.0 and 0.5 (almost zero) | 8 rows |
| `Age` | Impossible ages like 5, 90 or 100 | 5 rows |

These were added after the main dataset was built, so they don't affect the dropout logic.

---

## How to run it

You need Python with these libraries:

```bash
pip install numpy pandas matplotlib seaborn
python SUPERVISED_vs_UNSUPERVISED_LEARNING.py
```

Running the script will generate two files:
- `student_dropout_dataset.csv` — the full dataset
- `outliers_boxplots.png` — boxplot graphs showing where the outliers are

---

## Authors

- Diego Navarro Gómez, Dinelis García, Juan Félix, Kimberly Ochoa  — Systems Engineering, Universidad de la Costa
