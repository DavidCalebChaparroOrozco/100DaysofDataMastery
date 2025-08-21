# 🏙️ Day 14: Airbnb NYC Dataset

Welcome to **Day 14** of the **100 Days of Data Mastery** journey!  
Today, we dive into the **Airbnb NYC dataset** from Kaggle to explore **pricing, availability, and geographic trends**.  
This project combines **EDA, visualization, and mapping** to uncover key insights about hosts, listings, and customer preferences across New York City boroughs.  

> **Note**: We use a cleaned version of the Airbnb dataset (`airbnb_nyc_cleaned.csv`) for analysis.

---

## 🎯 Objectives

* Explore the **distribution of listings** across boroughs and room types.  
* Analyze **price variations** based on location, room type, and number of bedrooms.  
* Detect **seasonality and availability trends** in Airbnb listings.  
* Compare **hosts and their listings**, identifying top contributors.  
* Apply **geospatial visualization** to map listing density and pricing across NYC.  
* Derive **actionable insights** on customer preferences and market dynamics.  

---

## 🧰 Tools & Libraries

* Python 3.9+  
* numpy  
* pandas  
* matplotlib  
* seaborn  
* folium (for interactive maps)  

Install all dependencies with:

```bash
pip install -r requirements.txt
````

---

## 📁 Folder Structure

```
Day_14_Airbnb_NYC_Dataset/
│
├── README.md                      # This file: project overview and instructions
├── airbnb_nyc_analysis.ipynb      # Main notebook with EDA and visualization
├── requirements.txt               # Python dependencies
├── data/
│   └── airbnb_nyc_cleaned.csv     # Cleaned Airbnb NYC dataset
└── outputs/
    ├── availability_by_borough.png
    ├── correlation_matrix.png
    ├── listings_per_host.png
    ├── manhattan_brooklyn_price_comparison.png
    ├── nyc_airbnb_map.html
    ├── price_by_availability.png
    ├── price_by_bedrooms.png
    ├── price_by_borough.png
    ├── price_by_room_type.png
    ├── price_distribution.png
    ├── price_heatmap.png
    ├── reviews_last_12_months.png
    ├── room_type_distribution_by_borough.png
    ├── room_type_distribution.png
    └── top_hosts.png
```

---

## 🔍 Key Concepts Covered

* **Price Analysis** — distribution of prices across boroughs, room types, and availability.
* **Geospatial Visualization** — mapping listings to explore geographic density and pricing hotspots.
* **Host Insights** — identifying top hosts and analyzing their impact on the marketplace.
* **Seasonality & Availability** — exploring listing availability and review patterns over time.
* **Room Type Dynamics** — comparing private rooms, shared rooms, and entire homes.
* **Correlation Analysis** — understanding numerical feature relationships with price and demand.

---

## 📊 Example Outputs

* **Price distribution plots** — detect skewness and anomalies.
* **Room type breakdowns** — visualize preferences across boroughs.
* **Heatmaps** — show price concentration across NYC.
* **Interactive Folium map** — visualize Airbnb listings geographically.
* **Top hosts analysis** — highlight most active contributors.
* **Borough-level comparisons** — Manhattan vs Brooklyn price dynamics.

---

## 🚀 What’s Next?

**Day 15: Kaggle Data Cleaning Challenge**
We’ll tackle messy, real-world datasets by applying systematic **data cleaning** techniques: handling missing values, fixing inconsistencies, and preparing data for modeling.

From exploring Airbnb dynamics to cleaning new datasets — we continue sharpening our data mastery skills.

---
 