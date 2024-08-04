import streamlit as st
from transformers import pipeline

st.title('Hugging face NLP Test')

st.info('coming soon')

model=pipeline('sentiment-analysis')

# Create an input text box
input_text = st.text_input("Enter your text", "")

# Create a button to trigger model inference
if st.button("Analyze"):
    # Perform inference using the loaded model
    result = model(input_text)
    st.write("Prediction:", result[0]['label'], "| Score:", result[0]['score'])