# 📈 Day 3: Data Visualizations with Python

Welcome to **Day 3** of the **100 Days of Data Mastery** journey!  
Today’s focus is on building strong data visualization skills using Python.  
We’ll explore how to create, customize, and interpret a variety of plots to better understand and communicate data insights.

---

## 🎯 Objectives

- Learn to visualize distributions, relationships, and categorical data using `matplotlib` and `seaborn`.
- Practice creating histograms, boxplots, violin plots, swarm plots, heatmaps, KDE plots, and more.
- Build reusable visualization functions for common analysis tasks.
- Apply visualization techniques to a synthetic dataset with real-world features.

---

## 🧰 Tools & Libraries

- Python 3.9+
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

Install all requirements with:

```bash
pip install -r requirements.txt
```

---

## 📁 Folder Structure

```
Day3_Data_Visualizations/
│
├── README.md                      # This file: project overview and instructions
├── visualizations.ipynb           # Jupyter Notebook with step-by-step visualizations and code
├── visualization_utils.py         # Python module with reusable plotting functions
├── requirements.txt               # List of required Python packages
│
└── outputs/                       # Folder for saving generated plots
    ├── histogram.png
    ├── violin_plot.png
    ├── boxplot.png
    ├── swarmplot.png
    ├── kdeplot.png
    ├── barplot_mean.png
    ├── jointplot.png
    ├── heatmap.png
    └── radar_chart.png
```

---

## 📌 Key Concepts Covered

* Visualizing distributions: histograms, KDE plots, violin plots
* Comparing categories: boxplots, swarm plots, bar plots
* Exploring relationships: scatter plots, jointplots, pairplots
* Categorical heatmaps for frequency analysis
* Radar charts for comparing normalized means across groups
* Building reusable plotting functions for analysis workflows

---

## 📊 Dataset Used

We use a **synthetic dataset** simulating real-world features:
- Age
- Income
- Gender
- Job Category

This allows us to practice visualizing both numerical and categorical variables, as well as their interactions.

---

## ✅ Output Examples

* **Saved Plots**: All generated visualizations are saved in the `outputs/` folder for easy review and sharing.
* **Notebook Insights**: The Jupyter Notebook (`visualizations.ipynb`) contains code, explanations, and inline visualizations for each concept.
* **Reusable Functions**: The `visualization_utils.py` module provides ready-to-use plotting functions for future projects.

---

## 🚀 What’s Next?

Proceed to **Day 4: Data Cleaning & Preprocessing**, where we’ll learn how to prepare data for analysis and modeling.

Keep exploring and visualizing your data!