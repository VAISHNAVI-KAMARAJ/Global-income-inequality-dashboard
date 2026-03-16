import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Global Income Inequality Platform",
    layout="wide"
)

st.title("Global Income Distribution & Inequality Analytics Platform")

st.markdown("""
### Introduction

Income inequality is a major economic challenge affecting countries across the world.
Differences in income distribution influence economic growth, social mobility,
and the overall well-being of populations.

This platform provides an analytical perspective on global economic conditions
by examining key economic indicators across countries and years.
""")

st.markdown("---")

st.subheader("Key Indicators Analyzed")

col1, col2, col3 = st.columns(3)

col1.markdown("""
**GDP per Capita**

Measures the economic output produced per person in a country.
It is widely used to evaluate the level of economic development.
""")

col2.markdown("""
**Gini Index**

The Gini Index measures income inequality within a country.
Higher values indicate greater income disparity.
""")

col3.markdown("""
**Unemployment Rate**

Represents the percentage of the labor force that is unemployed
and actively seeking employment.
""")

st.markdown("---")

st.subheader("Platform Capabilities")

st.markdown("""
This analytics platform allows users to:

• Compare economic performance across countries  
• Analyze income inequality patterns globally  
• Explore relationships between GDP, inequality, and unemployment  
• Examine trends across multiple years  
• Interact with dynamic visualizations and filters
""")

st.info("Navigate to the **Analytics Dashboard** to explore the data interactively.")