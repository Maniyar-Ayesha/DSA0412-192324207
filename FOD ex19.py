import numpy as np
import scipy.stats as stats

# Simulated data (replace with actual trial data)
np.random.seed(42)  # For reproducibility

# Blood pressure reductions
drug_group = np.random.normal(loc=12, scale=5, size=25)      # New drug group
placebo_group = np.random.normal(loc=4, scale=3, size=25)    # Placebo group

# Function to compute 95% confidence interval
def compute_confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    std_err = stats.sem(data)  # Standard error of the mean
    margin = std_err * stats.t.ppf((1 + confidence) / 2, df=n-1)
    return mean, mean - margin, mean + margin

# Calculate CIs
drug_mean, drug_lower, drug_upper = compute_confidence_interval(drug_group)
placebo_mean, placebo_lower, placebo_upper = compute_confidence_interval(placebo_group)

# Print Results
print(f"New Drug Group:")
print(f"Mean Reduction: {drug_mean:.2f} mmHg")
print(f"95% Confidence Interval: ({drug_lower:.2f}, {drug_upper:.2f}) mmHg\n")

print(f"Placebo Group:")
print(f"Mean Reduction: {placebo_mean:.2f} mmHg")
print(f"95% Confidence Interval: ({placebo_lower:.2f}, {placebo_upper:.2f}) mmHg")
