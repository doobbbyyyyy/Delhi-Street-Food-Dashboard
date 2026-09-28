import sys
from pathlib import Path

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from analytics import kpis, load_data  # noqa: E402

st.set_page_config(page_title="Delhi Street Food Dashboard", page_icon="🍴", layout="wide")

@st.cache_data
def get_data():
    return load_data()


df = get_data()
st.title("Delhi NCR Street Food Explorer")
st.caption("A filterable view of restaurants, pricing, ratings, and locations in the committed dataset.")

with st.sidebar:
    st.header("Filters")
    localities = st.multiselect("Locality", sorted(df["Locality"].dropna().unique()))
    categories = st.multiselect("Category contains", sorted({x.strip() for value in df["Category"].dropna() for x in value.split(",")}))
    price_max = int(df["Pricing_for_2"].max())
    price_range = st.slider("Price for two (₹)", 0, price_max, (0, price_max), step=100)
    rating_min = st.slider("Minimum dining rating", 0.0, 5.0, 0.0, step=0.1)

filtered = df.copy()
if localities:
    filtered = filtered[filtered["Locality"].isin(localities)]
if categories:
    pattern = "|".join(categories)
    filtered = filtered[filtered["Category"].str.contains(pattern, case=False, na=False)]
filtered = filtered[filtered["Pricing_for_2"].between(*price_range)]
filtered = filtered[filtered["Dining_Rating"].ge(rating_min)]

metrics = kpis(filtered)
cols = st.columns(5)
cols[0].metric("Vendors", f"{metrics['vendors']:,}")
cols[1].metric("Average price", f"₹{metrics['avg_price']:,.0f}")
cols[2].metric("Median price", f"₹{metrics['median_price']:,.0f}")
cols[3].metric("Average dining rating", f"{metrics['avg_dining_rating']:.2f} ⭐")
cols[4].metric("Missing delivery ratings", f"{metrics['missing_delivery_rating']:,}")

left, right = st.columns(2)
with left:
    st.subheader("Top localities")
    locality_counts = filtered["Locality"].value_counts().head(10).rename("vendors")
    st.bar_chart(locality_counts)
with right:
    st.subheader("Price versus dining rating")
    st.scatter_chart(filtered[["Pricing_for_2", "Dining_Rating"]].rename(columns={"Pricing_for_2": "Price for two", "Dining_Rating": "Rating"}), x="Price for two", y="Rating")

if filtered["Latitude"].notna().any() and filtered["Longitude"].notna().any():
    st.subheader("Vendor map")
    map_df = filtered[["Latitude", "Longitude"]].dropna().rename(columns={"Latitude": "lat", "Longitude": "lon"})
    st.map(map_df)

st.subheader("Top-rated vendors")
top = filtered.sort_values(["Dining_Rating", "Dining_Review_Count"], ascending=False).head(10)
st.dataframe(top[["Restaurant_Name", "Locality", "Category", "Dining_Rating", "Dining_Review_Count", "Pricing_for_2"]], use_container_width=True, hide_index=True)
st.info("Category matching is a practical proxy for street food; ratings and prices reflect the committed dataset and may change when the source is refreshed.")
