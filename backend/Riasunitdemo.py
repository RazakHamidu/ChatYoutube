import streamlit as st

text = """

*Streamlit* is **really** ***cool***.

"""
with st.container(border=True):
    st.markdown(text)
