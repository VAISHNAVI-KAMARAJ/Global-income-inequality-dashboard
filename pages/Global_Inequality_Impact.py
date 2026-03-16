import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Impact of Global Income Inequality")

st.markdown("""
Income inequality affects economic systems and social structures across the world.
Large income gaps can influence economic growth, social stability, and access to
opportunities for different population groups.
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Economic Impact")

    st.markdown("""
• Reduced long-term economic growth  
• Lower investment in education and human capital  
• Limited access to financial opportunities  
• Decreased productivity in developing economies

When wealth becomes highly concentrated, large portions of the population
may have limited access to resources necessary for economic advancement.
""")

with col2:

    st.subheader("Social Impact")

    st.markdown("""
• Reduced social mobility  
• Higher poverty levels  
• Increased economic vulnerability  
• Greater social and political tensions

High inequality can weaken social cohesion and create barriers to
equal opportunities for economic participation.
""")

st.markdown("---")

st.subheader("Importance of Monitoring Inequality")

st.markdown("""
Monitoring income inequality helps policymakers identify structural economic issues
and design policies aimed at promoting inclusive growth.

Countries that maintain balanced income distribution often experience:

• Higher economic stability  
• Improved social welfare  
• Sustainable long-term development
""")
