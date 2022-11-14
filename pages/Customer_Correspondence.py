import streamlit as st 
import openai
import random

openai.api_key = st.secrets["openai_api_key"]

st.header('Make customer interactions professional and friendly! 🫶 ')

temp_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
cust_prompt = "Correct this to standard English with a professional and friendly tone:"
agnt_prompt = st.text_area('Enter your message here', value="Sorry, mr james.  I cant make it today coz of a conflict. are you availanble tmw same tym?")
resp_len = st.number_input('Word limit', value=100, step=50)

if st.button('Generate edited response! 🧑‍🚀'):
  cust_response = openai.Completion.create(
  model="text-davinci-002",
  prompt=cust_prompt+" "+agnt_prompt,
  temperature=random.choice(temp_list),
  max_tokens=resp_len,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0)
  
  st.write(cust_response['choices'][0]['text'].strip('\n'))