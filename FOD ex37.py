import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Load the data
df = pd.read_csv('student_scores.csv')

# Display basic statistics
print("📈 Descriptive Statistics:")
print(df.describe())

# Calculate Pearson correlation
corr, p_value = pearsonr(df['study_time'], df['exam_score'])
print(f"\n🔗 Pearson Correlation: {corr:.2f}")
print(f"P-value: {p_value:.4f}")

# Scatter plot with regression line
plt.figure(figsize=(8, 5))
sns.regplot(x='study_time', y='exam_score', data=df, color='blue', line_kws={"color": "red"})
plt.title('Study Time vs Exam Score')
plt.xlabel('Study Time (hours)')
plt.ylabel('Exam Score')
plt.grid(True)
plt.tight_layout()
plt.show()

# Line plot
plt.figure(figsize=(8, 5))
plt.plot(df['study_time'], df['exam_score'], marker='o', linestyle='-', color='green')
plt.title('Line Plot: Study Time vs Exam Score')
plt.xlabel('Study Time (hours)')
plt.ylabel('Exam Score')
plt.grid(True)
plt.tight_layout()
plt.show()

# Heatmap of correlation matrix
plt.figure(figsize=(5, 4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()
