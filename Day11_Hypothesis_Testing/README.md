# 🧪 Day 11: Hypothesis Testing (z, t, chi-squared)

Welcome to **Day 11** of the **100 Days of Data Mastery** journey!  
Today, we step into the world of **statistical hypothesis testing**, where we validate assumptions, compare groups, and draw data-driven conclusions with measurable confidence.  
We explore **z-tests**, **t-tests**, and **chi-squared tests**, both through theoretical explanations and hands-on examples.

> **Note**: The datasets include both **synthetic samples** and **categorical frequency tables** for practical test applications.

---

## 🎯 Objectives

* Perform and interpret different hypothesis tests:
  * **Z-test** — compare a sample mean to a known population mean.
  * **Independent t-test** — compare the means of two independent groups.
  * **Paired t-test** — compare related measurements before and after an event.
  * **Chi-squared test** — test independence between categorical variables.
* Visualize test results with meaningful plots.
* Understand **p-values**, **degrees of freedom**, and statistical significance.
* Compare **observed** vs **expected** frequencies in categorical data.
* Highlight differences between observed and expected with comparison plots.

---

## 🧰 Tools & Libraries

* Python 3.9+
* numpy
* pandas
* matplotlib
* seaborn
* scipy

Install all dependencies with:

```bash
pip install -r requirements.txt
````

---

## 📁 Folder Structure

```
Day_11_Hypothesis_Testing/
│
├── README.md                        # This file: project overview and instructions
├── hypothesis_testing.ipynb         # Main notebook with hypothesis testing workflows
├── hypothesis_utils.py               # Utility functions for performing tests & plotting results
├── requirements.txt                  # Python dependencies
├── data/
│   ├── contingency_table.csv         # Categorical dataset for chi-squared test
│   ├── heights_sample.csv            # Heights dataset for z-test and independent t-test
│   └── sales_before_after.csv        # Paired dataset for before/after t-test
└── outputs/
    ├── chi_squared_comparison_improved.png
    ├── chi_squared_observed_expected_difference.png
    ├── height_distribution.png
    ├── paired_t_test_visualization.png
    ├── product_sales_by_state.png
    ├── sales_distribution.png
    ├── t_test_visualization.png
    └── z_test_visualization.png
```

---

## 🔍 Key Concepts Covered

* **Z-test** — determine if a sample mean significantly differs from a population mean.
* **T-test**:

  * **Independent** — compare two unrelated groups.
  * **Paired** — compare measurements before and after a treatment.
* **Chi-squared test** — test the relationship between categorical variables.
* **P-values & significance levels** — interpret the strength of results.
* **Observed vs Expected analysis** — visualize categorical differences.

---

## 📊 Example Outputs

* Z-test visualization showing sample vs population mean.
* Boxplot comparison of two groups for t-test.
* Paired line plot of before/after measurements.
* Bar charts for chi-squared test: observed, expected, and differences.

---

## 🚀 What’s Next?

**Day 12: Basic Feature Engineering**
We’ll prepare raw data for modeling by creating, transforming, and selecting features to improve model performance.

From validating ideas statistically to transforming data for prediction — the journey continues.

---
