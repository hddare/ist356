import requests
import streamlit as st
import pandas as pd


st.title("First API")
url = "https://jsonplaceholder.typicode.com/users/"
response = requests.get(url)
response.raise_for_status()
users=response.json()
users_df = pd.json_normalize(users)
st.dataframe(users_df)