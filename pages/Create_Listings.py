import streamlit as st 
import os
import openai
import random

openai.api_key = st.secrets["openai_api_key"]

listing_prompt ="Write a professional and compelling property description for creating listing using adjectives to praise the property as seen on zillow and redfin"
temp_list_1 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
temp_list_2 = [0.7, 0.8, 0.9, 1.0]
temp_list_vals = ['Let us keep it sane', 'Surprise me!']

st.header('Create a professional listing instantly with Agent Co-Pilot!  ✨')

import os
def copy_to_clipboard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

col1, col2 = st.columns(2)

with col1:
	strt_val = st.text_input('Street Address')
	city_val = st.text_input('City')
	stat_val = st.text_input('State')
	zipc_val = st.text_input('ZIP')
	prop_val = st.selectbox('Property Type', ['Single Family Home','Apartment','Condo','Multi-family Home','Townhouse','Mobile Home'])
	prop_det = st.text_area('General Property Details', value="Spacious, Recently renovated, Modern Architecture, Duplex, Basement")
	otdr_det = st.text_area('Outdoor Details', value="Overlooking lake, garden, Patio, Private pool")
	addn_det = st.text_area('Additional Details', value="Gated community, 24 hour security, Shared Gym, Close to Public Transport")
	resp_len = st.number_input('Word limit', value=200, step=50)

with col2:
	num_beds = st.number_input('Number of Bedrooms', step=1)
	num_bath = st.number_input('Number of Bathrooms', step=0.5)
	num_sqft = st.number_input('Property Sq. Ft', min_value=0, step=100)
	num_park = st.number_input('Number of parking spots', min_value=0, step=1)
	blt_year = st.number_input('Built Year', value= 1980, min_value=1800, max_value = 2022)
	kchn_det = st.text_area('Kitchen Details', value="Quartz counter, Kitchen island, stainless steel appliances, Gas range")
	intr_det = st.text_area('Interior Details', value="Hardwood floors, Fireplace in the living room, freshly painted")
	luck_val = st.radio('Feeling lucky?', temp_list_vals)


if st.button('Generate Listing Description! 🧑‍🚀'):
	property_prompt = "Property: " +str(prop_val[0])+" in "+str(city_val)+" "+str(stat_val)+", "+str(int(num_beds))+" bedrooms, "+str(int(num_bath))+" bathrooms, "+str(int(num_sqft))+" sqft, "+str(int(num_park))+" parking spot(s), built in "+str(int(blt_year))+", "+str(prop_det)+", "+str(intr_det)+", "+str(kchn_det)+", "+str(otdr_det)+", "+str(addn_det)+""
	
	if (luck_val == temp_list_vals[0]):
		temp_list = temp_list_1
	else:
		temp_list = temp_list_2
	
	listing_response = openai.Completion.create(
	  model="text-davinci-002",
	  prompt=listing_prompt+" "+property_prompt,
	  temperature=random.choice(temp_list),
	  max_tokens=resp_len,
	  top_p=1.0,
	  frequency_penalty=0.5,
	  presence_penalty=0.5
)
	st.write(listing_response['choices'][0]['text'].strip('\n'))