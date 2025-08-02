# 📊 Day 2: Exploratory Data Analysis (EDA) with Pandas

On the second day of my data journey, I focused on performing **Exploratory Data Analysis (EDA)** using the powerful **Pandas** library. This process helps uncover patterns, spot anomalies, test hypotheses, and check assumptions using summary statistics and visualizations.

---

## 📁 Folder Structure

```

Day2\_Pandas\_EDA/
│
├── data/
│   └── netflix\_top10.csv
│
├── utils/
│   └── statistics\_utils.py
│
├── eda\_analysis.ipynb
├── README.md
└── outputs/
├── top10\_shows\_per\_week.png
├── genre\_distribution.png
└── weekly\_hours\_trend.png

````

---

## 📌 Dataset Used

The dataset used is the **[Netflix Top 10 Weekly Data](https://github.com/rfordatascience/tidytuesday/blob/master/data/2022/2022-01-18/netflix_titles.csv)**, originally curated by the team at [rfordatascience/tidytuesday](https://github.com/rfordatascience/tidytuesday). This dataset includes weekly global Top 10 shows/movies on Netflix, categorized by type, title, release year, and total hours viewed.

---

## 🔍 EDA Goals

1. **Clean the dataset** – handle missing values and format columns.
2. **Explore categorical and numerical features** – like genre, type, hours watched.
3. **Visualize** trends and distributions.

---

## ✨ Real-Life Example: Streaming Habits

Imagine you're analyzing the **viewing habits of Netflix users**. You may wonder:

- What genres are most watched?
- Are movies or TV shows more popular?
- Which weeks had viewing spikes?
- Is there seasonality in the content people watch?

These are exactly the types of questions we can answer with EDA.

---

## 🔧 Data Cleaning

Using a helper function:

```python
def data_cleaning(data: pd.DataFrame) -> pd.DataFrame:
    # Handle missing values, parse dates, standardize column names
    ...
````

This cleaned our data to make it analysis-ready.

---

## 📈 Key Visualizations

### 1. Top 10 Shows per Week

Shows the most watched shows each week and how often they appear.

![top10\_shows\_per\_week](outputs/top10_shows_per_week.png)

---

### 2. Genre Distribution

Displays how many times each genre appears in the Top 10 list.

![genre\_distribution](outputs/genre_distribution.png)

---

### 3. Weekly Hours Watched Trend

Tracks the total hours viewed over time to identify peaks.

![weekly\_hours\_trend](outputs/weekly_hours_trend.png)

---

## 🧠 What I Learned

* **Pandas GroupBy** is key for summarizing and slicing data.
* **Missing data** can heavily skew your interpretations if not handled.
* Visuals help explain the story behind the data better than raw numbers.

---

## ✅ Example Insight

> In the last quarter of 2021, **TV Shows** dominated the Top 10 rankings, especially genres like **Drama** and **Crime**, possibly due to global releases like *Money Heist* and *Squid Game*.

---

## 🙏 Acknowledgment

Thanks to [rfordatascience/tidytuesday](https://github.com/rfordatascience/tidytuesday) for making this dataset publicly available. It’s been an excellent resource for exploring real-world data and sharpening my analysis skills.

---

## 🚀 Next Steps

Tomorrow, I plan to dive into **Data Preprocessing & Feature Engineering**, preparing this data for modeling.

---

> In commitment and discipline lie the seeds of accomplishment.

```

---
