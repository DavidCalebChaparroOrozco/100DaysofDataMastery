# 📈 Day 6: Correlation Analysis on Titanic Dataset

Welcome to **Day 6** of the **100 Days of Data Mastery** journey!  
Today, we move from visual exploration to **quantifying relationships** between variables using **correlation analysis**.  
We'll explore both **numeric** and **categorical** associations to better understand which features most strongly relate to survival.

> **Note**: We’re building on the **cleaned dataset from Day 4** (`titanic_cleaned.csv`).

---

## 🎯 Objectives

- Compute and visualize Pearson correlation among numeric variables
- Analyze survival rates across categorical features
- Use **Cramér’s V** to assess relationships between categorical pairs
- Discover how combined features (like `pclass` & `sex`) influence survival
- Build reusable correlation functions for scalable analysis

---

## 🧰 Tools & Libraries

- Python 3.9+
- pandas
- numpy
- seaborn
- matplotlib
- scipy

Install all dependencies with:

```bash
pip install -r requirements.txt
````

---

## 📁 Folder Structure

```
Day_06_Titanic_Correlation/
│
├── README.md                    # This file: project overview and instructions
├── correlation_analysis.ipynb   # Main notebook with full correlation analysis
├── correlation_utils.py         # Modular functions for plotting and computing correlation
├── requirements.txt             # Python dependencies
├── data/
│   └── titanic_cleaned.csv      # Cleaned dataset from Day 4
└── outputs/
    ├── combined_pclass_by_sex.png
    ├── cramers_v_matrix.png
    ├── numeric_correlation.png
    ├── survival_by_alive.png
    ├── survival_by_class.png
    ├── survival_by_embarked.png
    ├── survival_by_embark_town.png
    ├── survival_by_sex.png
    └── survival_by_who.png
```

---

## 🔍 Key Concepts Covered

* 📐 **Pearson Correlation** for numerical relationships
* 🔗 **Cramér's V** for categorical associations
* 🎨 Visual tools: Heatmaps, barplots, grouped bar charts
* 📊 Feature engineering: Age groups, combined factors
* 📁 Code modularization for reusable analysis workflows

---

## 🛳️ Dataset: Titanic (Cleaned)

We continue using the **cleaned Titanic dataset** from Day 4.
This version includes imputed missing values, standardized formats, and cleaned duplicates.

Important columns:

* `survived`: Binary outcome (0 = No, 1 = Yes)
* `pclass`, `sex`, `age`, `fare`, `embarked`, `who`, `alone`: Features for correlation

---

## ✅ Output Examples

* 📊 **Heatmaps** of Pearson & Cramér’s V correlation matrices
* 🧠 **Survival Rate Plots** across multiple categories
* 🧩 **Combined Feature Visualizations** (e.g. class & sex)
* 💡 **Reusable Utilities** in `correlation_utils.py` for future datasets

---

## 🚀 What’s Next?

**Day 7: SQL for Data Science**
We’ll step into relational databases and learn to **query data with SQL**, using techniques like `JOIN`, `GROUP BY`, and aggregations — foundational tools for every data professional.

Keep exploring the patterns — and let the data guide you!
---
