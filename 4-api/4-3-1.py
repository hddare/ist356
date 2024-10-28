import streamlit as st
import requests
'''
Let's write an LLM-based spellchecker!

The spellchecker should take some text as input and return the misspelled works along with suggestions for the correct spellings. 

Make the inputs, then create a suitable prompt for the LLM.'''

text = st.text_area("Enter some text")
if text:
    prompt = "You are a spellchecker AI. You are given the following text:\n"
    prompt += text
    prompt += "\n\nIdentify the misspelled words and suggest corrections."
    url = "https://cent.ischool-iot.net/api/openai/generate"
    response = requests.post(url, data={"query": prompt}, headers={"x-api-key" : '6502ef18c563ffdc99b1bc4c'})
    response.raise_for_status()
    results = response.json()
    st.write(results)