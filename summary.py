import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from analytics import load_data  # noqa: E402


df = load_data()
print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())
print("\nData types:")
print(df.dtypes.to_string())
print("\nMissing values:")
print(df.isna().sum().to_string())
print("\nNumeric summary:")
print(df.select_dtypes(include="number").describe().to_string())
