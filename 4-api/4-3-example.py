import requests
import streamlit as st

def get_text_completion(query: str) -> str:
    url = "https://cent.ischool-iot.net/api/openai/generate"
    data = {"query": query}
    headers = {'X-API-KEY': '6502ef18c563ffdc99b1bc4c'}
    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()
    return response.json()


st.title("First GPT")
text = st.text_area('Enter some text')
if text:
    with st.spinner("Thinking..."):
        response = get_text_completion(text)
        st.write(response)
