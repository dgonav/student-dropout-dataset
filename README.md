# Activity I — Supervised vs Unsupervised Learning

**Universidad de la Costa**  
**Department of Computer Science and Electronics**  
**Course:** Data Mining  
**Professor:** José Escorcia-Gutierrez, Ph.D.  

**Group members:**
- Diego Navarro Gómez
- Dinelis García
- Juan Félix
- Kimberly Ochoa

---

## About this repository

This repository contains the synthetic dataset and the Python script we developed for Activity I. The goal of the activity was to analyze a real-world problem — student dropout in undergraduate programs — and determine which machine learning model would be best suited to predict it.

The dataset simulates 500 student records with demographic, academic, and financial information, plus a dropout variable (Yes/No) as the output. Since we are trying to predict a binary outcome using labeled historical data, this is a **supervised learning** problem, specifically a **binary classification** task.

---

## Dataset description

The file `student_dropout_dataset.csv` contains 500 records. Each row represents one fictional student. The columns are organized as follows:

**Demographic variables**
| Column | Type | Range / Values |
|---|---|---|
| Age | Integer | 16 to 30 |
| Gender | Categorical | Male, Female |
| Origin | Categorical | Urban, Rural |

**Academic variables**
| Column | Type | Range / Values |
|---|---|---|
| High School Average | Float | 2.0 to 5.0 (Colombian scale) |
| Admission Result | Float | 0 to 100 |
| First Semester Grades | Float | 0.0 to 5.0 |

**Financial variables**
| Column | Type | Range / Values |
|---|---|---|
| Socioeconomic Level | Integer | 1 to 6 (Colombian stratum) |
| Scholarships | Categorical | Yes, No |
| Loans | Categorical | Yes, No |
| Financial Aid | Categorical | Yes, No |

**Output variable**
| Column | Type | Values |
|---|---|---|
| Dropout | Categorical | Yes, No |

---

## How the dropout variable was generated

Instead of assigning dropout randomly, we built a simple probability model based on factors that are known to increase dropout risk in Colombian universities. Each factor adds a percentage to the student's dropout probability:

```
First Semester Grades < 2.5  →  +40%   (failing grades are the strongest predictor)
Socioeconomic Level <= 2      →  +30%   (economic pressure is a major cause of dropout)
High School Average < 3.0     →  +20%   (weak academic background increases the risk)
No Scholarship                →  +5%
No Financial Aid              →  +5%
```

The final Yes or No is assigned based on this probability, so the output variable has a logical relationship with the input variables — which is necessary for a supervised learning model to learn from it.

---

## How null values were introduced

We set 10% of the values in each column to null (`NaN`) to simulate incomplete records. In real university databases it is common for some fields to be missing — for example, a student who never submitted their financial information.

```python
for col in data.columns:
    data.loc[data.sample(frac=0.10).index, col] = np.nan
```

This results in approximately 50 missing values per column.

---

## How outliers were introduced

We added extreme values in two numeric columns to simulate data entry errors:

| Column | Outlier type | Value inserted | Rows affected |
|---|---|---|---|
| First Semester Grades | High outlier | 10 (max valid is 5.0) | 5 rows |
| High School Average | Low outlier | 0 (extremely low) | 5 rows |

The script generates a file called `outliers_boxplots.png` with boxplot graphs that show these outliers visually.

---

## How to run the script

Make sure you have Python installed with the following libraries:

```bash
pip install numpy pandas matplotlib seaborn
```

Then navigate to the folder where the script is saved and run:

```bash
python "SUPERVISED vs UNSUPERVISED LEARNING.py"
```

This will generate two output files in the same folder:
- `student_dropout_dataset.csv` — the full dataset
- `outliers_boxplots.png` — boxplot visualization of the outliers
