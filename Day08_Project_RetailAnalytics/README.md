# 🛍️ Day 8: Retail Analytics with SQL + Pandas

Welcome to **Day 8** of the **100 Days of Data Mastery** journey!
Today, we combine the querying power of **SQL** with the data manipulation flexibility of **Pandas** to analyze a retail sales dataset.
This hybrid workflow allows us to efficiently extract, aggregate, and visualize business insights.

> **Note**: We’ll be working with the **Retail Sales Dataset** from Kaggle, which contains transactional-level data for a store’s sales, customers, and products.

---

## 🎯 Objectives

* Connect to an SQLite retail sales database
* Execute SQL queries from within a Jupyter Notebook
* Apply `JOIN` operations to combine multiple tables
* Perform aggregations such as **SUM**, **AVG**, and **COUNT**
* Load SQL results directly into Pandas for additional analysis
* Create visualizations to identify trends and patterns
* Export query outputs for reporting

---

## 🧰 Tools & Libraries

* Python 3.9+
* sqlite3
* pandas
* matplotlib
* seaborn
* plotly

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 📁 Folder Structure

```
Day_08_Retail_Analytics/
│
├── README.md                   # This file: project overview and instructions
├── analysis.ipynb              # Main notebook combining SQL queries and Pandas analysis
├── retail_utils.py             # Utility functions for database connection, querying, and visualization
├── requirements.txt            # Python dependencies
├── data/
│   ├── retail_queries.sql      # Predefined SQL queries for analysis
│   └── retail_sales.db         # SQLite retail database
├── images/
│   └── schema_diagram.png      # Database schema diagram
└── outputs/
    ├── customer_tiers.png
    ├── monthly_sales_growth_corrected.png
    ├── monthly_sales_trend.html
    ├── retail_sales_dashboard.png
    ├── sales_sunburst.html
    └── scatter_matrix.html
```

---

## 🔍 Key Concepts Covered

* **SQL for Data Extraction** — filtering, aggregating, and joining data
* **Pandas for Data Wrangling** — cleaning, transforming, and feature engineering
* **Hybrid Workflow** — combining SQL efficiency with Pandas flexibility
* **Data Visualization** — bar charts, scatter plots, sunburst charts, and dashboards
* **Exporting Outputs** — saving static and interactive visualizations

---

## 🛒 Dataset: Retail Sales

The **Retail Sales Dataset** includes transactional data for sales in a retail store.
Key information includes:

* Customer demographics
* Product details
* Sales transactions
* Revenue over time

**Source**: [Retail Sales Dataset on Kaggle](https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset)

---

## ✅ Output Examples

* **Customer Segmentation** — Tier classification by spending
* **Monthly Sales Trends** — Static and interactive charts
* **Product Performance** — Sunburst visualization by category and subcategory
* **Sales Dashboard** — Consolidated KPIs and charts in one view

---

## 🚀 What’s Next?

**Day 9: Probability Fundamentals**
We’ll step into the world of probability theory, learning how to quantify uncertainty and model real-world scenarios.

## Data tells the story — and today we learned to ask the right questions using the best of both SQL and Pandas!