import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset: post IDs and number of likes
data = {
    'PostID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Likes': [10, 15, 10, 20, 15, 10, 25, 20, 10, 15]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Frequency distribution of likes
like_distribution = df['Likes'].value_counts().sort_index()
print("Frequency distribution of likes among posts:\n")
print(like_distribution)

# Optional: Plotting (save as image if Tkinter issues)
import matplotlib
matplotlib.use('Agg')  # Use this to avoid GUI issues

plt.figure(figsize=(8, 5))
like_distribution.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Frequency Distribution of Likes')
plt.xlabel('Number of Likes')
plt.ylabel('Number of Posts')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('like_distribution.png')

print("Plot saved as 'like_distribution.png'")
