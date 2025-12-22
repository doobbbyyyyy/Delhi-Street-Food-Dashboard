import pandas as pd
import numpy as np

# Load your file
df = pd.read_csv(r'C:\Users\rohit\Downloads\DelhiNCR Restaurants.csv')

# PERFECT STREET FOOD FILTER for YOUR dataset
street_keywords = ['Street Food', 'Chaat', 'Momo', 'Rolls', 'Fast Food', 'Snack']
df_street = df[df['Category'].str.contains('|'.join(street_keywords), case=False, na=False)]

# Backup: Cheap eats proxy (<₹500 = street food)
df_cheap = df[df['Pricing_for_2'] < 500].copy()

print(f"🎉 Street food by Category: {len(df_street)} vendors")
print(f"💰 Cheap street proxies: {len(df_cheap)} vendors")
print("\n📍 TOP 10 Street Food Hotspots:")
print(df_street['Locality'].value_counts().head(10))
print("\n⭐ BEST Street Food Spots (Top 5 by Dining_Rating):")
print(df_street.nlargest(5, 'Dining_Rating')[['Restaurant_Name', 'Locality', 'Dining_Rating', 'Pricing_for_2', 'Category']])

print("\n💎 Chandni Chowk Street Food Preview:")
chandni = df_street[df_street['Locality'].str.contains('Chandni|Chowk', case=False, na=False)]
print(chandni[['Restaurant_Name', 'Dining_Rating', 'Pricing_for_2']])
