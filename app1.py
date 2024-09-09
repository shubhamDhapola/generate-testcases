import streamlit as st
from groq import Groq
import base64
from PIL import Image
from io import BytesIO
import os


# Function to encode the image to base64, for handling different image formats
def encode_image(image_file):
    # Determine the format of the image based on file extension or content
    format = image_file.format if image_file.format else 'JPEG'  # Default to JPEG 
    buffered = BytesIO()
    image_file.save(buffered, format=format)
    return base64.b64encode(buffered.getvalue()).decode('utf-8'), format.lower()

# Initialize the Groq client with API key
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def analyze_image(base64_image, format, text_context=""):
    try:
        prompt = ("Generate a detailed, step-by-step guide on how to test the app feature depicted in this image. "
                  "Include: Description of the test case, Pre-conditions for testing, Testing Steps, Expected Result. All four parts should have a proper heading")
        if text_context:
            prompt += f" Context: {text_context}"

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/{format};base64,{base64_image}",
                            },
                        },
                    ],
                }
            ],
            model="llava-v1.5-7b-4096-preview",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Failed to analyze the image: {str(e)}"

# Set up Streamlit layout
st.title("App Feature Testing Guide Generator")
uploaded_files = st.file_uploader("Choose images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

context_text = st.text_area("Optional Context", "", height=150)

if uploaded_files:
    for idx, uploaded_file in enumerate(uploaded_files):
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        base64_image, format = encode_image(image)

        if st.button(f"Analyze {uploaded_file.name}", key=f"analyze_button_{idx}"):
            result = analyze_image(base64_image, format, context_text)
            st.write("Generated Testing Guide for " + uploaded_file.name + ":")
            st.write(result)