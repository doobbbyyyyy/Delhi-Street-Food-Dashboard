import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from analytics import filter_street_food, kpis, load_data  # noqa: E402


def test_load_data_uses_committed_dataset():
    df = load_data()
    assert len(df) == 833
    assert {"Restaurant_Name", "Pricing_for_2", "Dining_Rating"}.issubset(df.columns)


def test_filter_street_food_is_case_insensitive():
    df = pd.DataFrame({"Category": ["Street Food", "Italian", "MOMO special"]})
    result = filter_street_food(df)
    assert len(result) == 2


def test_kpis_are_calculated_from_filtered_rows():
    df = pd.DataFrame({
        "Pricing_for_2": [200, 400],
        "Dining_Rating": [4.0, 4.5],
        "Delivery_Rating": [4.1, None],
    })
    result = kpis(df)
    assert result["vendors"] == 2
    assert result["avg_price"] == 300
    assert result["missing_delivery_rating"] == 1
