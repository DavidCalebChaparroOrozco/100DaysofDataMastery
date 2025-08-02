# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Apply visual style globally
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Ensure outputs directory exists
def _ensure_output_dir():
    os.makedirs("outputs", exist_ok=True)

# Plot histogram with KDE for a given column.
def plot_histogram(data, column, color="skyblue"):
    plt.figure()
    sns.histplot(data[column], bins=30, kde=True, color=color)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# Plot bar chart for categorical column.
def plot_bar(data, column, color_palette="Set2"):
    plt.figure()
    sns.countplot(data=data, x=column, palette=color_palette)
    plt.title(f"Count of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

# Plot boxplot for numeric vs category.
def plot_boxplot(data, x_column, y_column, color_palette="Set3"):
    plt.figure()
    sns.boxplot(data=data, x=x_column, y=y_column, palette=color_palette)
    plt.title(f"{y_column} by {x_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.tight_layout()
    plt.show()

# Plot scatter plot for two numeric variables with optional hue.
def plot_scatter(data, x_column, y_column, hue_column=None, color_palette="coolwarm"):
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
    plt.tight_layout()
    plt.show()

# Generate and save all four basic plots as a single image.
def save_combined_plots(data, output_path="outputs/eda_visualizations.png"):
    # Create a 3x2 grid (3 rows, 2 columns)
    fig, axes = plt.subplots(3, 2, figsize=(14, 10))

    # Plot 1: Top-left (row 0, column 0)
    sns.histplot(data["hours_viewed"], bins=30, kde=True, ax=axes[0,0], color="skyblue")
    axes[0,0].set_title("Distribution of Hours Viewed (millions)")

    # Plot 2: Top-right (row 0, column 1)
    sns.countplot(data=data, x="available_globally", ax=axes[0,1], palette="Set2")
    axes[0,1].set_title("Content Availability Globally")

    # Plot 3: Middle-left (row 1, column 0)
    sns.boxplot(data=data, x="available_globally", y="hours_viewed", ax=axes[1,0], palette="Set3")
    axes[1,0].set_title("Hours Viewed by Content Type")

    # Plot 4: Middle-right (row 1, column 1)
    sns.scatterplot(data=data, x="views", y="hours_viewed", hue="available_globally", ax=axes[1,1], palette="coolwarm")
    axes[1,1].set_title("Views vs Hours Viewed")

    # Plot 5: Bottom-left (row 2, column 0)
    numeric_cols = data.select_dtypes(include=['float64', 'int64'])
    sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', center=0, ax=axes[2,0])
    axes[2,0].set_title("Correlation Matrix")

    # Remove the empty subplot (row 2, column 1)
    fig.delaxes(axes[2,1])

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()