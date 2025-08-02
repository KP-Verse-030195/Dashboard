import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.metrics import (
    get_delivery_metrics,
    get_rto_metrics,
    get_cod_prepaid_split,
    get_pickup_metrics,
    get_revenue_metrics
)

st.set_page_config(page_title="Logistics Performance Dashboard", layout="wide")

st.title("📦 Logistics Performance Dashboard")

uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("🚚 Delivery Metrics")
    st.dataframe(get_delivery_metrics(df), use_container_width=True)

    st.subheader("📦 RTO Metrics")
    st.dataframe(get_rto_metrics(df), use_container_width=True)

    st.subheader("💰 COD vs Prepaid")
    st.dataframe(get_cod_prepaid_split(df), use_container_width=True)

    st.subheader("📦 Pickup Performance")
    st.dataframe(get_pickup_metrics(df), use_container_width=True)

    st.subheader("📊 Revenue")
    revenue = get_revenue_metrics(df)
    st.metric("Total Revenue After Tax", f"₹{revenue['total_revenue_after_tax']:,.2f}")
    st.metric("Total Revenue Before Tax", f"₹{revenue['total_revenue_before_tax']:,.2f}")
