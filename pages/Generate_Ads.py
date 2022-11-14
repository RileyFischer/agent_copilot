import streamlit as st 
import openai
import random

openai.api_key = st.secrets["openai_api_key"]

st.header('Generate creative ads for various platforms instantly! 💫')

temp_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
cnty_val = st.text_input('County')
city_val = st.text_input('City')
stat_val = st.text_input('State')
brnd_val = st.selectbox('Brand', ['Coldwell Banker','Century 21','Better Homes and Gardens','Corcoran','Southeby\'s'])
ptfm_val = st.selectbox('Platform', ['Facebook','Twitter','Instagram','Tiktok','Reddit'])
trgt_val = st.selectbox('Target Audience', ['Empty nesters',' Newly married','Looking to grow their family','First time home buyers'])
resp_len = st.number_input('Ad word limit', value=150, step=50)
ad_prompt = "Write an SEO optimized and creative ad for "+(brnd_val)+" to run on "+(ptfm_val)+" aimed at potential home buyers who are "+(trgt_val)+" in "+str(city_val)+", "+str(cnty_val)+" county, "+str(stat_val)+". Use appropriate adjectives to make a compelling and attractive ad."

if st.button('Generate Ad! 🧑‍🚀'):
  ad_response = openai.Completion.create(
  model="text-davinci-002",
  prompt=ad_prompt,
  temperature=random.choice(temp_list),
  max_tokens=resp_len,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0)
  st.write(ad_response['choices'][0]['text'].strip('\n'))