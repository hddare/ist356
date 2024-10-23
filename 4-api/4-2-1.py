import requests
import streamlit as st
import pandas as pd

def extract_entities(text: str) -> dict:
    url = "https://cent.ischool-iot.net/api/azure/entityrecognition"
    data = {"text": text}
    headers = {'X-API-KEY': '6502ef18c563ffdc99b1bc4c'}
    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()
    return response.json()

text = st.text_area('Enter some text')
if text:
    result = extract_entities(text)
    entities = result['results']['documents'][0]['entities']
    df = pd.DataFrame(entities)
    st.dataframe(df)
