import pandas as pd
import streamlit as st

base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/"

customers = pd.read_csv(base + "customers.csv")
st.write("Customers")
months = ['jan', 'feb', 'mar', 'apr']
months_df = []
for month in months:
    month_df = pd.read_csv(base + f"purchases-{month}.csv")
    month_df['month'] = month
    months_df.append(month_df)

purchases = pd.concat(months_df)
combined = pd.merge(customers, purchases, left_on='customer_id', right_on = 'customer_id', how='outer').sort_values(by='month')
st.write("Combined Data")
st.dataframe(combined)
selected_month = st.selectbox("Select Month", months)
filtered = combined[combined['month'] == selected_month]
no_purchase = filtered[filtered['order_id'].isna()]
st.dataframe(filtered)