# 🧹 Day 4: Data Cleaning & Preprocessing with Titanic Dataset

Welcome to **Day 4** of the **100 Days of Data Mastery** journey!  
Today’s focus is on cleaning and preprocessing real-world data — an essential skill before any meaningful analysis or modeling can take place.

We'll be working with the classic **Titanic dataset**, which provides a great mix of numerical, categorical, and missing data — perfect for practicing hands-on data cleaning.

---

## 🎯 Objectives

- Identify and remove duplicate records
- Handle missing data using domain-informed imputation or removal
- Correct inconsistent data formats
- Convert features to appropriate data types
- Detect and understand outliers
- Remove irrelevant or redundant columns
- Save the cleaned dataset for downstream analysis

---

## 🧰 Tools & Libraries

- Python 3.9+
- pandas
- numpy
- matplotlib
- seaborn

Install all required packages with:

```bash
pip install -r requirements.txt
````

---

## 📁 Folder Structure

```
Day_04_DataCleaning_Titanic/
│
├── README.md                  # This file: project overview and instructions
├── data_cleaning.ipynb        # Jupyter notebook with step-by-step data cleaning
├── cleaning_utils.py          # Python module with reusable cleaning functions
├── requirements.txt           # List of required Python packages
│
└── outputs/
    └── titanic_cleaned.csv    # Final cleaned Titanic dataset
```

---

## 🧼 Key Concepts Covered

* Removing exact and near duplicates
* Imputing missing values based on grouped medians or modes
* Dropping features with excessive missingness
* Standardizing inconsistent entries in categorical columns
* Adjusting incorrect data types (e.g., categorical vs numerical)
* Evaluating and documenting outliers (e.g., extreme fare or age values)
* Saving a clean, analysis-ready version of the dataset

---

## 🛳️ Dataset Used

The **Titanic dataset** contains information about the passengers aboard the RMS Titanic:

* Age, sex, and class (Pclass)
* Ticket fare and cabin info
* Survival status
* Embarkation port

This dataset is widely used in the data science community for practicing data preparation and classification models.

---

## ✅ Output Example

* **Cleaned CSV**: Located in the `outputs/` folder (`titanic_cleaned.csv`)
* **Notebook**: Interactive notebook (`data_cleaning.ipynb`) with all cleaning steps and explanations
* **Reusable Functions**: Cleaning helpers centralized in `cleaning_utils.py`

---

## 🚀 What’s Next?

Proceed to **Day 5: Titanic Dataset EDA**, where we’ll dive deeper into the cleaned data, uncover patterns, and extract insights using Exploratory Data Analysis techniques.

Keep cleaning — clean data = smart data!
---