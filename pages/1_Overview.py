import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Project Overview")

st.markdown("""
### Understanding Income Inequality

Income inequality refers to the uneven distribution of income among individuals
within an economy. It is one of the most widely discussed issues in economic policy
because it directly affects economic opportunity, living standards, and long-term
economic stability.

A common measure used to quantify income inequality is the **Gini Index**.
The Gini Index ranges between:

• **0** – Perfect income equality  
• **100** – Maximum income inequality
""")

st.markdown("---")

st.subheader("Purpose of the Analysis")

st.markdown("""
The purpose of this platform is to analyze economic inequality across countries
using real economic indicators.

The analysis focuses on:

• Economic development differences between countries  
• The relationship between GDP growth and income inequality  
• Changes in unemployment levels across economies  
• Trends in economic indicators over time
""")

st.markdown("---")

st.subheader("Analytical Approach")

st.markdown("""
This platform combines **data analysis and interactive visualization techniques**
to provide insights into global income distribution.

Using statistical summaries and visual analytics, users can explore how
economic indicators vary across countries and identify patterns that influence
economic inequality.
""")
