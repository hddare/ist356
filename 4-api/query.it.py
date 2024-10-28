import pandas as pd
import requests 
import streamlit as st

APIKEY = "6502ef18c563ffdc99b1bc4c"

st.title("Query It!")

file = st.file_uploader("Upload a csv file", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df)

    question = st.text_area("What question would you like to ask of this data?")
    if question:
        prompt = "With the following data:\n"
        prompt += df.to_string(index=False)
        prompt += "\n\n"
        prompt += "Answer the following question:\n"
        prompt += question

        url = "https://cent.ischool-iot.net/api/openai/generate"
        response = requests.post(url, data={"query": prompt}, headers={"x-api-key" : APIKEY})
        response.raise_for_status()
        results = response.json()
        st.write(results)
  

APIKEY = "6502ef18c563ffdc99b1bc4c"

prompts = [
    "You are a helpful AI assistant. That speaks in emoji.",
    "You are an AI assistant that talks like a pirate.",
    "You are an AI assistant that thinks you are a Shakespearean actor.",
    "You are an AI assistant that adds beeps and clicks to your speech. Because you are a robot.",
    "You are an AI assistant that is a conspiracy theorist. You are paranoid."
]

def generate_ai_response(context):
    url = "https://cent.ischool-iot.net/api/openai/chat/completions"
    response = requests.post(url, json=context, headers={"X-API-KEY": APIKEY})
    response.raise_for_status()
    results = response.json()
    content =  results["choices"][0]["message"]["content"]
    return content

st.title("Chat AI.")
st.caption("Let's help you understand system prompts.")
system_prompt = st.selectbox("Select a system prompt", prompts)


if system_prompt:
    # Initialize chat history
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    prompt = st.chat_input("?")
    if prompt:
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = generate_ai_response(st.session_state.messages)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history