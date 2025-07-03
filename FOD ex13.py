import os
import string
from collections import Counter

filename = "sample_text.txt"

# Create the file with sample text if not found
if not os.path.exists(filename):
    with open(filename, "w", encoding='utf-8') as f:
        f.write("Data science is a growing field. It uses techniques from machine learning, statistics, and programming.")

# Read and process the file
with open(filename, "r", encoding='utf-8') as file:
    text = file.read()

# Text processing
text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))
words = text.split()

# Word frequency
word_freq = Counter(words)

# Output
print("Top 10 most frequent words:\n")
for word, freq in word_freq.most_common(10):
    print(f"{word}: {freq}")

