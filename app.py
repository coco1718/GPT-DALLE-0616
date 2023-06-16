

import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]


st.title("ChatGPT plus DALL-E")

with st.form("form"):
    user_input = st.text_input("Prompt")#userinput 저장
    size = st.selectbox("Size", ["1024x1024","512x512","256x256"])
    submit = st.form_submit_button("제출")

#gpt response를 만든다
if submit and user_input:
    #st.write(user_input) # input아래 보이도록
    gpt_prompt = [{
        "role": "system",
        "content": "Imagine the detail appearance of the input. Response it shotly around 30 words."
    }]

    gpt_prompt.append({
        "role": "user",
        "content": user_input
    })

    with st.spinner("Waiting for ChatGPT..."):
        gpt_response = open.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = gpt_prompt
        )

    prompt = gpt_response["choices"][0]["message"]["content"]
    st.write(prompt)

    with st.spinner("Waiting for DALL-E..."):
        dalle_response = openai.Image.create(
            prompt=prompt,
            #size="1024x1024"
            size=size
        )

    st.image(dalle_response["data"][0]["url"]) 


