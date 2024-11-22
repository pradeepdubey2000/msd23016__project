import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Set up the Streamlit page
st.set_page_config(page_title="🔍 CVE Similarity Search", page_icon=":guardsman:", layout="wide")

# Title and description for the app
st.title("🔍 CVE Similarity Search")
st.markdown("""
Enter a vulnerability description below, and we will find the most similar CVE records from the database. This tool helps in identifying vulnerabilities based on descriptions.
""")
st.markdown("---")

# Load only necessary columns (embedding columns + CVE_ID)
dataset_path = r'C:\Users\pradeep dubey\Desktop\NLP_Project\Data\merged_cve_data.csv'  # Adjust path
embedding_columns = [str(i) for i in range(768)]  # Assuming embeddings are stored in columns "0" to "767"

# Cache the data loading to speed up the app (using Streamlit's caching feature)
@st.cache_resource
def load_data():
    # Load only the embedding columns and CVE_ID for faster processing
    cve_data = pd.read_csv(dataset_path, usecols=['CVE_ID'] + embedding_columns + ['Description', 'Impact_Score', 'Base_Score', 'Exploitability_Score', 'Access_Complexity', 'Access_Vector', 'Availability_Impact', 'Confidentiality_Impact', 'Integrity_Impact', 'Published_Date'])
    return cve_data

# Load data
cve_data = load_data()

# Function to compute cosine similarity efficiently
def find_similar_cves(description, n_similar=5):
    # Load the pre-trained SentenceTransformer model (if not already loaded)
    model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
    
    # Encode the input description into an embedding
    input_embedding = model.encode(description).reshape(1, -1)
    
    # Extract the precomputed embeddings from the dataset
    dataset_embeddings = cve_data[embedding_columns].values
    
    # Compute cosine similarity between the input embedding and all dataset embeddings
    similarities = cosine_similarity(input_embedding, dataset_embeddings).flatten()

    # Get the indices of the top N most similar CVEs
    top_indices = similarities.argsort()[-n_similar:][::-1]

    # Retrieve the most similar CVEs based on those indices
    similar_cves = cve_data.iloc[top_indices]

    # Remove the embedding columns from the result
    similar_cves = similar_cves.drop(columns=embedding_columns)

    # Convert the result to JSON format
    output_json = similar_cves.to_json(orient='records', lines=False)
    
    return output_json

# User input field for description
description = st.text_area("Enter vulnerability description:", height=150, max_chars=1000)

# Button to trigger the search
if st.button("Find Similar CVEs", key="search_button"):
    if description.strip():
        # Find similar CVEs based on the input description
        similar_cves_json = find_similar_cves(description)

        # Display the results in JSON format
        st.markdown("### Top 5 Similar CVEs (JSON Format)")
        st.json(similar_cves_json)

        st.markdown("---")
        st.markdown("""
        This analysis is based on the CVE descriptions and their associated impact scores, exploitability metrics, and other related factors.
        """)
    else:
        st.warning("Please enter a description to find similar CVEs.")

# Optional: Add a footer or additional UI elements if needed
st.markdown("""
---
Created with ❤️ by Your Name. For more information, visit [Your GitHub](https://github.com/yourprofile).
""")
