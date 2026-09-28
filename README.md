# Delhi NCR Street Food Dashboard

A reproducible Streamlit dashboard exploring **833 restaurants** in the committed Delhi NCR street-food dataset. It covers price, dining ratings, delivery ratings, localities, categories, and map coordinates.

## Features

- Filter by locality, category, price, and dining rating.
- Compare price for two with dining rating.
- Explore vendor concentration by locality.
- View top-rated vendors with review counts.
- Browse vendor locations on a map.
- Run the same analysis from the command line or generate PNG charts.

## Run locally

```bash
git clone https://github.com/doobbbyyyyy/Delhi-Street-Food-Dashboard.git
cd Delhi-Street-Food-Dashboard
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
streamlit run dashboard.py
```

Command-line scripts:

```bash
python analysis.py
python summary.py
python visualization.py
pytest
```

Generated charts are written to `outputs/` and are intentionally ignored by Git.

## Dataset

`street_food_final.csv` contains 833 filtered records and 15 fields. The dataset includes restaurant details, category text, price for two, dining and delivery ratings, review counts, address/contact fields, and coordinates.

Some delivery ratings and descriptive fields are missing. Category matching is a practical proxy for street food rather than a perfect classification model. Restaurant names are not unique identifiers.

## Current snapshot

The committed snapshot has an average price for two of approximately **₹784**, an average dining rating of approximately **4.11**, and **Connaught Place, New Delhi** as the most represented locality. These figures should be regenerated if the data is refreshed.

## Project structure

```text
dashboard.py              # Streamlit application
analysis.py               # CLI analysis
summary.py                # Data-quality summary
visualization.py          # Reproducible PNG charts
src/analytics.py          # Shared data and KPI logic
tests/test_analytics.py   # Automated checks
street_food_final.csv     # Committed cleaned dataset
```

## Disclaimer

This is a portfolio/learning project. Restaurant information, ratings, prices, and contact details may change over time; verify information independently before relying on it.
