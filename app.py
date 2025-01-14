from dotenv import load_dotenv
load_dotenv() ## loading all the env variables

import streamlit as st 
import os 
import google.generativeai as genai 
from PIL import Image


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load gemini flash latest  model and get response 

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def get_gemmini_response(input,image,prompt):
    response = model.generate_content([input,image[0],prompt])

    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data  = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }

        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Initiaalize our streamlit APP

st.set_page_config(page_title="Multilangauge Invoice Extractor")

st.header("Multilangauge Invoice Extractor")

input = st.text_input("Input:",key="input")

uploaded_file = st.file_uploader("Choose an image of the invoice .......",type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image .",use_column_width=True)

submit = st.button("Tell me about the invoice")

input_prompt  = """
You are an expert in understanding invoices. 
We will upload an image as invoices you will have to answer any questions
based on the uploaded invoice image
"""
## If Submit button is click  

if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemmini_response(input_prompt,image_data,input)
    st.subheader("The response is ")
    st.write(response)
    