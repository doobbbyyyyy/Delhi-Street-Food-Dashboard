from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "street_food_final.csv"
STREET_KEYWORDS = ("street", "chaat", "momo", "roll", "fast", "snack", "kulfi")


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the committed, cleaned street-food dataset."""
    df = pd.read_csv(path)
    numeric = [
        "Pricing_for_2", "Dining_Rating", "Dining_Review_Count",
        "Delivery_Rating", "Delivery_Rating_Count", "Latitude", "Longitude",
    ]
    for column in numeric:
        if column in df:
            df[column] = pd.to_numeric(df[column], errors="coerce")
    return df


def filter_street_food(df: pd.DataFrame) -> pd.DataFrame:
    """Return rows whose category contains a street-food-related keyword."""
    pattern = "|".join(STREET_KEYWORDS)
    return df[df["Category"].fillna("").str.contains(pattern, case=False, regex=True)].copy()


def kpis(df: pd.DataFrame) -> dict:
    """Calculate dashboard KPIs from the currently filtered dataframe."""
    return {
        "vendors": len(df),
        "avg_price": float(df["Pricing_for_2"].mean()) if len(df) else 0.0,
        "median_price": float(df["Pricing_for_2"].median()) if len(df) else 0.0,
        "avg_dining_rating": float(df["Dining_Rating"].mean()) if len(df) else 0.0,
        "missing_delivery_rating": int(df["Delivery_Rating"].isna().sum()),
    }
