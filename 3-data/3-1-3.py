import pandas as pd
import numpy as np
import streamlit as st
import certifi
url = "https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv"

customers = pd.read_csv(url)

st.title('Customers')
choice = st.radio("Select Gender:", ["M", "F"])
cols = st.multiselect("Select Columns", customers.columns)
gender_index = customers['Gender']==choice
st.dataframe(customers[gender_index][cols])