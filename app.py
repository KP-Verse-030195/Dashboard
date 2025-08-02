import streamlit as st
import pandas as pd
import os

from utils.metrics import get_delivery_metrics, get_rto_metrics, get_cod_prepaid_split, get_pickup_metrics, get_revenue_metrics
from utils.charts import plot_delivery_pie, plot_rto_bar, plot_cod_pie, plot_pickup_bar
from utils.filters import filter_data

# Set page config
st.set_page_config(page_title="Shipment Dashboard", layout="wide")

# Sidebar - Branding and filters
st.sidebar.image("assets/logo.png", use_column_width=True)
st.sidebar.title("📊 Dashboard Filters")

uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='utf-8')

    # Apply filters
    df_filtered = filter_data(df)

    st.title("📦 Shipment Performance Dashboard")

    # Tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📮 Delivery", "↩️ RTO", "💰 Prepaid/COD", "🚚 Pickup", "📈 Revenue", "📋 Full Table"
    ])

    with tab1:
        st.subheader("Delivery Performance")
        delivery_data = get_delivery_metrics(df_filtered)
        st.dataframe(delivery_data)
        st.pyplot(plot_delivery_pie(df_filtered))

    with tab2:
        st.subheader("RTO Performance")
        rto_data = get_rto_metrics(df_filtered)
        st.dataframe(rto_data)
        st.pyplot(plot_rto_bar(df_filtered))

    with tab3:
        st.subheader("Prepaid / COD Split")
        cod_split = get_cod_prepaid_split(df_filtered)
        st.dataframe(cod_split)
        st.pyplot(plot_cod_pie(df_filtered))

    with tab4:
        st.subheader("Pickup Performance")
        pickup_data = get_pickup_metrics(df_filtered)
        st.dataframe(pickup_data)
        st.pyplot(plot_pickup_bar(df_filtered))

    with tab5:
        st.subheader("Revenue Summary")
        revenue_data = get_revenue_metrics(df_filtered)
        st.metric("Total Revenue (After Tax)", f"₹ {revenue_data['total_revenue_after_tax']:,.2f}")
        st.metric("Total Revenue (Before Tax)", f"₹ {revenue_data['total_revenue_before_tax']:,.2f}")

    with tab6:
        st.subheader("Full Shipment Table")
        st.dataframe(df_filtered)

else:
    st.title("📦 Shipment Dashboard")
    st.info("Upload a shipment CSV file from the sidebar to begin.")
