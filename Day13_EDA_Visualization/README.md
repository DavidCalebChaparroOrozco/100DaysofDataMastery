# 📊 Day 13: Project — EDA + Visualization

Welcome to **Day 13** of the **100 Days of Data Mastery** journey!  
Today, we focus on a **full Exploratory Data Analysis (EDA)** project, where we combine **statistics and visualization techniques** to better understand the structure, patterns, and hidden insights in a sales dataset.  
EDA is the foundation of any data project, helping us validate assumptions, detect anomalies, and uncover relationships before modeling.  

> **Note**: We use a processed sales dataset to demonstrate real-world EDA workflows.

---

## 🎯 Objectives

* Explore **numeric and categorical feature distributions**.
* Detect **skewness, outliers, and anomalies** in sales data.
* Perform **correlation analysis** to identify feature relationships.
* Conduct **temporal analysis** of sales trends across months and years.
* Apply **Pareto and RFM analysis** to identify top customers and sales dynamics.
* Visualize **shipping behavior, product categories, and seasonal patterns**.
* Derive actionable **business insights** through data storytelling.

---

## 🧰 Tools & Libraries

* Python 3.9+
* numpy
* pandas
* matplotlib
* seaborn
* scipy
* squarify (for treemap visualization)

Install all dependencies with:

```bash
pip install -r requirements.txt
````

---

## 📁 Folder Structure

```
Day_13_EDA_Visualization/
│
├── README.md                        # This file: project overview and instructions
├── EDA_Visualization.ipynb          # Main notebook with EDA workflow
├── EDA_utils.py                     # Utility functions for reusable EDA tasks
├── requirements.txt                  # Python dependencies
├── data/
│   └── processed_sales_data.csv     # Sales dataset for EDA
└── outputs/
    ├── categorical_distributions.png
    ├── correlation_matrix.png
    ├── monthly_sales_trend.png
    ├── numeric_distributions.png
    ├── outliers_boxplot.png
    ├── product_treemap.png
    ├── rfm_distributions.png
    ├── sales_by_category_subcategory.png
    ├── shipping_mode_distribution.png
    ├── shipping_vs_sales.png
    ├── top_customers.png
    ├── weekday_analysis.png
    └── yearly_comparison.png
```

---

## 🔍 Key Concepts Covered

* **Distributions** — analyze numeric and categorical features to detect patterns.
* **Outlier Detection** — identify anomalies with boxplots, log transforms, and z-scores.
* **Correlation Analysis** — measure relationships between variables with heatmaps.
* **Temporal Trends** — monthly, yearly, and weekday sales patterns.
* **Pareto Principle** — identify the customers driving most sales.
* **RFM Analysis** — segment customers by Recency, Frequency, and Monetary value.
* **Business Insights** — uncover hidden trends in shipping, categories, and subcategories.

---

## 📊 Example Outputs

* **Numeric & categorical distributions** — histograms, bar charts, and KDE plots.
* **Correlation heatmap** — reveal strongest relationships with sales.
* **Pareto analysis** — cumulative sales distribution by customers.
* **RFM plots** — customer segmentation by purchasing behavior.
* **Treemap visualization** — sales by product subcategory.
* **Yearly & monthly sales trends** — seasonality insights.
* **Outlier detection** — extreme cases in sales and shipping duration.

---

## 🚀 What’s Next?

**Day 14: Airbnb NYC Dataset — Feature Engineering & EDA**
We’ll apply the same techniques of **EDA and visualization** to the **Airbnb NYC dataset from Kaggle**, uncovering insights into pricing, location dynamics, and customer preferences.

From analyzing sales to exploring a global dataset — we keep expanding our data mastery toolkit.

---
 