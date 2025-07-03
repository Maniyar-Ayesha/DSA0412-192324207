import pandas as pd
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords

# Download NLTK stopwords (run once)
nltk.download('stopwords')

# Sample customer reviews data
data = {
    'Review': [
        "Great product! Really loved it.",
        "Bad quality. Very disappointing.",
        "Excellent! Will buy again.",
        "Not worth the money.",
        "Good value for the price. Happy with the purchase."
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Combine all reviews into one text
all_reviews = ' '.join(df['Review']).lower()

# Remove punctuation using regex and tokenize
words = re.findall(r'\b\w+\b', all_reviews)

# Remove stopwords (like 'the', 'and', 'with', etc.)
filtered_words = [word for word in words if word not in stopwords.words('english')]

# Get word frequency using Counter
word_freq = Counter(filtered_words)

# Display top 10 most common words
print("Top 10 most frequent words in reviews:")
for word, freq in word_freq.most_common(10):
    print(f"{word}: {freq}")
