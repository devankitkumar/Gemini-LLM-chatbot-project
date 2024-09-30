import streamlit as st  #to work with frontend and backend
from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()
# gmail= os.getenv('gmail')
# gmail_pass =os.getenv('gmail_pass')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key= GOOGLE_API_KEY)

def get_gemini_response(input_message, input_image):
    model= genai.GenerativeModel('gemini-1.5-flash')
    if input_message !="":
        response= model.generate_content([input_message, input_image])
    else:
        response= model.generate_content(input_message)
    return response.text

# print(gmail)
# print(gmail_pass)
# print(GOOGLE_API_KEY)
st.set_page_config(page_title='genrative ai based chatbot')
st.header('Gemini Based Chatbot 😍❤️')
input= st.text_input("Input prompt :", key="input")
uploaded_file = st.file_uploader("Choose an image :, ", type=['jpeg','jpg','png'])

submit= st.button('Submit')

display_image= " "
if uploaded_file is not None:
    # Open the image file uploaded
    display_image= Image.open(uploaded_file)
    st.image(display_image, caption="uploaded_image",use_column_width=True)

if submit:
    output= get_gemini_response(input_message=input,input_image=display_image)
    st.subheader('Your response is :')
    st.write(output)
