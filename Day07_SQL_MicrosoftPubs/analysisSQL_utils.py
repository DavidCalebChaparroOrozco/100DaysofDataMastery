# Import necessary libraries
import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, Union, List, Dict, Any

# Configure visualization settings and create output directory.
def configure_visuals(figsize: tuple = (12, 8), 
                    palette: str = "pastel", 
                    output_dir: str = "outputs") -> None:
    """    
    Args:
        figsize (tuple): Figure size (width, height) in inches. Default is (12, 8).
        palette (str): Color palette name. Default is "pastel".
        output_dir (str): Path to output directory for saving plots. Default is "outputs".
    """
    sns.set(style="whitegrid", palette=palette)
    plt.rcParams["figure.figsize"] = figsize
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

# Establish connection to SQLite database.
def connect_db(db_path: str) -> sqlite3.Connection:
    """
    Args:
        db_path (str): Path to SQLite database file
        
    Returns:
        sqlite3.Connection: Database connection object
    """
    return sqlite3.connect(db_path)

# Execute SQL query and return results as DataFrame.
def run_query(conn: sqlite3.Connection, 
                query: str, 
                params: Optional[Union[tuple, dict]] = None) -> pd.DataFrame:
    """
    Args:
        conn (sqlite3.Connection): Database connection
        query (str): SQL query to execute
        params (Optional[Union[tuple, dict]]): Parameters for parameterized query
        
    Returns:
        pd.DataFrame: Query results as DataFrame
    """
    return pd.read_sql_query(query, conn, params=params)

# Create and customize bar plot.
def plot_bar(data: pd.DataFrame, 
            x: str, 
            y: str, 
            title: str, 
            xlabel: str, 
            ylabel: str,
            orientation: str = 'vertical',
            output_file: str = "outputs") -> None:
    """
    Args:
        data (pd.DataFrame): Input data
        x (str): Column name for x-axis
        y (str): Column name for y-axis
        title (str): Plot title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
        orientation (str): 'vertical' or 'horizontal' bars
        output_file (Optional[str]): Path to save plot image
    """
    plt.figure()
    if orientation == 'vertical':
        sns.barplot(x=x, y=y, data=data)
    else:
        sns.barplot(x=y, y=x, data=data)
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.xticks(rotation=45)
    plt.ylabel(ylabel)
    plt.tight_layout()
    
    if output_file:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        plt.savefig(output_file)
        print(f"✅ Plot saved to: {output_file}")
    plt.show()

# Create and customize line plot for trends.
def plot_trend(data: pd.DataFrame, 
                x: str, 
                y: str, 
                title: str, 
                xlabel: str, 
                ylabel: str,
                output_file: str = "outputs") -> None:
    """
    Args:
        data (pd.DataFrame): Input data
        x (str): Column name for x-axis
        y (str): Column name for y-axis
        title (str): Plot title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
        output_file (Optional[str]): Path to save plot image
    """
    plt.figure()
    sns.lineplot(x=x, y=y, data=data, marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    
    if output_file:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        plt.savefig(output_file)
        print(f"✅ Plot saved to: {output_file}")
    plt.show()

# Save DataFrame to CSV file.
def save_to_csv(data: pd.DataFrame, 
                filename: str, 
                output_dir: str = "outputs") -> None:
    """
    Args:
        data (pd.DataFrame): Data to save
        filename (str): Output filename
        output_dir (str): Output directory path
    """
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    data.to_csv(filepath, index=False)
    print(f"Data saved to {filepath}")

# Get list of table names in the database.
def get_table_names(conn: sqlite3.Connection) -> List[str]:
    """
    Args:
        conn (sqlite3.Connection): Database connection
        
    Returns:
        List[str]: List of table names
    """
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    tables = run_query(conn, query)
    return tables['name'].tolist()

# Get schema information for a table.
def describe_table(conn: sqlite3.Connection, table_name: str) -> pd.DataFrame:
    """
    Args:
        conn (sqlite3.Connection): Database connection
        table_name (str): Name of table to describe
        
    Returns:
        pd.DataFrame: Table schema information
    """
    query = f"PRAGMA table_info({table_name});"
    return run_query(conn, query)

# Close database connection.
def close_connection(conn: sqlite3.Connection) -> None:
    """
    Args:
        conn (sqlite3.Connection): Database connection to close
    """
    if conn:
        conn.close()