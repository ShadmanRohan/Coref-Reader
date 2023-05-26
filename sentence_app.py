import streamlit as st
import pandas as pd
import requests

# Define the available JSON files
json_files = {
    "Descriptive": "https://github.com/ShadmanRohan/BenCoref/raw/master/data/train/descriptive.json",
    "Novel": "https://github.com/ShadmanRohan/BenCoref/raw/master/data/train/novel.json",
    "Story": "https://github.com/ShadmanRohan/BenCoref/raw/master/data/train/story.json",
    "Biography": "https://github.com/ShadmanRohan/BenCoref/raw/master/data/train/biography.json"
}

# Create a dropdown to select a JSON file
selected_file = st.selectbox("Select a file", list(json_files.keys()))

# Define the URL of the selected JSON file
json_url = json_files[selected_file]

# Fetch the JSON data
response = requests.get(json_url)
data = response.json()

# Convert the JSON data to a DataFrame
df = pd.DataFrame(data)

# Create a dropdown to select an ID
selected_id = st.selectbox("Select an ID", df['id'].unique())

# Filter the DataFrame based on the selected ID
selected_data = df[df['id'] == selected_id]['sentences'].tolist()
mention_clusters = df[df['id'] == selected_id]['mention_clusters'].tolist()

# Create a dropdown to select a sentence
selected_sentence = st.selectbox("Select a sentence", range(len(mention_clusters[0])))

# Display the selected data in a formatted way
st.subheader("Selected Data")
if len(selected_data) == 0:
    st.write("No data found for the selected ID.")
else:
    st.write(f"ID: {selected_id}")
    st.write(f"Sentence: {selected_sentence}")
    st.write(' '.join(selected_data[0][selected_sentence]))
    st.write(mention_clusters[0][selected_sentence])
