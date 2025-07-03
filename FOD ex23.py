import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Example data — replace with actual CSV data if available
# You can also load data from CSV like: pd.read_csv("clinical_trial.csv")
control_group = np.array([120, 122, 121, 119, 123, 118, 117, 124, 122, 121])
treatment_group = np.array([110, 108, 109, 107, 111, 106, 105, 112, 110, 109])

# Perform independent two-sample t-test
t_stat, p_value = ttest_ind(treatment_group, control_group)

# Print results
print("Control Group Mean:", np.mean(control_group))
print("Treatment Group Mean:", np.mean(treatment_group))
print(f"\n🔍 T-Statistic: {t_stat:.3f}")
print(f"📊 P-Value: {p_value:.4f}")

# Determine significance
alpha = 0.05
if p_value < alpha:
    print("✅ The result is statistically significant (reject null hypothesis).")
else:
    print("❌ The result is NOT statistically significant (fail to reject null hypothesis).")

# Visualization
plt.figure(figsize=(10, 5))
plt.hist(control_group, alpha=0.6, label="Control Group", color='skyblue', bins=7)
plt.hist(treatment_group, alpha=0.6, label="Treatment Group", color='salmon', bins=7)
plt.axvline(np.mean(control_group), color='blue', linestyle='dashed', linewidth=2)
plt.axvline(np.mean(treatment_group), color='red', linestyle='dashed', linewidth=2)
plt.title(f"Comparison of Blood Pressure Reduction\nP-value = {p_value:.4f}")
plt.xlabel("Blood Pressure")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
