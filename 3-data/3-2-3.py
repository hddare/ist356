import requests
import pandas as pd
import streamlit as st

st.title("EXcel to JSON")
uploaded_file = st.file_uploader("Choose a file" type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file.getvalue())
    st.dataframe(df)
    json_file = df.to_json(orient="records", index=False)
    json_filename = uploaded_file.name.split(".")[0] + ".json"
    
