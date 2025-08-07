# Import necessary libraries
import math
from collections import Counter

# Function to calculate mean (average)
def calculate_mean(data):
    """
    Calculate the mean (average) of a list of numbers.
    Example: 
        Ages [20, 25, 30] -> mean = 25.0
    """
    return sum(data) / len(data)


# Function to calculate median (middle value)
def calculate_median(data):
    """
    Calculate the median of a list of numbers.
    If the list has an odd length, return the middle value.
    If even, return the average of the two middle values.
    Example: 
        Ages [22, 25, 30] -> median = 25
        Ages [20, 25, 30, 35] -> median = 27.5
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]


# Function to calculate mode (most frequent value)
def calculate_mode(data):
    """
    Calculate the mode (most frequent value) of a list.
    If multiple modes exist, return all of them in a list.
    Example: 
        Ages [20, 22, 22, 25, 30] -> mode = 22
    """
    freq = Counter(data)
    max_freq = max(freq.values())
    modes = [key for key, val in freq.items() if val == max_freq]

    return modes if len(modes) > 1 else modes[0]


# Function to calculate variance
def calculate_variance(data):
    """
    Calculate the variance of a list of numbers.
    Measures how spread out the data is.
    Example: 
        Ages [20, 25, 30] -> low variance
        Ages [10, 25, 40] -> higher variance
    """
    mean = calculate_mean(data)
    squared_diffs = [(x - mean) ** 2 for x in data]
    return sum(squared_diffs) / len(data)


# Function to calculate standard deviation
def calculate_std_dev(data):
    """
    Calculate the standard deviation of a list of numbers.
    It is the square root of the variance.
    Example: Standard deviation tells you how much ages deviate from the average.
    """
    return math.sqrt(calculate_variance(data))


# Function to calculate range
def calculate_range(data):
    """
    Calculate the range (max - min) of the data.
    Example: 
        Ages [20, 25, 30] -> range = 10
    """
    return max(data) - min(data)


# Function to summarize all stats
def summarize_statistics(data):
    """
    Print summary statistics of the dataset.
    """
    print("Summary Statistics:")
    print(f"Mean: {calculate_mean(data):.2f}")
    print(f"Median: {calculate_median(data)}")
    print(f"Mode: {calculate_mode(data)}")
    print(f"Variance: {calculate_variance(data):.2f}")
    print(f"Standard Deviation: {calculate_std_dev(data):.2f}")
    print(f"Range: {calculate_range(data)}")

ages = [20, 22, 22, 25, 30, 35, 40]
summarize_statistics(ages)