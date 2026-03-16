import streamlit as st

st.set_page_config(
    page_title="Global Income Inequality Platform",
    layout="wide"
)

st.title("Global Income Distribution & Inequality Analysis Platform")

st.markdown("""
Welcome to the **Global Income Inequality Analytics Platform**.

This platform explores global economic indicators such as:

• GDP per Capita  
• Gini Index (Income Inequality)  
• Unemployment Rate  

Use the **sidebar navigation** to explore different sections of the platform including:

Overview, Global Inequality Impact, Causes and Measures, Dataset Information, Analytics Dashboard, and Data Explorer.
""")

st.info("Select a page from the sidebar to explore the analytics dashboard.")