import os
import streamlit as st
from transformer import Transformer

openai_api_key = os.getenv('OPENAI_API_KEY')

Transformer = Transformer()

st.set_page_config(
    page_title="Table Transformer"
)

st.title('Table Transformer')

template_upload = st.file_uploader("Upload Template",type=['csv'])
csv_upload = st.file_uploader("Upload CSV",type=['csv'])

if template_upload and csv_upload:
    result = Transformer.generate_transformations(template_upload,csv_upload,openai_api_key)
    st.write("Found the following Transformations:")
    st.json(result)
    
    feedback = st.selectbox("Are transformations correct?",['Yes','No'])


else:
    st.write("**Template and csv to be transformed are required")
    