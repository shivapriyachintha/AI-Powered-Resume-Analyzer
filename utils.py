import io
import pdf2image
import google.generativeai as genai
import streamlit as st

def navigate_to_page(page_name: str):
    st.query_params["page"] = page_name

# Google Gemini API
genai.configure(api_key="YOUR API KEY")  

def get_gemini_response(prompt, pdf_content, jd):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([prompt, pdf_content, jd])
    return response.text

def input_pdf_setup(resume_bytes):
    images = pdf2image.convert_from_bytes(resume_bytes)
    first_page = images[0]
    return first_page


