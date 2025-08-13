# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Generate and save all datasets needed for hypothesis testin
def generate_datasets():
    np.random.seed(42)
    
    # Heights dataset
    heights_male = np.random.normal(loc=175, scale=7, size=200)
    heights_female = np.random.normal(loc=162, scale=6, size=200)
    heights_data = pd.DataFrame({
        'height': np.concatenate([heights_male, heights_female]),
        'gender': ['male']*200 + ['female']*200
    })
    
    # Sales dataset
    sales_before = np.random.normal(loc=500, scale=50, size=100)
    sales_after = sales_before + np.random.normal(loc=30, scale=20, size=100)
    sales_data = pd.DataFrame({
        'before': sales_before,
        'after': sales_after
    })
    
    # Contingency table
    contingency_data = pd.DataFrame({
        'Product': ['A','B','C','D'],
        'NY': [150, 70, 60, 120],
        'CA': [100, 90, 110, 95],
        'TX': [130, 80, 70, 140]
    })
    
    return heights_data, sales_data, contingency_data

# Plot distribution with KD
def plot_distribution(data, x, hue=None, title="", filename=""):
    plt.figure()
    sns.histplot(data=data, x=x, hue=hue, kde=True, bins=20)
    plt.title(title)
    if filename:
        plt.savefig(f'outputs/{filename}')
    plt.show()

# Perform z-test and return results with visualizatio
def perform_ztest(sample, pop_mean, pop_std):
    z_score = (np.mean(sample) - pop_mean) / (pop_std / np.sqrt(len(sample)))
    p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
    
    plt.figure()
    x = np.linspace(pop_mean - 4*pop_std, pop_mean + 4*pop_std, 100)
    y = stats.norm.pdf(x, loc=pop_mean, scale=pop_std)
    plt.plot(x, y, label='Population Distribution')
    plt.axvline(np.mean(sample), color='red', linestyle='--', 
                label=f'Sample Mean: {np.mean(sample):.2f}')
    plt.axvline(pop_mean, color='green', linestyle='-', 
                label=f'Population Mean: {pop_mean}')
    plt.title('Z-Test: Sample vs Population')
    plt.legend()
    plt.show()
    
    return z_score, p_value

# Perform t-test (independent or paired) with visualizatio
def perform_ttest(group1, group2, paired=False):
    if paired:
        t_stat, p_value = stats.ttest_rel(group1, group2)
        plt.figure()
        plt.plot([1]*len(group1), group1, 'bo', label='Group 1', alpha=0.5)
        plt.plot([2]*len(group2), group2, 'ro', label='Group 2', alpha=0.5)
        for i in range(len(group1)):
            plt.plot([1, 2], [group1[i], group2[i]], 'gray', alpha=0.1)
        plt.xlim(0.5, 2.5)
        plt.xticks([1, 2], ['Group 1', 'Group 2'])
        plt.title('Paired T-Test Visualization')
    else:
        t_stat, p_value = stats.ttest_ind(group1, group2)
        plt.figure()
        sns.boxplot(data=pd.DataFrame({
            'values': np.concatenate([group1, group2]),
            'groups': ['Group 1']*len(group1) + ['Group 2']*len(group2)
        }), x='groups', y='values')
        plt.title('Independent T-Test Visualization')
    
    plt.legend()
    plt.show()
    return t_stat, p_value

# Perform chi-squared test with visualizatio
def perform_chi2_test(contingency_table):
    # Extract numeric values for the test 
    observed_values = contingency_table.iloc[:, 1:].values

    # Perform Chi-Squared test
    chi2, p, dof, expected = stats.chi2_contingency(observed_values)

    # Build DataFrames
    observed_df = contingency_table.set_index(contingency_table.columns[0])
    expected_df = pd.DataFrame(
        expected,
        index=contingency_table.iloc[:, 0],
        columns=contingency_table.columns[1:]
    )
    difference_df = observed_df - expected_df

    # Melt DataFrames for seaborn
    obs_melted = observed_df.reset_index().melt(id_vars='Product', var_name='State', value_name='Count')
    exp_melted = expected_df.reset_index().melt(id_vars='Product', var_name='State', value_name='Count')
    diff_melted = difference_df.reset_index().melt(id_vars='Product', var_name='State', value_name='Count')

    # Plot
    fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

    sns.barplot(data=obs_melted, x='Product', y='Count', hue='State', ax=axes[0])
    axes[0].set_title('Observed Frequencies')

    sns.barplot(data=exp_melted, x='Product', y='Count', hue='State', ax=axes[1])
    axes[1].set_title('Expected Frequencies')

    sns.barplot(data=diff_melted, x='Product', y='Count', hue='State', ax=axes[2])
    axes[2].set_title('Difference (Observed - Expected)')

    fig.suptitle('Chi-Squared Test: Observed vs Expected vs Difference', fontsize=16)
    plt.tight_layout()
    plt.show()

    return chi2, p, dof, expected

# Helper function to save plot
def save_plot(title, filename):
    plt.title(title)
    plt.savefig(f'outputs/{filename}')
    plt.close()