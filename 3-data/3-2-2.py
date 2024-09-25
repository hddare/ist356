import json
import pandas as pd
import streamlit as st
import requests as req


link = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees.json"
response = req.get(link)
data = response.json()
df = pd.json_normalize(data, record_path="employees")
st.dataframe(df)