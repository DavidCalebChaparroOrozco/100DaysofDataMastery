# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import os

# Configure output directory and visualization settings
def configure_visuals(figsize=(12, 8), palette="pastel", output_dir="outputs"):
    """
    Args:
        figsize (tuple): Figure size
        palette (str): Color palette
        output_dir (str): Path to output directory for saving plots
    """
    sns.set(style="whitegrid", palette=palette)
    plt.rcParams["figure.figsize"] = figsize
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

# Calculate and plot Pearson correlation for numeric features
def plot_numeric_correlation(data, target_var='survived', save_plot=True, output_dir="outputs"):
    """    
    Args:
        data (DataFrame): Input dataframe
        target_var (str): Target variable for correlation analysis
        save_plot (bool): Whether to save the plot
        output_dir (str): Output directory path
    """
    numeric_data = data.select_dtypes(include='number')
    
    if target_var not in numeric_data.columns:
        print(f"Target variable {target_var} not in numeric columns")
        return
    
    corr_matrix = numeric_data.corr(method="pearson")
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", 
                center=0, fmt=".3f", linewidths=.5)
    plt.title("Correlation Matrix of Numeric Features")
    
    if save_plot:
        output_path = os.path.join(output_dir, "numeric_correlation.png")
        plt.savefig(output_path, bbox_inches='tight', dpi=300)
        print(f"Plot saved to {output_path}")
    plt.show()
    
    return corr_matrix

# Plot survival rates by categorical features
def plot_categorical_survival(data, target_var='survived', save_plots=True, output_dir="outputs"):
    """    
    Args:
        data (DataFrame): Input dataframe
        target_var (str): Target variable for survival analysis
        save_plots (bool): Whether to save the plots
        output_dir (str): Output directory path
    """
    categorical_cols = data.select_dtypes(include=['object', 'category'])
    
    if target_var not in data.columns:
        print(f"Target variable {target_var} not in dataframe")
        return
    
    for col in categorical_cols:
        # Skip target variable
        if col != target_var:  
            plt.figure()
            sns.barplot(x=col, y=target_var, data=data, 
                        errorbar=None, palette='pastel')
            plt.title(f"Survival Rate by {col}")
            plt.ylabel("Survival Rate")
            plt.xticks(rotation=45)
            
            if save_plots:
                output_path = os.path.join(output_dir, f"survival_by_{col}.png")
                plt.savefig(output_path, bbox_inches='tight', dpi=300)
                print(f"Plot saved to {output_path}")
            plt.show()

# Calculate Cramér's V statistic for categorical-categorical association
def cramers_v(x, y):
    """    
    Args:
        x, y: Categorical variables (series or array-like)
    
    Returns:
        float: Cramér's V statistic (0-1)
    """
    confusion_matrix = pd.crosstab(x, y)
    try:
        chi2 = stats.chi2_contingency(confusion_matrix)[0]  
        n = confusion_matrix.sum().sum()
        phi2 = chi2/n
        r, k = confusion_matrix.shape
        return np.sqrt(phi2 / min((k-1), (r-1)))
    except:
        return 0  # Return 0 if calculation fails

# Calculate and plot Cramér's V correlation matrix
def plot_cramers_v_matrix(data, cat_cols=None, figsize=(10, 8), save_plot=True, output_dir="outputs"):
    """  
    Args:
        data (DataFrame): Input dataframe
        cat_cols (list): List of categorical columns to analyze
        figsize (tuple): Figure size
        save_plot (bool): Whether to save the plot
        output_dir (str): Output directory path
    """
    if cat_cols is None:
        cat_cols = data.select_dtypes(include=['object', 'category']).columns.tolist()
    
    results = pd.DataFrame(index=cat_cols, columns=cat_cols)
    
    for col1 in cat_cols:
        for col2 in cat_cols:
            results.loc[col1, col2] = cramers_v(data[col1], data[col2])
    
    plt.figure(figsize=figsize)
    sns.heatmap(results.astype(float), annot=True, 
                cmap="Blues", fmt=".3f")
    plt.title("Cramér's V Correlation Between Categorical Variables")
    
    if save_plot:
        output_path = os.path.join(output_dir, "cramers_v_matrix.png")
        plt.savefig(output_path, bbox_inches='tight', dpi=300)
        print(f"Plot saved to {output_path}")
    plt.show()
    
    return results

# Plot combined factor analysis
def plot_combined_factors(data, x_var, hue_var, target_var='survived', 
                            figsize=(10, 6), save_plot=True, output_dir="outputs"):
    """    
    Args:
        data (DataFrame): Input dataframe
        x_var (str): Variable for x-axis
        hue_var (str): Variable for hue grouping
        target_var (str): Target variable
        figsize (tuple): Figure size
        save_plot (bool): Whether to save the plot
        output_dir (str): Output directory path
    """
    plt.figure(figsize=figsize)
    sns.barplot(x=x_var, y=target_var, hue=hue_var, 
                data=data, errorbar=None)
    plt.title(f"Survival Rates by {x_var} and {hue_var}")
    plt.ylabel("Survival Rate")
    plt.xlabel(x_var)
    
    if save_plot:
        output_path = os.path.join(output_dir, f"combined_{x_var}_by_{hue_var}.png")
        plt.savefig(output_path, bbox_inches='tight', dpi=300)
        print(f"Plot saved to {output_path}")
    plt.show()