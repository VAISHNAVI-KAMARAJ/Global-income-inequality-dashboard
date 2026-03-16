import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Interactive Data Explorer")

df = pd.read_excel("master_dataset.xlsx")

st.markdown("""
This section allows users to explore the raw dataset used in the analysis.
""")

country = st.selectbox("Select Country", sorted(df["country"].unique()))

filtered = df[df["country"] == country]

st.dataframe(filtered)
