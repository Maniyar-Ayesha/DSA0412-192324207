import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import nltk
import re
import string
from nltk.corpus import stopwords

# Download stopwords from NLTK (run only once)
nltk.download('stopwords')

# Load dataset from CSV file
try:
    df = pd.read_csv('data.csv')

    # Ensure 'feedback' column exists
    if 'feedback' not in df.columns:
        raise ValueError("CSV file must contain a 'feedback' column.")
except Exception as e:
    print(f"Error loading file: {e}")
    exit()

# Combine all feedback into one string
all_feedback = ' '.join(df['feedback'].dropna()).lower()

# Remove punctuation and tokenize
all_feedback = re.sub(f"[{re.escape(string.punctuation)}]", "", all_feedback)
words = all_feedback.split()

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

# Count word frequencies
word_freq = Counter(filtered_words)

# Ask user how many top words to display
try:
    N = int(input("Enter the number of top frequent words to display: "))
except ValueError:
    print("Invalid input. Please enter a numeric value.")
    exit()

# Get top N words
top_words = word_freq.most_common(N)

# Display results
print(f"\nTop {N} Most Frequent Words:")
for word, freq in top_words:
    print(f"{word}: {freq}")

# Plotting
words, freqs = zip(*top_words)
plt.figure(figsize=(10, 6))
plt.bar(words, freqs, color='skyblue')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title(f'Top {N} Most Frequent Words in Customer Feedback')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
