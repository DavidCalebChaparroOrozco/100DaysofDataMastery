# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, zscore, probplot
from math import comb

# Visualization settings
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Generate normally distributed data
def generate_normal_data(mean=170, std=10, size=1000, seed=None):
    np.random.seed(seed)
    return np.random.normal(loc=mean, scale=std, size=size)

# Generate sales data with optional outliers
def generate_sales_data(shape=2, scale=1000, size=200, outliers=None, seed=None):
    np.random.seed(seed)
    data = np.random.gamma(shape=shape, scale=scale, size=size)
    if outliers:
        data = np.append(data, outliers)
    return data

# Plot histogram with KDE curve
def plot_distribution(data, title="Distribution", xlabel="Value", ylabel="Frequency", color='skyblue'):
    plt.figure()
    sns.histplot(data, kde=True, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Create a Q-Q plot for normality check
def qq_plot(data, title="Q-Q Plot"):
    plt.figure()
    probplot(data, plot=plt)
    plt.title(title)
    plt.show()

# Detect outliers using Z-score method
def detect_outliers_zscore(data, threshold=3):
    z_scores = zscore(data)
    return np.where(np.abs(z_scores) > threshold)[0]

# Detect outliers using IQR method
def detect_outliers_iqr(data, multiplier=1.5):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - multiplier * iqr
    upper_bound = q3 + multiplier * iqr
    return np.where((data < lower_bound) | (data > upper_bound))[0]

# Create a boxplot for outlier visualization
def plot_boxplot(data, title="Boxplot", xlabel="", color='salmon'):
    plt.figure()
    sns.boxplot(x=data, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.show()

# Calculate binomial probability P(X=k)
def binomial_probability(n, k, p):
    return comb(n, k) * (p**k) * ((1-p)**(n-k))

# Calculate cumulative binomial probability P(k_min ≤ X ≤ k_max)
def binomial_cumulative(n, k_min, k_max, p):
    return sum(binomial_probability(n, k, p) for k in range(k_min, k_max+1))

# Plot binomial PMF
def plot_binomial(n, p, title="Binomial Distribution"):
    k_values = np.arange(0, n+1)
    pmf = [binomial_probability(n, k, p) for k in k_values]
    
    plt.bar(k_values, pmf, color='lightgreen', edgecolor='black')
    plt.xlabel("Number of Successes")
    plt.ylabel("Probability")
    plt.title(f"{title} (n={n}, p={p:.2f})")
    plt.show()

# Plot normal PDF
def plot_normal(mu, sigma, x_range=None, title="Normal Distribution"):
    if x_range is None:
        x_range = (mu - 4*sigma, mu + 4*sigma)
    x = np.linspace(x_range[0], x_range[1], 200)
    y = norm.pdf(x, mu, sigma)
    
    plt.plot(x, y, 'r-')
    plt.xlabel("X")
    plt.ylabel("Density")
    plt.title(f"{title} (μ={mu}, σ={sigma})")
    plt.show()

# Demonstrate Central Limit Theorem
def clt_demo(population, sample_size, n_samples=1000, title="CLT Demonstration"):
    sample_means = [np.mean(np.random.choice(population, sample_size)) for _ in range(n_samples)]
    
    plt.hist(sample_means, bins=30, density=True, alpha=0.6, color='g', label='Sample Means')
    
    pop_mean = np.mean(population)
    pop_std = np.std(population)/np.sqrt(sample_size)
    x = np.linspace(pop_mean - 3*pop_std, pop_mean + 3*pop_std, 100)
    plt.plot(x, norm.pdf(x, pop_mean, pop_std), 'r-', label='Normal Distribution')
    
    plt.title(f"{title}\nSample Size = {sample_size}")
    plt.xlabel("Sample Mean")
    plt.ylabel("Density")
    plt.legend()
    plt.show()

# Save dataset to CSV
def save_dataset(data, filename, column_name="value"):
    df = pd.DataFrame({column_name: data})
    df.to_csv(filename, index=False)
    return df

# Load dataset from CSV
def load_dataset(filename):
    return pd.read_csv(filename)