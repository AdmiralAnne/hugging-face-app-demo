import streamlit as st
from transformers import pipeline

st.title('Hugging face NLP Test')
st.info('coming soon')

model=pipeline('sentiment-analysis')