# App Feature Testing Guide Generator

## Overview

The **App Feature Testing Guide Generator** is a Streamlit-based web application that allows users to upload images and generate a detailed testing guide for app features depicted in those images. This guide includes a description of the test case, pre-conditions, testing steps, and expected results.

## Features

- Upload and process images to generate testing guides.
- Include optional context for refining the generated guide.
- Integration with the Groq API for generating detailed guides based on images and context.

## Prompting Strategy

### General Prompt

The primary goal of the prompt is to generate a comprehensive, step-by-step guide for testing the app feature shown in the uploaded image. The guide should include:


### Optional Context

If additional context is provided by the user via the `context_text` field, this context will be appended to the prompt to enhance the guide. The context will be included as follows:


### Image Handling

To provide a visual reference, the image is converted to base64 and embedded directly in the prompt using the data URL scheme:


### Integration with Groq API

The Groq API is used to generate the testing guide based on the combined prompt and image URL. Ensure to handle any potential errors and provide appropriate feedback if the API request fails.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/shubhamDhapola/generate-testcases.git
   cd generate-testcases
pip install -r requirements.txt
