

# 🎲 Day 9: Probability Fundamentals

Welcome to **Day 9** of the **100 Days of Data Mastery** journey!
Today, we dive into the essential building blocks of **probability theory** — the foundation of statistics, machine learning, and data-driven decision-making.
Through a mix of simulations, theoretical calculations, and visualizations, we’ll explore how to model uncertainty and randomness.

> **Note**: The datasets used here are generated through simulations for illustrative purposes.

---

## 🎯 Objectives

* Simulate random experiments: coin tosses, dice rolls, and event probabilities
* Apply **basic probability rules**:

  * Complement Rule
  * Addition Rule
  * Conditional Probability
  * Bayes’ Theorem
* Work with **discrete random variables**:

  * Probability Mass Functions (PMF)
  * Expected Value and Variance
* Explore **probability distributions**:

  * Bernoulli
  * Binomial
  * Normal
* Compare theoretical vs. empirical probabilities
* Visualize probability concepts for better intuition

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
Day_09_Probability_Fundamentals/
│
├── README.md                      # This file: project overview and instructions
├── probability_fundamentals.ipynb # Main notebook with simulations and probability analysis
├── probability_utils.py           # Utility functions for probability calculations and plotting
├── requirements.txt               # Python dependencies
├── data/
│   ├── coin_tosses.csv             # Simulated coin toss results
│   ├── dice_rolls.csv              # Simulated dice roll results
│   └── events_dataset.csv          # Dataset for event probability exercises
└── outputs/
    ├── BernoulliDistribution.png
    ├── BinomialDistribution.png
    ├── DistributionofSampleMeans.png
    ├── NormalDistribution.png
    ├── NumberofTailsTheoricalvsEmpirical.png
    ├── PDFofHeights.png
    └── PMFofDiceRolls.png
```

---

## 🔍 Key Concepts Covered

* **Simulations** — coin tosses, dice rolls, and event-based experiments
* **Probability Rules** — complement, addition, conditional probability, Bayes' theorem
* **Random Variables** — PMF, expected value, and variance
* **Distributions** — Bernoulli, Binomial, Normal
* **Empirical vs. Theoretical** — validating simulations against formulas

---

## 📊 Example Outputs

* Bar chart of dice roll PMF
* Bernoulli distribution visualization
* Binomial probability distribution plot
* Normal distribution curve (PDF) and cumulative distribution function (CDF)
* Side-by-side comparison of empirical vs. theoretical probabilities

---

## 🚀 What’s Next?

**Day 10: Distributions and Outliers**
We’ll expand our understanding of probability by exploring statistical distributions in depth and learning techniques to detect and handle outliers in datasets.

Probability is the language of uncertainty — and today, we started speaking it fluently.
---