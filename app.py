#This is a streamlit app to output API calls to DALL-E
# The user inputs a string as a response prompt and the app outputs a generated image
# The app also outputs the image as a .png file
import openai
import streamlit as st
# import requests
# import json
# import base64
# import io
# import os
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
openai.api_key = config['DALL-E']['key']

# Set the title of the app
st.title("DALL-E API")

# Set the subtitle of the app
st.subheader("A streamlit app to output API calls to DALL-E")

# Set the text of the app
st.text("This is a streamlit app to output API calls to DALL-E.")

# create columns for th inputs and outputs 
col1, col2 = st.columns(2)

#create the input box for the user to input a string
with col1:
    user_input = st.text_input("Enter a creative prompt:" )


# create a button to generate the image
if st.button("Generate Image"):
    # create the API call
    url = "https://api-inference.huggingface.co/models/afiaka87/dalle-mini"
    resp = openai.Image.create(
    prompt="{user_input}",
    n=1,
    size="1024x1024")
    image_url = resp['data'][0]['url']
    with col2:
        st.subheader("Output")
        st.image(image_url, caption="Generated Image")

# 
