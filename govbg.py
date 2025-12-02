import streamlit as st
import pandas as pd

st.set_page_config(page_title="Budget Dashboard", page_icon="📊", layout="wide")

st.title("📊 Indian Budget Dashboard (2014–2025)")
st.write("Dataset is automatically loaded from GitHub.")

# ---- Load CSV from GitHub RAW URL ----
CSV_URL = "https://raw.githubusercontent.com/Yashhh-07/bg2/main/BG1.csv"

try:
    df = pd.read_csv(CSV_URL)
except Exception as e:
    st.error("❌ Could not load CSV file from GitHub. Check the file name and path.")
    st.stop()

# ---- Show dataset ----
st.subheader("📄 Dataset Preview")
st.dataframe(df)

# ---- Select Department ----
departments = df["Department"].unique()
department = st.selectbox("Select Department", departments)

# ---- Extract budget values ----
row = df[df["Department"] == department].iloc[0]
years = df.columns[1:]  # all year columns
values = row[1:].astype(float)

# ---- Convert to plotting DataFrame ----
chart_df = pd.DataFrame({
    "Year": years,
    "Budget": values
})

# ---- Line Chart ----
st.subheader(f"📈 Budget Trend for {department}")
st.line_chart(chart_df, x="Year", y="Budget")

# ---- Bar Chart ----
st.subheader(f"📊 Budget Distribution for {department}")
st.bar_chart(chart_df, x="Year", y="Budget")

st.write("---")
st.caption("Built with ❤️ using Streamlit & GitHub RAW data loading")
