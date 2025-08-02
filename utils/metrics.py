import pandas as pd

def get_delivery_metrics(df):
    delivered = df[df['status'].str.lower() == 'delivered']
    total = len(df)
    percent = round((len(delivered) / total) * 100, 2) if total > 0 else 0
    return pd.DataFrame({
        'Total Orders': [total],
        'Delivered': [len(delivered)],
        'Delivery %': [percent]
    })

def get_rto_metrics(df):
    rto = df[df['status'].str.lower().str.contains("rto")]
    total = len(df)
    percent = round((len(rto) / total) * 100, 2) if total > 0 else 0
    return pd.DataFrame({
        'Total Orders': [total],
        'RTO Count': [len(rto)],
        'RTO %': [percent]
    })

def get_cod_prepaid_split(df):
    cod = df[df['paymentMode'].str.lower() == 'cod']
    prepaid = df[df['paymentMode'].str.lower() != 'cod']
    return pd.DataFrame({
        'COD Orders': [len(cod)],
        'Prepaid Orders': [len(prepaid)]
    })

def get_pickup_metrics(df):
    attempted = df['outForPickup1stAttempt'].notna().sum()
    successful = df['pickupDate'].notna().sum()
    percent = round((successful / attempted) * 100, 2) if attempted > 0 else 0
    return pd.DataFrame({
        'Pickup Attempts': [attempted],
        'Successful Pickups': [successful],
        'Pickup Success %': [percent]
    })

def get_revenue_metrics(df):
    revenue_after_tax = df['merchantPriceAfterTax'].sum()
    revenue_before_tax = df['merchantPriceBeforeTax'].sum()
    return {
        'total_revenue_after_tax': revenue_after_tax,
        'total_revenue_before_tax': revenue_before_tax
    }
