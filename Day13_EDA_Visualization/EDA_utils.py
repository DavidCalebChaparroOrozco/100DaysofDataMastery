# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
import os
import scipy
import squarify

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Helper: create dirs
def setup_environment():
    os.makedirs("outputs", exist_ok=True)
    os.makedirs("data", exist_ok=True)


# 1. Numeric Features Distribution
def plot_numeric_distributions(data, numeric_cols):
    plt.figure(figsize=(15, 10))
    for i, col in enumerate(numeric_cols, 1):
        plt.subplot(4, 4, i)
        sns.histplot(data[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.tight_layout()
    plt.savefig('outputs/numeric_distributions.png')
    plt.show()


# 2. Categorical Features Distribution
def plot_categorical_distributions(data, categorical_cols):
    cols_to_plot = [col for col in categorical_cols if col != 'CustomerID']
    n_cols = 3
    n_rows = math.ceil(len(cols_to_plot) / n_cols)

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))
    axes = axes.flatten()

    for i, col in enumerate(cols_to_plot):
        data[col].value_counts().plot(kind='bar', ax=axes[i])
        axes[i].set_title(f'Distribution of {col}')
        axes[i].tick_params(axis='x', rotation=45)

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.savefig('outputs/categorical_distributions.png')
    plt.show()


# 3. Improved Visualizations for Skewness & Outliers
def plot_sales_logscale(data):
    plt.figure(figsize=(10,6))
    sns.boxplot(x='Category', y='Sales', data=data)
    plt.yscale('log')
    plt.title("Sales Distribution by Category (Log Scale)")
    plt.show()

def plot_customer_sales_distribution(data):
    customer_sales = data.groupby("CustomerID")["Sales"].sum().reset_index()
    plt.figure(figsize=(10,6))
    sns.histplot(customer_sales["Sales"], bins=50, kde=True)
    plt.title("Total Sales per Customer")
    plt.yscale("log")
    plt.show()

def plot_boxen_subcategory(data):
    plt.figure(figsize=(12,6))
    sns.boxenplot(x="SubCategory", y="Sales", data=data)
    plt.xticks(rotation=45)
    plt.title("Sales Distribution by SubCategory (Boxen Plot)")
    plt.show()

def plot_pareto_analysis(data):
    customer_sales = data.groupby("CustomerID")["Sales"].sum().sort_values(ascending=False).reset_index()
    customer_sales["CumulativePct"] = customer_sales["Sales"].cumsum() / customer_sales["Sales"].sum() * 100
    plt.figure(figsize=(10,6))
    sns.lineplot(x=customer_sales.index, y=customer_sales["CumulativePct"])
    plt.axhline(80, color="red", linestyle="--")
    plt.title("Pareto Analysis: Cumulative Sales by Customers")
    plt.xlabel("Customers (sorted)")
    plt.ylabel("Cumulative % of Sales")
    plt.show()

def plot_log_transformed_sales(data):
    plt.figure(figsize=(8,5))
    sns.histplot(np.log1p(data["Sales"]), bins=50, kde=True)
    plt.title("Log-Transformed Sales Distribution")
    plt.xlabel("Log(Sales + 1)")
    plt.show()


# 4. Correlation Analysis
def correlation_analysis(data, numeric_cols):
    corr_matrix = data[numeric_cols].corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.savefig('outputs/correlation_matrix.png')
    plt.show()
    return corr_matrix


# 5. Temporal Analysis
def plot_monthly_sales(data):
    monthly_sales = data.groupby(['OrderYear', 'OrderMonth'])['Sales'].sum().reset_index()
    monthly_sales['Date'] = pd.to_datetime(monthly_sales['OrderYear'].astype(str) + '-' + monthly_sales['OrderMonth'].astype(str))
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='Sales', data=monthly_sales)
    plt.title('Monthly Sales Trend')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/monthly_sales_trend.png')
    plt.show()

def plot_sales_by_category_subcategory(data):
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='Category', y='Sales', hue='SubCategory', data=data)
    plt.title('Sales Distribution by Category and SubCategory')
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('outputs/sales_by_category_subcategory.png')
    plt.show()

def plot_shipping_vs_sales(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='ShippingDuration', y='Sales', hue='Category', data=data)
    plt.title('Shipping Duration vs Sales')
    plt.tight_layout()
    plt.savefig('outputs/shipping_vs_sales.png')
    plt.show()


# 6. Outlier Analysis
def outlier_analysis(data):
    plt.figure(figsize=(15, 8))
    for i, col in enumerate(['Sales', 'ShippingDuration', 'SalesPerShippingDay'], 1):
        plt.subplot(1, 3, i)
        sns.boxplot(y=data[col])
        plt.title(f'Outliers in {col}')
    plt.tight_layout()
    plt.savefig('outputs/outliers_boxplot.png')
    plt.show()

    numeric_for_outliers = data[['Sales', 'ShippingDuration', 'SalesPerShippingDay']]
    z_scores = scipy.stats.zscore(numeric_for_outliers)
    outliers = (abs(z_scores) > 3).any(axis=1)
    print(f"Number of outliers detected: {outliers.sum()}")
    return data[outliers]


# 7. Customer & RFM Analysis
def top_customers_plot(data):
    top_customers = data.groupby('CustomerID')['Sales'].sum().nlargest(10)
    plt.figure(figsize=(10, 6))
    top_customers.plot(kind='bar')
    plt.title('Top 10 Customers by Total Sales')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/top_customers.png')
    plt.show()

def rfm_analysis(data):
    rfm = data.groupby('CustomerID').agg({
        'OrderYear': 'max',
        'CustomerID': 'count',
        'Sales': 'sum'
    }).rename(columns={
        'OrderYear': 'Recency',
        'CustomerID': 'Frequency',
        'Sales': 'Monetary'
    })
    plt.figure(figsize=(15, 4))
    for i, col in enumerate(['Recency', 'Frequency', 'Monetary'], 1):
        plt.subplot(1, 3, i)
        sns.histplot(rfm[col], bins=20, kde=True)
        plt.title(f'Distribution of {col}')
    plt.tight_layout()
    plt.savefig('outputs/rfm_distributions.png')
    plt.show()
    return rfm

def treemap_sales(data):
    category_sales = data.groupby(['Category', 'SubCategory'])['Sales'].sum().reset_index()
    squarify.plot(
        sizes=category_sales['Sales'],
        label=category_sales.apply(lambda x: f"{x['SubCategory']}\n({x['Sales']:,.0f})", axis=1),
        color=sns.color_palette("Spectral", len(category_sales))
    )
    plt.title('Sales by Product SubCategory (Treemap)')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('outputs/product_treemap.png')
    plt.show()

def yearly_comparison(data):
    yearly_sales = data.groupby('OrderYear')['Sales'].sum()
    plt.figure(figsize=(8, 5))
    yearly_sales.plot(kind='bar', color=sns.color_palette("husl", len(yearly_sales)))
    plt.title('Year-over-Year Sales Comparison')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('outputs/yearly_comparison.png')
    plt.show()
    return yearly_sales

def weekday_analysis(data):
    weekday_sales = data.groupby('OrderWeekday')['Sales'].mean()
    weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekday_sales.index = weekday_names
    plt.figure(figsize=(10, 5))
    weekday_sales.plot(kind='bar')
    plt.title('Average Sales by Day of Week')
    plt.ylabel('Average Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/weekday_analysis.png')
    plt.show()
    return weekday_sales

def shipping_mode_distribution(data):
    shipping_modes = data[['ShipModeFirstClass', 'ShipModeSecondClass', 'ShipModeStandardClass']].sum()
    plt.figure(figsize=(8, 5))
    shipping_modes.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Shipping Mode Distribution')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig('outputs/shipping_mode_distribution.png')
    plt.show()
    return shipping_modes


# 8. Insights
def generate_insights(data, corr_matrix, yearly_sales, weekday_sales, shipping_modes):
    insights = {
        "Top Selling Category": data.groupby('Category')['Sales'].sum().idxmax(),
        "Most Frequent Shipping Mode": shipping_modes.idxmax(),
        "Year with Highest Sales": yearly_sales.idxmax(),
        "Day with Highest Average Sales": weekday_sales.idxmax(),
        "Correlation Shipping-Sales": corr_matrix.loc['ShippingDuration', 'Sales'].round(3),
        "Average Shipping Duration": data['ShippingDuration'].mean().round(2),
        "Total Customers": data['CustomerID'].nunique(),
        "Total Sales": f"${data['Sales'].sum():,.2f}"
    }
    return insights