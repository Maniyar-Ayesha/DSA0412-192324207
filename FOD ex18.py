import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Data
age = [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61]
fat = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]

# Create DataFrame
df = pd.DataFrame({'Age': age, 'BodyFat': fat})

# ---- 1. Mean, Median, Std Deviation ----
print("Descriptive Statistics:\n")
print("Age")
print("Mean:", df['Age'].mean())
print("Median:", df['Age'].median())
print("Standard Deviation:", df['Age'].std())

print("\nBody Fat %")
print("Mean:", df['BodyFat'].mean())
print("Median:", df['BodyFat'].median())
print("Standard Deviation:", df['BodyFat'].std())

# ---- 2. Boxplots ----
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
sns.boxplot(y=df['Age'], color="lightblue")
plt.title("Boxplot of Age")

plt.subplot(1, 2, 2)
sns.boxplot(y=df['BodyFat'], color="lightgreen")
plt.title("Boxplot of Body Fat %")
plt.tight_layout()
plt.show()

# ---- 3. Scatter plot ----
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Age', y='BodyFat', data=df)
plt.title("Scatter Plot of Age vs Body Fat %")
plt.xlabel("Age")
plt.ylabel("Body Fat %")
plt.grid(True)
plt.tight_layout()
plt.show()

# ---- 4. Q-Q plots ----
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
stats.probplot(df['Age'], dist="norm", plot=plt)
plt.title("Q-Q Plot for Age")

plt.subplot(1, 2, 2)
stats.probplot(df['BodyFat'], dist="norm", plot=plt)
plt.title("Q-Q Plot for Body Fat %")
plt.tight_layout()
plt.show()
