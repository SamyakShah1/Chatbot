import openai
import pandas as pd
import streamlit as st
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from environment variables
# openai.api_key = os.getenv("OPENAI_API_KEY") # Replace with your actual API key

# Create OpenAI client
client = openai.OpenAI(api_key=openai.api_key)

# Load dataset
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Chatbot function
def ask_chatbot(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on data."},
            {"role": "user", "content": question}
        ]
    )
    
    return response.choices[0].message.content

# Streamlit UI
st.title("Dataset Chatbot")

# Load CSV directly
file_path = r"C:\Users\Samyak Shah\OneDrive\Desktop\scaraping datascience\structured_from.csv"
df = load_data(file_path)

st.write("### Preview of the dataset:")
st.write(df.head())

question = st.text_input("Ask a question about the dataset:")
if st.button("Get Answer") and question:
    answer = ask_chatbot(question)
    st.write("### Answer:")
    st.write(answer)
