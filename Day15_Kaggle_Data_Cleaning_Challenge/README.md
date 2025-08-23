
# 🧹 Day 15: Kaggle Data Cleaning Challenge

Welcome to **Day 15** of the **100 Days of Data Mastery** journey!  
Today, we focus on the **Kaggle Data Cleaning Challenge**, where we practice systematic techniques to transform messy real-world data into a clean, structured format ready for analysis and modeling.  
This step is crucial in any data project since most datasets require significant preprocessing before extracting insights.

> **Note**: We use a cleaned version of the **Student Performance dataset by Kaggle** [`cleaned_student_performance.csv`](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams) for this project.

---

## 🎯 Objectives

* Handle **missing values** using imputation and removal strategies.  
* Standardize **categorical variables** by fixing inconsistencies.  
* Normalize and validate **numerical features**.  
* Detect and treat **outliers** in score distributions.  
* Perform **feature engineering** for categorical encoding and binning.  
* Visualize **score distributions** and categorical breakdowns.  
* Prepare a **final cleaned dataset** suitable for machine learning.  

---

## 🧰 Tools & Libraries

* Python 3.9+  
* numpy  
* pandas  
* matplotlib  
* seaborn  

Install all dependencies with:

```bash
pip install -r requirements.txt
````

---

## 📁 Folder Structure

```
Day_15_Kaggle_Data_Cleaning/
│
├── README.md                           # This file: project overview and instructions
├── kaggle_data_cleaning.ipynb          # Main notebook with data cleaning workflows
├── requirements.txt                     # Python dependencies
├── data/
│   └── cleaned_student_performance.csv # Cleaned version of the student performance dataset
└── outputs/
    ├── correlation_matrix.png
    ├── performance_category_distribution.png
    ├── score_by_gender.png
    ├── score_by_lunch.png
    ├── score_by_parental_education.png
    ├── score_by_test_preparation.png
    └── score_distributions.png
```

---

## 🔍 Key Concepts Covered

* **Missing Data Handling** — strategies for imputation, removal, and correction.
* **Data Cleaning** — fixing inconsistent categorical values and formatting.
* **Outlier Detection** — identifying unusual score values.
* **Feature Engineering** — transforming categorical variables for analysis.
* **Correlation Analysis** — understanding relationships between features and performance.
* **Visualization** — comparing student scores by gender, parental education, lunch type, and test preparation.

---

## 📊 Example Outputs

* **Distribution plots** — visualize exam scores.
* **Correlation heatmap** — highlight relationships between features.
* **Categorical breakdowns** — compare scores across groups (gender, lunch, education).
* **Performance segmentation** — categorize students by achievement levels.

---

## 🚀 What’s Next?

**Day 16: Kaggle — Google Sheets + Python (gspread)**
We’ll integrate Google Sheets with Python using the `gspread` library to automate data pipelines, manage datasets in the cloud, and collaborate more effectively.

From cleaning messy datasets to automating workflows with cloud spreadsheets — our data mastery journey keeps advancing.

---