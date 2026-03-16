import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Causes and Measures of Income Inequality")

st.markdown("""
Income inequality emerges from multiple structural and economic factors.
Understanding these factors is essential for designing effective economic policies.
""")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Key Causes")

    st.markdown("""
**Education Inequality**

Differences in access to quality education can create large income gaps.

**Technological Change**

Technological advancements often increase demand for highly skilled labor.

**Labor Market Differences**

Employment opportunities vary across regions and industries.

**Globalization**

Global trade and economic integration may increase income disparities between
skilled and unskilled workers.
""")

with col2:

    st.subheader("Policy Measures")

    st.markdown("""
**Progressive Taxation**

Higher taxes on high-income individuals help redistribute wealth.

**Education Investment**

Improving access to education helps reduce long-term inequality.

**Social Welfare Programs**

Support programs can protect vulnerable populations.

**Employment Policies**

Policies that encourage job creation can help reduce income disparities.
""")

st.markdown("---")

st.subheader("Long-Term Strategies")

st.markdown("""
Addressing income inequality requires long-term economic strategies that promote
inclusive growth and equal access to opportunities.

Policies that combine education development, labor market reforms,
and social protection programs are often the most effective in reducing inequality.
""")
