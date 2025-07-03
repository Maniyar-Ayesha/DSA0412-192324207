import numpy as np
from scipy import stats

# Simulated conversion rates (replace with actual data)
np.random.seed(0)
design_A = np.random.binomial(1, p=0.10, size=500)  # 10% conversion
design_B = np.random.binomial(1, p=0.13, size=500)  # 13% conversion

# Calculate the means
mean_A = np.mean(design_A)
mean_B = np.mean(design_B)

# Perform two-sample t-test (independent samples)
t_stat, p_value = stats.ttest_ind(design_A, design_B)

# Output the results
print(f"Mean Conversion Rate - Design A: {mean_A:.3f}")
print(f"Mean Conversion Rate - Design B: {mean_B:.3f}")
print(f"T-statistic: {t_stat:.3f}")
print(f"P-value: {p_value:.4f}")

# Conclusion
alpha = 0.05
if p_value < alpha:
    print("✅ There is a statistically significant difference between the two designs.")
else:
    print("❌ No statistically significant difference was found between the two designs.")
