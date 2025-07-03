import pandas as pd

# Load the dataset
df = pd.read_csv('city_temperatures.csv')

# Group by city
grouped = df.groupby('City')

# 1. Mean temperature for each city
mean_temp = grouped['Temperature'].mean()
print("📊 Mean Temperature for Each City:\n", mean_temp)

# 2. Standard deviation of temperature for each city
std_temp = grouped['Temperature'].std()
print("\n📉 Standard Deviation for Each City:\n", std_temp)

# 3. Temperature range (max - min) for each city
temp_range = grouped['Temperature'].max() - grouped['Temperature'].min()
print("\n🌡️ Temperature Range for Each City:\n", temp_range)

# 4. City with highest temperature range
city_max_range = temp_range.idxmax()
print(f"\n🔥 City with Highest Temperature Range: {city_max_range} ({temp_range[city_max_range]:.2f}°C)")

# 5. City with most consistent temperature (lowest std dev)
city_min_std = std_temp.idxmin()
print(f"❄️ City with Most Consistent Temperature: {city_min_std} (SD = {std_temp[city_min_std]:.2f}°C)")
