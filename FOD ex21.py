import pandas as pd
import numpy as np
from scipy import stats

# Load data
data = pd.read_csv('rare_elements.csv')
concentrations = data.iloc[:, 0]  # Assuming the data has only one column

# User inputs
sample_size = int(input("Enter sample size (n): "))
confidence_level = float(input("Enter confidence level (e.g., 0.95 for 95%): "))
precision = float(input("Enter desired precision (margin of error): "))

# Random sampling
if sample_size > len(concentrations):
    raise ValueError("Sample size cannot be greater than total available data.")
sample = concentrations.sample(sample_size, random_state=1)

# Point estimate (sample mean)
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)

# t-score for confidence interval
alpha = 1 - confidence_level
t_score = stats.t.ppf(1 - alpha/2, df=sample_size - 1)

# Margin of error and confidence interval
margin_error = t_score * (sample_std / np.sqrt(sample_size))
lower_bound = sample_mean - margin_error
upper_bound = sample_mean + margin_error

# Output results
print(f"\nSample Mean: {sample_mean:.4f}")
print(f"Sample Standard Deviation: {sample_std:.4f}")
print(f"{int(confidence_level * 100)}% Confidence Interval: ({lower_bound:.4f}, {upper_bound:.4f})")
print(f"Margin of Error: ±{margin_error:.4f}")

# Check precision requirement
if margin_error <= precision:
    print("✅ The desired precision is achieved.")
else:
    print("❌ The desired precision is NOT achieved. Consider increasing the sample size.")
