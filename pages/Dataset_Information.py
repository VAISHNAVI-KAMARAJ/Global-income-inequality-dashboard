import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dataset Information")

df = pd.read_excel("master_dataset.xlsx")

st.markdown("""
This project uses a dataset containing global economic indicators
for multiple countries across several years.

The dataset includes the following variables:

• **Country** – Country name  
• **Year** – Year of observation  
• **GDP per Capita ($)** – Economic output per person  
• **Gini Index** – Measure of income inequality  
• **Unemployment Rate (%)** – Percentage of unemployed population
""")

st.markdown("---")

st.subheader("Dataset Preview")

st.dataframe(df.head())

st.markdown("---")

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))
col2.metric("Countries", df["country"].nunique())
col3.metric("Years Covered", f"{df['year'].min()} - {df['year'].max()}")

st.markdown("---")

st.subheader("Countries Included")

st.write(sorted(df["country"].unique()))
