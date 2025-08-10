"""
retail_utils.py - Retail Analytics Utility Functions

This module provides utility functions for:
- Data loading and inspection
- Data cleaning and preparation
- Exploratory Data Analysis (EDA)
- SQL database operations
- Visualization helpers

Author: David Caleb Chaparro Orozco
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import sqlite3
from IPython.display import display
import warnings
warnings.filterwarnings("ignore")

# Constants
BACKGROUND_COLOR = "#f5f5f5"
OUTPUT_DIR = "outputs"
DATA_DIR = "data"
DB_NAME = "retail_sales.db"

# Configure global visualization settings
def configure_visuals(figsize=(12, 8), palette="pastel"):
    sns.set(style="whitegrid", palette=palette)
    plt.rcParams["figure.figsize"] = figsize
    plt.rcParams['figure.facecolor'] = BACKGROUND_COLOR
    plt.rcParams['axes.facecolor'] = BACKGROUND_COLOR
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(DATA_DIR, exist_ok=True)

# Generate comprehensive overview of dataset
def data_overview(data):
    print("=".center(50,"="))
    print(f"\nRetail Sales Dataset Overview")
    print(f"Shape: {data.shape}")
    print("=".center(50,"="))
    
    print("Information about the features:")
    print(data.info())
    print("=".center(50,"="))
    
    print("Basic statistics check:")
    print(data.describe(include='all'))
    print("=".center(50,"="))
    
    print("Checking the number of unique values:")
    unique_counts = {col: data[col].nunique() for col in data.columns}
    display(pd.DataFrame(unique_counts, index=["Unique Count"]).transpose())
    print("=".center(50,"="))
    
    print("Check for missing values:")
    print(data.isnull().sum())
    print("=".center(50,"="))

# Clean and preprocess retail sales data
def clean_data(data):
    data_cleaned = data.copy()
    
    # Drop missing values
    data_cleaned = data_cleaned.dropna()
    
    # Rename columns
    data_cleaned = data_cleaned.rename(columns={
        "Transaction ID": "TransactionID",
        "Customer ID": "CustomerID",
        "Product Category": "ProductCategory",
        "Price per Unit": "PricexUnit",
        "Total Amount": "TotalAmount"
    })
    
    # Convert and extract date features
    data_cleaned['Date'] = pd.to_datetime(data_cleaned['Date'])
    data_cleaned['Month'] = data_cleaned['Date'].dt.month
    data_cleaned['Year'] = data_cleaned['Date'].dt.year
    
    return data_cleaned

# SQLite database operations for retail analytics
class RetailDatabase:
    
    def __init__(self, db_name=os.path.join(DATA_DIR, DB_NAME)):
        self.conn = sqlite3.connect(db_name)
        
    # Execute SQL query and return DataFrame
    def run_query(self, query):
        return pd.read_sql_query(query, self.conn)
    
    # Execute SQL statement without returning results
    def execute_sql(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()
        return f"Executed: {sql.split()[0]}"
    
    # Load DataFrame into database table
    def load_dataframe(self, df, table_name):
        df.to_sql(table_name, self.conn, index=False, if_exists='replace')
        return f"Loaded {len(df)} rows to {table_name}"
    
    # Close database connection
    def close(self):
        self.conn.close()
        
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

# Generate comprehensive EDA dashboard
def create_eda_dashboard(data):
    fig = plt.figure(figsize=(20, 40))
    gs = fig.add_gridspec(10, 2)
    gs.update(wspace=0.3, hspace=0.8)
    
    # Title
    title_ax = fig.add_subplot(gs[0, :])
    title_ax.set_facecolor(BACKGROUND_COLOR)
    for spine in title_ax.spines.values():
        spine.set_visible(False)
    title_ax.tick_params(left=False, bottom=False)
    title_ax.text(0.5, 0.5,
                    'Retail Sales EDA Dashboard\n(Transactions, Customers, Products)',
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize=20, fontweight='bold', fontfamily='serif')
    
    # Initialize subplots
    axes = [fig.add_subplot(gs[i//2, i%2]) for i in range(12)]
    
    # Visualization 1: Sales by Product Category
    sns.barplot(data=data, x='TotalAmount', y='ProductCategory', 
                estimator=sum, ci=None, palette='Blues_d', ax=axes[0])
    axes[0].set_title('Total Sales by Product Category', fontsize=14, fontweight='bold')
    
    # Visualization 2: Sales Trend
    sales_over_time = data.groupby('Date')['TotalAmount'].sum().reset_index()
    sns.lineplot(data=sales_over_time, x='Date', y='TotalAmount', 
                color='mediumseagreen', ax=axes[1])
    axes[1].set_title('Daily Sales Trend', fontsize=14, fontweight='bold')
    
    # Add remaining visualizations similarly...
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'retail_sales_dashboard.png'), 
                dpi=300, bbox_inches='tight')
    plt.close()
    
# Generate interactive Plotly visualizations
def create_interactive_plots(data):
    # Monthly Sales Trend
    monthly_sales = data.groupby(['Year', 'Month'])['TotalAmount'].sum().reset_index()
    monthly_sales['Period'] = monthly_sales['Month'].astype(str) + '-' + monthly_sales['Year'].astype(str)
    
    fig = px.line(monthly_sales, x='Period', y='TotalAmount', 
                title='Interactive Monthly Sales Trend',
                template='plotly_white')
    fig.write_html(os.path.join(OUTPUT_DIR, 'monthly_sales_trend.html'))
    
    # Sunburst Chart
    fig = px.sunburst(data, path=['Gender', 'ProductCategory'], values='TotalAmount',
                    title='Sales Distribution by Gender and Product Category',
                    template='plotly_white')
    fig.write_html(os.path.join(OUTPUT_DIR, 'sales_sunburst.html'))
    
    # Scatter Matrix
    fig = px.scatter_matrix(data,
                        dimensions=['Age', 'Quantity', 'PricexUnit', 'TotalAmount'],
                        color='Gender',
                        title='Scatter Matrix of Key Variables',
                        template='plotly_white')
    fig.write_html(os.path.join(OUTPUT_DIR, 'scatter_matrix.html'))

# Perform customer segmentation analysis
def analyze_customer_segments(db):
    # Create customer summary table
    db.execute_sql("""
    CREATE TABLE IF NOT EXISTS customer_summary AS
    SELECT
        CustomerID,
        Gender,
        Age,
        COUNT(TransactionID) AS TransactionCount,
        SUM(TotalAmount) AS TotalSpent,
        MIN(Date) AS FirstPurchaseDate,
        MAX(Date) AS LastPurchaseDate,
        JULIANDAY(MAX(Date)) - JULIANDAY(MIN(Date)) AS CustomerTenureDays
    FROM retail_sales
    GROUP BY CustomerID, Gender, Age
    """)
    
    # Segmentation query
    segments = db.run_query("""
    SELECT
        CASE
            WHEN TotalSpent > 2000 THEN 'VIP'
            WHEN TotalSpent > 1000 THEN 'Premium'
            WHEN TotalSpent > 500 THEN 'Standard'
            ELSE 'Basic'
        END AS CustomerTier,
        COUNT(*) AS CustomerCount,
        SUM(TotalSpent) AS TotalRevenue,
        AVG(TotalSpent) AS AvgSpend
    FROM customer_summary
    GROUP BY CustomerTier
    ORDER BY TotalRevenue DESC
    """)
    
    return segments

if __name__ == "__main__":
    print("Retail Analytics Utilities Module")