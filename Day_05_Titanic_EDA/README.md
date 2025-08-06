# 📊 Day 5: Exploratory Data Analysis on Titanic Dataset

Welcome to **Day 5** of the **100 Days of Data Mastery** journey!  
Today, we dive into the world of **Exploratory Data Analysis (EDA)** using the iconic Titanic dataset.  
Our goal is to uncover patterns, relationships, and insights using visual and statistical techniques — a critical step before modeling.

> **Note**: We're using the **cleaned dataset generated in Day 4** (`titanic_cleaned.csv`) as the foundation for today's analysis.

---

## 🎯 Objectives

- Perform univariate and bivariate EDA using `pandas`, `matplotlib`, and `seaborn`
- Visualize distributions of age, fare, survival rate, etc.
- Compare survival rates across gender, class, and embarkation port
- Detect skewed distributions and outliers visually
- Identify initial hypotheses and guide further questions

---

## 🧰 Tools & Libraries

- Python 3.9+
- pandas
- numpy
- matplotlib
- seaborn

Install all dependencies with:

```bash
pip install -r requirements.txt
````

---

## 📁 Folder Structure

```
Day_05_Titanic_EDA/
│
├── README.md                  # This file: project overview and instructions
├── titanic_EDA.ipynb          # EDA notebook with visual and statistical analysis
├── EDA_utils.py               # Python module with reusable plotting functions
├── requirements.txt           # List of required packages
└── outputs/
    ├── age_violin_survival.png
    ├── barplot_mean.png
    ├── boxplot.png
    ├── fare_by_class.png
    ├── heatmap.png
    └── ...
```

---

## 🔍 Key Concepts Covered

* Summary statistics and dataset profiling
* Univariate plots: histograms, boxplots, countplots
* Bivariate analysis: survival vs class, gender, age groups
* Conditional distributions with `hue`
* Visual insights to drive hypotheses and modeling choices

---

## 🛳️ Dataset: Titanic (Cleaned)

We use the **cleaned version** of the Titanic dataset prepared in **Day 4**.
It includes standardized, imputed, and deduplicated records — ready for analysis!

Key columns:

* `Survived`: Binary target variable
* `Pclass`, `Sex`, `Age`, `Fare`, `Embarked`: Key features for analysis

---

## ✅ Output Examples

* 📊 **Saved Plots** in `outputs/` for reporting or further use
* 📓 **Interactive Notebook** with charts and markdown explanations
* 🧩 **EDA Utilities** with custom functions in `EDA_utils.py`

---

## 🚀 What’s Next?

**Day 6: Correlation Analysis**
We’ll take our insights further by quantifying relationships between variables and discovering which features influence survival the most.

Stay curious — and keep analyzing!
---