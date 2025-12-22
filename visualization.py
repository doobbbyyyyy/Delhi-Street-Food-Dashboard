import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# STEP 1: LOAD
print("🔄 Loading Delhi Street Food data...")
df = pd.read_csv(r'C:\Users\rohit\Downloads\DelhiNCR Restaurants.csv')

# 2. BROADER STREET FOOD SEARCH (case-insensitive, partial matches)
street_keywords = ['street', 'chaat', 'momo', 'rolls', 'fast', 'snack', 'kulfi']
mask = df['Category'].str.contains('|'.join(street_keywords), case=False, na=False)
df_street = df[mask].copy()
print(f"✅ Found {len(df_street)} street food vendors!")

# 3. FALLBACK: CHEAP FOOD (<₹500)
df_cheap = df[df['Pricing_for_2'] < 500].copy()
print(f"💰 Cheap eats: {len(df_cheap)}")

# USE WHICHEVER IS BIGGER
if len(df_street) == 0:
    df_street = df_cheap
    print("🔄 Using cheap eats as street food proxy")

# 4. VISUAL 1: TOP HOTSPOTS
plt.figure(figsize=(12, 6))
top_areas = df_street['Locality'].value_counts().head(10)
plt.bar(range(len(top_areas)), top_areas.values, color='orange', edgecolor='darkred')
plt.title('🔥 TOP 10 Street Food Hotspots', fontsize=16, fontweight='bold')
plt.xlabel('Neighborhoods')
plt.ylabel('Number of Vendors')
plt.xticks(range(len(top_areas)), top_areas.index, rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 5. VISUAL 2: PRICE vs RATING
plt.figure(figsize=(10, 6))
plt.scatter(df_street['Pricing_for_2'], df_street['Dining_Rating'], alpha=0.7, s=80, color='green')
plt.xlabel('Price for 2 (₹)')
plt.ylabel('Rating (⭐)')
plt.title('💰 Street Food Trends')
plt.axvline(x=500, color='red', linestyle='--', label='Budget Line')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 6. INSIGHTS
print("\n🏆 KEY FINDINGS:")
print(f"Hotspot #1: {top_areas.index[0]} ({top_areas.iloc[0]} vendors)")
print(f"Best rated: {df_street.nlargest(1,'Dining_Rating')['Restaurant_Name'].iloc[0]}")
print(f"Avg price: ₹{df_street['Pricing_for_2'].mean():.0f}")
print("\nTop 5 preview:")
print(df_street.nlargest(5, 'Dining_Rating')[['Restaurant_Name', 'Locality', 'Dining_Rating', 'Pricing_for_2']])

df_street.to_csv('street_food_final.csv', index=False)
print("💾 SAVED for dashboard!")
