# Import necessary libraries
import numpy as np
import pandas as pd
import random
from math import comb
from scipy.stats import bernoulli, binom, norm

# Data generation utilities

# Simulate coin tosses and return a pandas DataFrame.
def generate_coin_tosses(n_tosses=500, seed=None):
    """    
    Parameters:
        n_tosses (int): Number of tosses to simulate.
        seed (int or None): Optional random seed for reproducibility.
    
    Returns:
        pd.DataFrame: Columns ['toss_number', 'results'] with 'Heads' or 'Tails'.
    """
    if seed is not None:
        random.seed(seed)
    results = [random.choice(["Heads", "Tails"]) for _ in range(n_tosses)]
    return pd.DataFrame({"toss_number": range(1, n_tosses + 1), "results": results})


# Simulate dice rolls and return a pandas DataFrame.
def generate_dice_rolls(n_rolls=500, sides=6, seed=None):
    """
    Parameters:
        n_rolls (int): Number of rolls to simulate.
        sides (int): Number of sides on the die.
        seed (int or None): Optional random seed for reproducibility.
    
    Returns:
        pd.DataFrame: Columns ['roll_number', 'results'].
    """
    if seed is not None:
        random.seed(seed)
    results = [random.randint(1, sides) for _ in range(n_rolls)]
    return pd.DataFrame({"roll_number": range(1, n_rolls + 1), "results": results})


# Simulate a dataset of events with associated probabilities.
def generate_events_dataset(n_events=500, event_types=None, seed=None):
    """
    Parameters:
        n_events (int): Number of events to generate.
        event_types (list[str] or None): List of event categories.
        seed (int or None): Optional random seed.
    
    Returns:
        pd.DataFrame: Columns ['event_id', 'event_type', 'probability'].
    """
    if event_types is None:
        event_types = ["Rain", "Sunny", "Cloudy", "Snow", "Storm"]
    if seed is not None:
        random.seed(seed)
    event_type_list = [random.choice(event_types) for _ in range(n_events)]
    probabilities = [round(random.uniform(0, 1), 2) for _ in range(n_events)]
    return pd.DataFrame({
        "event_id": range(1, n_events + 1),
        "event_type": event_type_list,
        "probability": probabilities
    })


# Probability calculations

# Calculate the empirical probability given a boolean array/Series.
def empirical_probability(condition):
    """    
    Parameters:
        condition (array-like): Boolean mask indicating favorable outcomes.
    
    Returns:
        float: Empirical probability.
    """
    return np.mean(condition)


# Return the probability of not A given P(A).
def complement_rule(p_a):
    return 1 - p_a


# Return P(A ∪ B) using the addition rule.
def addition_rule(p_a, p_b, p_a_and_b):
    return p_a + p_b - p_a_and_b


# Calculate P(A|B).
def conditional_probability(p_a_and_b, p_b):
    """
    Returns:
        NaN if P(B) is zero.
    """
    return p_a_and_b / p_b if p_b > 0 else float("nan")


# Apply Bayes' theorem to compute P(A|B).
def bayes_theorem(p_b_given_a, p_a, p_b):
    return (p_b_given_a * p_a) / p_b if p_b > 0 else float("nan")


# Random variables and statistics

# Compute the probability mass function (PMF) from observed data.
def pmf_from_data(values):
    return pd.Series(values).value_counts(normalize=True).sort_index()


# Compute the expected value given a PMF.
def expected_value(pmf):
    return sum(x * p for x, p in pmf.items())


# Compute the variance given a PMF.
def variance(pmf):
    e_x = expected_value(pmf)
    e_x2 = sum((x**2) * p for x, p in pmf.items())
    return e_x2 - e_x**2


# Distribution helpers

# Return the PMF of a Bernoulli(p) distribution.
def bernoulli_pmf(p):
    return bernoulli.pmf([0, 1], p)


# Return the PMF values for k = 0..n of a Binomial(n, p).
def binomial_pmf(n, p):
    k_values = np.arange(0, n + 1)
    return binom.pmf(k_values, n, p)


# Return the PDF of a Normal(mu, sigma) at given x values.
def normal_pdf(x, mu, sigma):
    return norm.pdf(x, mu, sigma)


# Return the CDF of a Normal(mu, sigma) at value x.
def normal_cdf(x, mu, sigma):
    return norm.cdf(x, mu, sigma)


# Combinatorics

# Calculate P(X = k) for a Binomial(n, p) distribution using the formula:
# C(n, k) * p^k * (1-p)^(n-k)
def binomial_probability(n, k, p):
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
