
# 🛠️ Day 12: Basic Feature Engineering

Welcome to **Day 12** of the **100 Days of Data Mastery** journey!
Today, we focus on **Basic Feature Engineering**, the essential step of transforming raw data into meaningful inputs for machine learning models.
Through practical techniques, we’ll clean, transform, scale, encode, and create new features to improve model performance and interpretability.

> **Note**: We work with a processed sales dataset to demonstrate real-world feature engineering techniques.

---

## 🎯 Objectives

* Perform **data cleaning**:

  * Handle missing values using different imputation strategies.
  * Detect and treat outliers when necessary.
* Apply **feature transformation**:

  * Normalize or standardize numerical variables.
  * Encode categorical variables using one-hot encoding.
* Create **derived features**:

  * Combine or transform existing variables into new, more informative features.
* Perform **feature selection**:

  * Use statistical methods to retain only the most relevant variables.
* Visualize feature correlations to guide selection and transformation.

---

## 🧰 Tools & Libraries

* Python 3.9+
* numpy
* pandas
* matplotlib
* seaborn
* scikit-learn

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 📁 Folder Structure

```
Day_12_Basic_Feature_Engineering/
│
├── README.md                        # This file: project overview and instructions
├── basic_feature_engineering.ipynb  # Main notebook with feature engineering steps
├── feature_engineering_utils.py     # Utility functions for preprocessing & feature creation
├── requirements.txt                 # Python dependencies
├── data/
│   └── processed_sales_data.csv     # Example dataset for feature engineering
└── outputs/
    └── correlation_matrix.png       # Visualization of feature correlations
```

---

## 🔍 Key Concepts Covered

* **Data Cleaning** — handling missing values, outliers, and inconsistent data.
* **Scaling & Normalization** — adjusting numerical data for better model performance.
* **Encoding Categorical Variables** — transforming categories into numerical form.
* **Feature Creation** — engineering new variables from existing data.
* **Feature Selection** — keeping only the most informative variables.
* **Correlation Analysis** — understanding relationships between features.

---

## 📊 Example Outputs

* Correlation heatmap of numerical features.
* Before/after visualizations of scaling and normalization.
* Encoded dataset ready for modeling.
* New derived features improving dataset richness.

---

## 🚀 What’s Next?

**Day 13: Project — EDA + Visualization**
We’ll perform a full **Exploratory Data Analysis** on a real-world dataset, combining statistics and visualization techniques to uncover insights before modeling.

From transforming features to exploring data relationships — we’re building a strong foundation for predictive modeling.

---