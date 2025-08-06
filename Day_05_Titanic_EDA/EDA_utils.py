# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os
from typing import List, Dict, Optional
from sklearn.preprocessing import MinMaxScaler

# Apply visual style globally
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Ensure 'outputs' directory exists for saving plots
os.makedirs('outputs', exist_ok=True)

# Plot and save a histogram with KDE for a specified column.
def plot_histogram(data, column, filename='histogram.png', color="skyblue" ,**kwargs):
    """    
    Args:
        data: DataFrame containing the data
        column: Name of column to plot
        filename: Output filename (default: 'histogram.png')
        **kwargs: Additional arguments passed to sns.histplot()
    """
    plt.figure(figsize=(8, 6))
    sns.histplot(data[column], bins=30,kde=True, color=color,**kwargs)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.savefig(f'outputs/{filename}')
    plt.tight_layout()
    plt.show()
    plt.close()

# Plot and save a bar chart for a categorical column.
def plot_bar(data, column, color_palette="Set2"):
    """
    Args:
        data: DataFrame containing the data
        column: Name of categorical column to plot
        color_palette: Color palette to use (default: "Set2")
    """
    plt.figure()
    sns.countplot(data=data, x=column, palette=color_palette)
    plt.title(f"Count of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.savefig(f'outputs/plot_bar_{column}')
    plt.tight_layout()
    plt.show()

# Plot and save a scatter plot for two numeric variables with optional hue.
def plot_scatter(data, x_column, y_column, hue_column=None, color_palette="coolwarm"):
    """
    Args:
        data: DataFrame containing the data
        x_column: Name of column for x-axis
        y_column: Name of column for y-axis
        hue_column: Name of column for color grouping (optional)
        color_palette: Color palette to use (default: "coolwarm")
    """
    plt.figure()
    sns.scatterplot(
        data=data,
        x=x_column,
        y=y_column,
        hue=hue_column,
        palette=color_palette
    )
    plt.title(f"{y_column} vs {x_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    if hue_column:
        plt.legend(title=hue_column)
    plt.savefig(f'outputs/plot_scatter_{x_column}_{y_column}')
    plt.tight_layout()
    plt.show()

# Create and save a violin plot showing distribution of y by x.
def plot_violin(data, x, y, filename='violin_plot.png', **kwargs):
    """    
    Args:
        data: DataFrame containing the data
        x: Categorical variable for x-axis
        y: Numerical variable for y-axis
        filename: Output filename (default: 'violin_plot.png')
        **kwargs: Additional arguments passed to sns.violinplot()
    """
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=data, x=x, y=y, **kwargs)
    plt.title(f'Violin plot of {y} by {x}')
    plt.savefig(f'outputs/{filename}')
    plt.tight_layout()
    plt.show()
    plt.close()

# Generate and save a boxplot showing y distribution by x categories.
def plot_boxplot(data, x, y, color="Set3",filename='boxplot.png', **kwargs):
    """    
    Args:
        data: DataFrame containing the data
        x: Categorical variable for x-axis
        y: Numerical variable for y-axis
        filename: Output filename (default: 'boxplot.png')
        **kwargs: Additional arguments passed to sns.boxplot()
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, x=x, y=y, palette=color, **kwargs)
    plt.title(f'Boxplot of {y} by {x}')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.savefig(f'outputs/{filename}')
    plt.tight_layout()
    plt.show()
    plt.close()

# Create and save a swarm plot showing individual data points by category.
def plot_swarm(data, x, y, filename='swarmplot.png', **kwargs):
    """    
    Args:
        data: DataFrame containing the data
        x: Categorical variable for x-axis
        y: Numerical variable for y-axis
        filename: Output filename (default: 'swarmplot.png')
        **kwargs: Additional arguments passed to sns.swarmplot()
    """
    plt.figure(figsize=(10, 6))
    sns.swarmplot(data=data, x=x, y=y, **kwargs)
    plt.title(f'Swarm plot of {y} by {x}')
    plt.savefig(f'outputs/{filename}')
    plt.tight_layout()
    plt.show()
    plt.close()

# Plot and save a Kernel Density Estimate (KDE) for a numerical variable.
def plot_kde(data, x, filename='kdeplot.png', **kwargs):
    """
    Args:
        data: DataFrame containing the data
        x: Numerical variable to plot
        filename: Output filename (default: 'kdeplot.png')
        **kwargs: Additional arguments passed to sns.kdeplot()
    """
    plt.figure(figsize=(8, 6))
    sns.kdeplot(data=data, x=x, **kwargs)
    plt.title(f'KDE plot of {x}')
    plt.savefig(f'outputs/{filename}')
    plt.tight_layout()
    plt.show()
    plt.close()

# Create and save a bar plot showing mean values by category.
def plot_bar_mean_by_category(data, category, value, filename='barplot_mean.png', **kwargs):
    """    
    Args:
        data: DataFrame containing the data
        category: Categorical grouping variable
        value: Numerical variable to calculate means
        filename: Output filename (default: 'barplot_mean.png')
        **kwargs: Additional arguments passed to sns.barplot()
    """
    plt.figure(figsize=(10, 6))
    mean_values = data.groupby(category)[value].mean().sort_values()
    sns.barplot(x=mean_values.index, y=mean_values.values, **kwargs)
    plt.title(f'Mean {value} by {category}')
    plt.xlabel(category)
    plt.ylabel(f'Mean {value}')
    plt.xticks(rotation=45)
    plt.savefig(f'outputs/{filename}')
    plt.tight_layout()
    plt.show()
    plt.close()

# Generate and save a jointplot with regression line showing relationship between two variables.
def plot_jointplot(data, x, y, filename='jointplot.png', **kwargs):
    """    
    Args:
        data: DataFrame containing the data
        x: First numerical variable
        y: Second numerical variable
        filename: Output filename (default: 'jointplot.png')
        **kwargs: Additional arguments passed to sns.jointplot()
    """
    jp = sns.jointplot(data=data, x=x, y=y, kind='reg', **kwargs)
    jp.fig.suptitle(f'Jointplot of {x} and {y}', y=1.02)
    jp.savefig(f'outputs/{filename}')
    plt.tight_layout()
    plt.show()
    plt.close()

# Create and save a heatmap showing frequency counts between two categorical variables.
def plot_heatmap_category_combinations(data, cat1, cat2, filename='heatmap.png', **kwargs):
    """
    Args:
        data: DataFrame containing the data
        cat1: First categorical variable
        cat2: Second categorical variable
        filename: Output filename (default: 'heatmap.png')
        **kwargs: Additional arguments passed to sns.heatmap()
    """
    heatmap_data = pd.crosstab(data[cat1], data[cat2])
    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlGnBu', **kwargs)
    plt.title(f'Heatmap of {cat1} vs {cat2}')
    plt.savefig(f'outputs/{filename}')
    plt.tight_layout()
    plt.show()
    plt.close()

# Create and save a radar chart comparing normalized means of multiple variables by category.
def plot_radar_chart_by_category_means(data, category, variables, filename='radar_chart.png'):
    """  
    Args:
        data: DataFrame containing the data
        category: Categorical variable for grouping
        variables: List of numerical variables to compare
        filename: Output filename (default: 'radar_chart.png')
    """
    # Calculate means per category
    mean_df = data.groupby(category)[variables].mean()

    # Normalize the values (0-1 range)
    scaler = MinMaxScaler()
    norm_data = scaler.fit_transform(mean_df)
    norm_df = pd.DataFrame(norm_data, columns=variables, index=mean_df.index)

    # Create radar chart coordinates
    num_vars = len(variables)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    # Close the loop
    angles += angles[:1]  

    plt.figure(figsize=(8, 8))
    for index in norm_df.index:
        values = norm_df.loc[index].tolist()
        # Close the loop
        values += values[:1]  
        plt.polar(angles, values, label=index)
    
    plt.xticks(angles[:-1], variables)
    plt.title(f'Radar Chart of Normalized Means by {category}')
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.tight_layout()
    plt.savefig(f'outputs/{filename}')
    plt.tight_layout()
    plt.show()
    plt.close()

# Generate and save multiple plots combined in a single image with customizable grid layout.
def save_combined_plots(
    data,
    plot_configs: List[Dict],
    grid_size: tuple = (3, 2),
    figsize: tuple = (14, 10),
    output_path: str = "outputs/EDA_visualizations.png",
    remove_empty: bool = True,
    tight_layout: bool = True
):
    """
    Args:
        data: DataFrame containing the data to visualize
        plot_configs: List of dictionaries with plot configurations
        grid_size: Grid dimensions (rows, columns) (default: (3, 2))
        figsize: Figure size in inches (default: (14, 10))
        output_path: Output file path (default: "outputs/EDA_visualizations.png")
        remove_empty: Whether to remove empty subplots (default: True)
        tight_layout: Whether to apply tight layout (default: True)
        
    Each plot config dictionary should contain:
        - 'plot_type': Type of plot (histplot, countplot, boxplot, etc.)
        - 'position': Grid position (row, column) for the plot
        - 'params': Parameters for the seaborn plotting function
        - 'title': Plot title (optional)
    """
    
    # Create the subplot grid with specified dimensions.
    fig, axes = plt.subplots(*grid_size, figsize=figsize)
    
    # Generate each plot according to its configuration.
    for config in plot_configs:
        row, col = config['position']
        plot_type = config['plot_type']
        # Create a copy to avoid modifying original
        params = config.get('params', {}).copy()  
        title = config.get('title', '')
        
        # Get the correct axis object based on grid dimensions.
        ax = axes[row, col] if grid_size[0] > 1 and grid_size[1] > 1 else axes[col] if grid_size[0] == 1 else axes[row]
        
        # For heatmap, we need special handling of data parameter
        if plot_type == 'heatmap':
            # Use specific data if provided, else use main data
            heatmap_data = params.pop('data', data)  
            sns.heatmap(data=heatmap_data, ax=ax, **params)
        else:
            # Create the specified plot type with given parameters.
            if plot_type == 'histplot':
                sns.histplot(data=data, ax=ax, **params)
            elif plot_type == 'countplot':
                sns.countplot(data=data, ax=ax, **params)
            elif plot_type == 'boxplot':
                sns.boxplot(data=data, ax=ax, **params)
            elif plot_type == 'scatterplot':
                sns.scatterplot(data=data, ax=ax, **params)
            elif plot_type == 'barplot':
                sns.barplot(data=data, ax=ax, **params)
            elif plot_type == 'lineplot':
                sns.lineplot(data=data, ax=ax, **params)
            # Add more plot types here as needed
        
        # Set plot title if specified.
        if title:
            ax.set_title(title)
    
    # Remove unused subplots if enabled.
    if remove_empty:
        total_plots = grid_size[0] * grid_size[1]
        used_positions = {config['position'] for config in plot_configs}
        
        for row in range(grid_size[0]):
            for col in range(grid_size[1]):
                if (row, col) not in used_positions:
                    if grid_size[0] > 1 and grid_size[1] > 1:
                        fig.delaxes(axes[row, col])
                    elif grid_size[0] == 1:
                        fig.delaxes(axes[col])
                    else:
                        fig.delaxes(axes[row])
    
    # Apply tight layout if enabled.
    if tight_layout:
        plt.tight_layout()
    
    # Save the figure and close the plot.
    plt.savefig(output_path)
    plt.close()