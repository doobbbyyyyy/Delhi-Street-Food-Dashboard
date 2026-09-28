from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from src.analytics import load_data


df = load_data()
output = Path(__file__).resolve().parent / "outputs"
output.mkdir(exist_ok=True)

hotspots = df["Locality"].value_counts().head(10).sort_values()
fig, ax = plt.subplots(figsize=(10, 6))
hotspots.plot.barh(ax=ax, color="#f59e0b")
ax.set_title("Top 10 Delhi NCR vendor localities")
ax.set_xlabel("Number of vendors")
fig.tight_layout()
fig.savefig(output / "top_localities.png", dpi=160)
plt.close(fig)

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df["Pricing_for_2"], df["Dining_Rating"], alpha=0.55, color="#15803d")
ax.set_title("Price for two versus dining rating")
ax.set_xlabel("Price for two (₹)")
ax.set_ylabel("Dining rating")
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(output / "price_vs_rating.png", dpi=160)
plt.close(fig)

print(f"Saved charts to {output}")
