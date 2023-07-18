import streamlit as st


st.set_page_config(
    page_title="Table Transformer",
    layout='wide'
)

st.title('Table Transformer')

template_upload = st.file_uploader("Upload Template",type=['csv'])
csv_upload = st.file_uploader("Upload CSV",type=['csv'])

if template_upload and csv_upload:
    None

else:
    st.write("Template and csv to be transformed are required")
    