import pandas as pd

# Sample data
data = {
    'property_id': ['P101', 'P102', 'P103', 'P104', 'P105'],
    'location': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Chicago'],
    'bedrooms': [3, 5, 2, 6, 4],
    'area_sqft': [1200, 2500, 900, 3200, 1800],
    'listing_price': [500000, 750000, 350000, 650000, 480000]
}

# Create DataFrame
property_data = pd.DataFrame(data)

# 1. Average listing price of properties in each location
avg_price_per_location = property_data.groupby('location')['listing_price'].mean()

# 2. Number of properties with more than four bedrooms
num_properties_4plus = property_data[property_data['bedrooms'] > 4].shape[0]

# 3. Property with the largest area
property_largest_area = property_data.loc[property_data['area_sqft'].idxmax()]

# Display results
print("1. Average Listing Price by Location:")
print(avg_price_per_location)

print("\n2. Number of Properties with More Than 4 Bedrooms:")
print(num_properties_4plus)

print("\n3. Property with the Largest Area:")
print(property_largest_area)

