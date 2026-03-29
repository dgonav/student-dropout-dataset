# Activity I — Supervised vs Unsupervised Learning
### Data Mining | Universidad de la Costa
**Professor:** José Escorcia-Gutierrez, Ph.D.

**Group:**
- Diego Navarro Gómez
- Dinelis García
- Juan Félix
- Kimberly Ochoa

---

## What we did

For this activity we had to create a synthetic dataset simulating a university dropout problem. The idea is that a model could later use this data to predict whether a student will drop out or not during their first year.

Since we already know the output (dropout: yes or no), this is a supervised learning problem — specifically a binary classification task.

The script generates 500 student records and saves them in a CSV file called `student_dropout_dataset.csv`.

---

## Variables

The dataset has three types of input variables plus the output:

- **Demographic:** Age, Gender, Origin (Urban/Rural)
- **Academic:** High School Average (0–5), Admission Result (0–100), First Semester Grades (0–5)
- **Financial:** Socioeconomic Level (1–6), Scholarships, Loans, Financial Aid
- **Output:** Dropout (Yes / No)

---

## How we handled the dropout variable

We didn't want it to be random, so we assigned it based on a simple probability model. The factors that increase dropout risk are:

- First semester grades below 2.5 → biggest risk factor (+40%)
- Socioeconomic level 1 or 2 → economic pressure (+30%)
- High school average below 3.0 → weak academic background (+20%)
- No scholarship or financial aid → adds a bit more (+5% each)

---

## Null values

We removed 10% of the values in each column randomly to simulate incomplete records, which is something that happens in real databases.

## Outliers

We added extreme values in two columns to simulate data entry errors:
- `First Semester Grades` → 5 rows with a value of 10 (impossible, max is 5)
- `High School Average` → 5 rows with a value of 0 (extremely low)

The script also generates a boxplot image called `outliers_boxplots.png` where you can see these outliers.

---

## How to run it

```bash
pip install numpy pandas matplotlib seaborn
python "SUPERVISED vs UNSUPERVISED LEARNING.py"
```
