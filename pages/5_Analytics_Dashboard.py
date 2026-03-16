# ---------------- IMPORTS ----------------
import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Global Income Distribution Dashboard",
    layout="wide"
)

# ---------------- DARK PROFESSIONAL STYLE ----------------
st.markdown("""
<style>

[data-testid="stSidebar"] {
    background-color: #000000;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

h1, h2, h3 {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("Global Income Distribution & Inequality Dashboard")
st.caption("Interactive Economic Analytics Platform")

# ---------------- LOAD DATA ----------------
df = pd.read_excel("master_dataset.xlsx")

# ---------------- CREATE GDP CATEGORY ----------------
def classify_gdp(value):
    if value < 4000:
        return "Low Income"
    elif value < 12000:
        return "Middle Income"
    else:
        return "High Income"

df["gdp_category"] = df["gdp_per_capita($)"].apply(classify_gdp)

# ---------------- CREATE INEQUALITY CATEGORY ----------------
def classify_inequality(value):
    if value < 30:
        return "Low Inequality"
    elif value < 45:
        return "Moderate Inequality"
    else:
        return "High Inequality"

df["inequality_level"] = df["gini_index"].apply(classify_inequality)

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("Dashboard Filters")

selected_country = st.sidebar.selectbox(
    "Country",
    ["All"] + sorted(df["country"].unique())
)

selected_year = st.sidebar.selectbox(
    "Year",
    ["All"] + sorted(df["year"].unique())
)

selected_gdp_category = st.sidebar.selectbox(
    "GDP Category",
    ["All"] + sorted(df["gdp_category"].unique())
)

selected_inequality = st.sidebar.selectbox(
    "Inequality Level",
    ["All"] + sorted(df["inequality_level"].unique())
)

# ---------------- FILTER LOGIC ----------------
filtered_df = df.copy()

if selected_country != "All":
    filtered_df = filtered_df[filtered_df["country"] == selected_country]

if selected_year != "All":
    filtered_df = filtered_df[filtered_df["year"] == selected_year]

if selected_gdp_category != "All":
    filtered_df = filtered_df[filtered_df["gdp_category"] == selected_gdp_category]

if selected_inequality != "All":
    filtered_df = filtered_df[filtered_df["inequality_level"] == selected_inequality]

# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs(["Overview", "Trends", "Analysis"])

# =========================================================
# TAB 1 — OVERVIEW
# =========================================================

with tab1:

    st.subheader("Executive KPI Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Avg GDP per Capita ($)",
        round(filtered_df["gdp_per_capita($)"].mean(), 2)
    )

    col2.metric(
        "Avg Gini Index",
        round(filtered_df["gini_index"].mean(), 2)
    )

    col3.metric(
        "Avg Unemployment (%)",
        round(filtered_df["unemployment_rate(%)"].mean(), 2)
    )

    col4.metric(
        "Countries",
        filtered_df["country"].nunique()
    )

    st.subheader("Country Economic Comparison")

    colA, colB = st.columns(2)

    gdp_country = filtered_df.groupby("country")["gdp_per_capita($)"].mean().reset_index()

    fig1 = px.bar(
        gdp_country,
        x="country",
        y="gdp_per_capita($)",
        color="gdp_per_capita($)",
        color_continuous_scale="viridis",
        template="plotly_dark",
        title="Average GDP per Capita by Country"
    )

    colA.plotly_chart(fig1, use_container_width=True)

    gini_country = filtered_df.groupby("country")["gini_index"].mean().reset_index()

    fig2 = px.bar(
        gini_country,
        x="country",
        y="gini_index",
        color="gini_index",
        color_continuous_scale="plasma",
        template="plotly_dark",
        title="Income Inequality Comparison by Country"
    )

    colB.plotly_chart(fig2, use_container_width=True)

# =========================================================
# TAB 2 — TRENDS
# =========================================================

with tab2:

    st.subheader("Economic Trends Over Time")

    colC, colD = st.columns(2)

    gdp_trend = filtered_df.groupby("year")["gdp_per_capita($)"].mean().reset_index()

    fig3 = px.line(
        gdp_trend,
        x="year",
        y="gdp_per_capita($)",
        markers=True,
        template="plotly_dark",
        title="GDP per Capita Trend"
    )

    colC.plotly_chart(fig3, use_container_width=True)

    gini_trend = filtered_df.groupby("year")["gini_index"].mean().reset_index()

    fig4 = px.line(
        gini_trend,
        x="year",
        y="gini_index",
        markers=True,
        template="plotly_dark",
        title="Gini Index Trend"
    )

    colD.plotly_chart(fig4, use_container_width=True)

# =========================================================
# TAB 3 — ANALYSIS
# =========================================================

with tab3:

    st.subheader("GDP vs Inequality Relationship")

    fig5 = px.scatter(
        filtered_df,
        x="gdp_per_capita($)",
        y="gini_index",
        color="country",
        template="plotly_dark",
        title="Correlation Between GDP per Capita and Inequality"
    )

    st.plotly_chart(fig5, use_container_width=True)

    st.subheader("Economic Category Distribution")

    colE, colF = st.columns(2)

    gdp_dist = filtered_df["gdp_category"].value_counts().reset_index()
    gdp_dist.columns = ["category","count"]

    fig6 = px.pie(
        gdp_dist,
        names="category",
        values="count",
        template="plotly_dark",
        color_discrete_sequence=["#7B61FF","#FFD700","#9CA3AF"],
        title="GDP Category Distribution"
    )

    colE.plotly_chart(fig6, use_container_width=True)

    ineq_dist = filtered_df["inequality_level"].value_counts().reset_index()
    ineq_dist.columns = ["category","count"]

    fig7 = px.pie(
        ineq_dist,
        names="category",
        values="count",
        template="plotly_dark",
        color_discrete_sequence=["#A29BFE","#FD79A8","#00CEC9"],
        title="Inequality Level Distribution"
    )

    colF.plotly_chart(fig7, use_container_width=True)

# ---------------- DATA DOWNLOAD ----------------

st.subheader("Download Filtered Dataset")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download Data",
    csv,
    "filtered_data.csv",
    "text/csv"
)

# ---------------- FOOTER ----------------

st.markdown("---")
st.caption("Data Analytics Dashboard | Built using Python, Streamlit & Plotly")
