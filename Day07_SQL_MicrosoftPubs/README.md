# 🗄️ Day 7: SQL for Data Science with Chinook Database

Welcome to **Day 7** of the **100 Days of Data Mastery** journey!
Today, we step into the world of **relational databases** and explore how to extract, aggregate, and analyze data using **SQL**.
Our focus will be on mastering **joins, filtering, grouping, and aggregations** — essential skills for any data analyst.

> **Note**: We’ll be working with the **Chinook SQLite Database**, a sample database that simulates a digital media store.

---

## 🎯 Objectives

* Connect to an SQLite database using Python
* Run SQL queries directly from Jupyter Notebook
* Perform **INNER JOIN** operations to combine related tables
* Apply **WHERE** filters for conditional extraction
* Use **GROUP BY** and **ORDER BY** for aggregations
* Save query results to CSV files for reporting
* Visualize aggregated results with `matplotlib` and `seaborn`

---

## 🧰 Tools & Libraries

* Python 3.9+
* sqlite3
* pandas
* matplotlib
* seaborn

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 📁 Folder Structure

```
Day_07_SQL_Chinook/
│
├── README.md                   # This file: project overview and instructions
├── analysis.ipynb              # Main notebook running SQL queries & visualizations
├── analysisSQL_utils.py        # Utility functions for querying and plotting
├── requirements.txt            # Python dependencies
├── data/
│   ├── chinook_practice.sql    # SQL practice queries
│   └── Chinook_Sqlite.sqlite   # SQLite database file
├── images/
│   └── ChinookDatabaseSchema.png # Database schema diagram
└── outputs/
    ├── acdc_songs.csv
    ├── albums_artists.csv
    ├── artists_most_songs.csv
    ├── brazil_customers.csv
    ├── customers_countries.csv
    ├── sales_by_country.csv
    ├── song_duration.csv
    ├── songs_per_genre.csv
    ├── songs_per_genre.png
    └── top_customers.csv
```

---

## 🔍 Key Concepts Covered

* **Basic SELECT Queries** — retrieving specific columns
* **INNER JOIN** — combining data across multiple tables
* **Filtering with WHERE** — extracting targeted subsets
* **Aggregations with COUNT, SUM, AVG** — summarizing data
* **GROUP BY + ORDER BY** — organizing and ranking results
* **Data Export** — saving SQL results to CSV
* **Visualization** — transforming query outputs into charts

---

## 🎼 Dataset: Chinook Database

The **Chinook Database** is a sample database representing a digital music store.
It contains information about:

* Customers & Invoices
* Artists, Albums, and Tracks
* Genres and Media Types
* Employees and their relationships to sales

**Source**: [Chinook SQLite Database on Kaggle](https://www.kaggle.com/datasets/ranasabrii/chinook)

---

## ✅ Output Examples

* **CSV files** of query results saved in `outputs/`
* **Bar charts** showing number of songs per genre
* **Tables** ranking top customers by spending
* **Aggregated reports** on sales by country, artist productivity, and more

---

## 🚀 What’s Next?

**Day 8: Retail Analytics (SQL + Pandas)**
We’ll combine the power of **SQL queries** with **Pandas** data manipulation to create a hybrid workflow for deeper analytics.

Keep querying — and let the database tell its story!
---