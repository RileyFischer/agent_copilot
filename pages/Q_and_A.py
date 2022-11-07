import streamlit as st 
import openai
import random
import requests

openai.api_key = st.secrets["openai_api_key"]

st.header('Real time Q & A! ⭐')

faq_file = open('faq', 'r')
faq_data = [line.split(',') for line in faq_file.readlines()]
faq_flat = [item for sublist in faq_data for item in sublist]

question = st.text_area('Enter questions here:', value="How does the Appraisal process take place?")
resp_len = st.number_input('Answer word limit', value=200, step=50)
q_payload = {
   "documents": faq_flat,
   "question": question,
   "search_model": "davinci",
   "model": "curie",
   "examples_context": "There are nine planets and one star in the solar system.",
   "examples": [["How many planets are there in the solar system?", "There are 9 planets in the solar system"]],
   "max_tokens": resp_len
}

head = {'Authorization': 'Bearer ' + openai.api_key}
data = q_payload

url = 'https://api.openai.com/v1/answers'
response = requests.post(url, json=data, headers=head)

if st.button('Answer me! 🧑‍🚀'):
	st.write(response.json()['answers'][0].split('\n', 1)[0])