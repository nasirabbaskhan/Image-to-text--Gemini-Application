from dotenv import load_dotenv
import google.generativeai as genai # type: ignore
import streamlit as st
from PIL import Image
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# create the llm
model = genai.GenerativeModel("gemini-1.5-flash")


def get_response_from_gemini(user_input, image):
    if user_input!= "":
        response = model.generate_content([user_input, image]) 
    else:
        response = model.generate_content(image)
        
    return response.text


#initilize our streamlite app

st.set_page_config(page_title="image demo")
st.header("Image to text Gemini application")
user_input = st.text_input("what you want to ask about your image:")

# image uploading
uplead_file =st.file_uploader("upload your impage", type=["jpg","jpeg","png"])
# to show image

if uplead_file is not None:
    image = Image.open(uplead_file)
    st.image(image, caption="uploaded image", use_column_width=True)
    

submit = st.button("Ask the question")

if submit:
    st.subheader("The Response is:")
    response = get_response_from_gemini(user_input, image)
    st.write(response)
    
    