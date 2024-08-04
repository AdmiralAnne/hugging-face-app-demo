import streamlit as st
from transformers import pipeline

pipe=pipeline("sentiment-analysis")
# store the text to analyze in a variable 
text = st.text_area=("enter your text here")

# if text has some value then, run this code
if text:
    output=pipe(text)
    st.json(out)