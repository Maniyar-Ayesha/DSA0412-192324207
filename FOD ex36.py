import pandas as pd
import matplotlib.pyplot as plt

# Load stock data
df = pd.read_csv('stock_data.csv', parse_dates=['Date'])
df.sort_values('Date', inplace=True)

# Basic stats
mean_price = df['Close'].mean()
std_dev = df['Close'].std()
max_price = df['Close'].max()
min_price = df['Close'].min()

print(f"📈 Stock Price Summary:")
print(f"Average Price: ₹{mean_price:.2f}")
print(f"Standard Deviation (Volatility): ₹{std_dev:.2f}")
print(f"Maximum Price: ₹{max_price:.2f}")
print(f"Minimum Price: ₹{min_price:.2f}")

# Moving average (7-day)
df['7-Day MA'] = df['Close'].rolling(window=7).mean()

# Plot closing price and moving average
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Close'], label='Closing Price', color='blue')
plt.plot(df['Date'], df['7-Day MA'], label='7-Day MA', color='orange', linestyle='--')
plt.title('Stock Price Trend and 7-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Daily returns and volatility
df['Daily Return'] = df['Close'].pct_change()
volatility = df['Daily Return'].std()

print(f"\n📉 Daily Return Volatility: {volatility:.4f} (as fraction)")

# Histogram of daily returns
plt.figure(figsize=(7, 4))
df['Daily Return'].hist(bins=20, color='green', edgecolor='black')
plt.title('Histogram of Daily Returns')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
