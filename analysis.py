import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from analytics import load_data  # noqa: E402


df = load_data()
print(f"Street-food vendors analyzed: {len(df):,}")
print("\nTop 10 localities:")
print(df["Locality"].value_counts().head(10).to_string())
print("\nBest-rated vendors:")
print(df.nlargest(10, "Dining_Rating")[["Restaurant_Name", "Locality", "Dining_Rating", "Pricing_for_2", "Category"]].to_string(index=False))
print("\nSummary:")
print(f"Average price for two: ₹{df['Pricing_for_2'].mean():,.0f}")
print(f"Average dining rating: {df['Dining_Rating'].mean():.2f}")
