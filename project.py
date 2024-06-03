import streamlit as st
import requests
import zipfile
import os

# Function to call Gemini API (replace with your actual Gemini API details)
def call_gemini_api(user_input):
    # This is a placeholder URL and headers for the Gemini API
    url = "POST https://us-central1-aiplatform.googleapis.com/v1/projects/AIzaSyC16uwNQRBJej5J34QKk8v_8u_QCu2V-4k/locations/us-central1/publishers/google/models/gemini-1.0-pro:streamGenerateContent?alt=sse"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "input": user_input
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()

# Function to create a zip file from the response
def create_zip(response_data, zip_filename):
    # Create a zip file and add the response data to it
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        # Here we assume response_data is a dictionary with text or other data
        for filename, content in response_data.items():
            # Create a text file for each response item
            with open(filename, 'w') as f:
                f.write(content)
            # Add the text file to the zip
            zipf.write(filename)
            # Remove the text file after adding to zip
            os.remove(filename)

# Streamlit app
st.title("Gemini API Response Generator")

# User input
user_input = st.text_input("Enter your input:")

# Button to trigger the API call and generate the zip file
if st.button("Generate Response"):
    if user_input:
        # Call the Gemini API
        response_data = call_gemini_api(user_input)
        
        # Display the response on the screen
        st.write("API Response:")
        st.json(response_data)
        
        # Create a zip file with the response data
        zip_filename = "response.zip"
        create_zip(response_data, zip_filename)
        
        # Notify the user and provide a download link
        st.success("Response generated successfully!")
        st.download_button(
            label="Download ZIP",
            data=open(zip_filename, 'rb'),
            file_name=zip_filename,
            mime='application/zip'
        )
    else:
        st.error("Please enter some input.")
      
