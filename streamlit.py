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
    transformation = Transformer.generate_transformations(template_upload,csv_upload,openai_api_key)
    st.write("Found the following Transformations:")
    st.json(transformation)
    
    feedback = st.selectbox("Are transformations correct?",['Yes','No'])
    match feedback:
        case 'Yes':
            if st.button('Generate Python Transformation Code'):
                code = Transformer.transformations_to_code(transformation,openai_api_key)
                st.code(code)
                st.write("Copy the code and run it on your machine")
        case 'No':
            None


else:
    st.write("**Template and CSV to be transformed are required")
    