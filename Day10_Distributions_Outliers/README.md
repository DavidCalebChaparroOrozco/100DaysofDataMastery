# 📈 Day 10: Distributions and Outliers

Welcome to **Day 10** of the **100 Days of Data Mastery** journey!
Today, we expand our probability knowledge by exploring **statistical distributions** in depth and learning how to detect and interpret **outliers** in datasets.
Through practical simulations, visualizations, and statistical techniques, we’ll gain the tools to identify patterns and anomalies in data.

> **Note**: The datasets include both **synthetic data** (coin tosses, dice rolls) and **sample datasets** (heights, sales).

---

## 🎯 Objectives

* Visualize and understand key **probability distributions**:

  * **Binomial**
  * **Uniform** (continuous)
  * **Normal (Gaussian)**
* Apply the **Central Limit Theorem (CLT)** through simulations
* Detect outliers using:

  * **Z-score method**
  * **Interquartile Range (IQR)**
* Create **Q-Q plots** to assess normality
* Use boxplots to identify and visualize unusual values in real datasets

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
```

---

## 📁 Folder Structure

```
Day_10_Distributions_Outliers/
│
├── README.md                      # This file: project overview and instructions
├── distributions_outliers.ipynb   # Main notebook with distributions & outlier detection
├── distributions_utils.py         # Utility functions for generating plots & detecting outliers
├── requirements.txt                # Python dependencies
├── data/
│   ├── coin_tosses.csv             # Simulated Bernoulli trials
│   ├── dice_rolls.csv              # Simulated discrete uniform distribution
│   ├── heights_dataset.csv         # Continuous dataset for normality checks
│   └── sales_dataset.csv           # Dataset for boxplot-based outlier detection
└── outputs/
    ├── binomial_dist.png
    ├── coin_tosses.png
    ├── continuous_uniform.png
    ├── dice_rolls.png
    ├── heights_distribution.png
    ├── qq_plot_heights.png
    └── sales_boxplot.png
```

---

## 🔍 Key Concepts Covered

* **Binomial Distribution** — probability of successes in a fixed number of trials
* **Uniform Distribution** — equal probability for all outcomes in a range
* **Normal Distribution** — bell curve, standard deviation, and empirical rule
* **Central Limit Theorem** — why sample means tend to follow a normal distribution
* **Outlier Detection** — Z-score & IQR
* **Visualization Techniques** — histograms, KDE plots, Q-Q plots, and boxplots

---

## 📊 Example Outputs

* Probability Mass Function for binomial trials
* Histogram + KDE for normal and uniform distributions
* Q-Q plot to check normality of height data
* Boxplot identifying sales outliers

---

## 🚀 What’s Next?

**Day 11: Hypothesis Testing (z, t, chi-squared)**
We’ll use statistical tests to validate assumptions, compare groups, and draw conclusions from data with measurable confidence.

Understanding distributions and spotting anomalies is a key step — next, we’ll learn how to test our insights statistically.

---