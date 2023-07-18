import streamlit as st

st.title('Table Transformer')

template_upload = st.file_uploader("Upload Template",type=['csv'])
csv_upload = st.file_uploader("Upload CSV",type=['csv'])