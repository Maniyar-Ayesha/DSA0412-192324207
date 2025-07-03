import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv('soccer_players.csv')

# Top 5 players by goals
top_goals = df.sort_values(by='Goals', ascending=False).head(5)
print("⚽ Top 5 Players with Highest Goals:\n", top_goals[['Name', 'Goals']], "\n")

# Top 5 players by salary
top_salary = df.sort_values(by='Salary', ascending=False).head(5)
print("💰 Top 5 Players with Highest Salaries:\n", top_salary[['Name', 'Salary']], "\n")

# Average age
average_age = df['Age'].mean()
print(f"📊 Average Age of Players: {average_age:.2f} years\n")

# Players above average age
above_avg_age = df[df['Age'] > average_age]
print("🧓 Players Older than Average Age:\n", above_avg_age[['Name', 'Age']], "\n")

# Visualization: Distribution of players based on position
position_counts = df['Position'].value_counts()

plt.figure(figsize=(8, 5))
position_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Distribution of Players by Position')
plt.xlabel('Position')
plt.ylabel('Number of Players')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y')
plt.show()
