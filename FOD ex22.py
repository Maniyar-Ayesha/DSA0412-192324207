import pandas as pd
import numpy as np
from scipy import stats

# Load the data
df = pd.read_csv("customer_reviews.csv")

# Preview the data
print("First 5 records:\n", df.head())

# Assuming the column containing ratings is named 'rating'
ratings = df['rating'].dropna()

# Basic statistics
mean_rating = np.mean(ratings)
std_dev = np.std(ratings, ddof=1)  # sample standard deviation
n = len(ratings)

# Confidence Level
confidence_level = 0.95
alpha = 1 - confidence_level

# Calculate the margin of error
t_score = stats.t.ppf(1 - alpha/2, df=n-1)
margin_of_error = t_score * (std_dev / np.sqrt(n))

# Confidence Interval
ci_lower = mean_rating - margin_of_error
ci_upper = mean_rating + margin_of_error

# Results
print(f"\n📊 Mean Rating: {mean_rating:.2f}")
print(f"✅ 95% Confidence Interval for the Mean Rating: ({ci_lower:.2f}, {ci_upper:.2f})")

# Optional: Customer satisfaction insight
if mean_rating >= 4:
    print("🙂 Customers are generally satisfied.")
elif mean_rating >= 3:
    print("😐 Mixed feedback from customers.")
else:
    print("☹️ Customers are generally dissatisfied.")
