# Gemini Vision Chatbot
This is a Generative AI-based chatbot that leverages Google's Gemini model for creating responses based on both textual prompts and images. The application is built using Streamlit to provide an interactive interface and allows users to input text and images to generate AI-driven responses.

 # Project Structure
 ├── gemini_vision.py        # Main Python script to run the chatbot
├── .env                    # Environment variables for sensitive keys
├── requirements.txt        # Dependencies required to run the project
└── README.md               # Documentation (this file)

# Features
Takes textual input from the user.
Option to upload image files in formats like jpeg, jpg, png.
Uses Google's Gemini Generative AI to generate responses.
Displays the uploaded image and generated AI response interactively.

# DEMO
![Chatbot Interface](assets/demo-screenshot.png)



# Installation & Setup
Prerequisites
Before running this application, ensure that you have the following installed on your local machine:

Python 3.8+
pip (Python package installer)
A Google Cloud API key for accessing the Gemini model.
Steps to Run the Application

# Clone the Repository: Clone the project repository from GitHub to your local machine.
git clone https://github.com/your-username/gemini-vision-chatbot.git
cd gemini-vision-chatbot

# Install Dependencies: Install the required Python libraries using the requirements.txt file.
pip install -r requirements.txt

# Setup API Key:

# Create a .env file in the root directory.
Add your Google API key to the .env file as shown below:
GOOGLE_API_KEY=your_google_api_key

# Run the Application: Use Streamlit to run the application locally.
streamlit run gemini_vision.py

# File Upload Limitations
Image files must be in one of the following formats: jpeg, jpg, png.

# Environment Variables
The application relies on a .env file to store your sensitive API key. You must configure your .env file correctly:
GOOGLE_API_KEY=your_google_api_key

Installing Google Generative AI Client
If you're using the Google Generative AI for the first time, ensure you follow the steps on Google Cloud's official page to create your account and generate the API key.

# Dependencies
All required dependencies are listed in the requirements.txt file. Here's a summary:

streamlit: For creating the front-end of the application.
python-dotenv: To load environment variables from a .env file.
PIL: Python Imaging Library for handling images.
google-generativeai: The Python library to interact with Google's Gemini model.

# To Install All Dependencies
pip install -r requirements.txt

# Running Locally
Once all dependencies are installed, you can launch the chatbot on your browser using:streamlit run gemini_vision.py

# Usage Instructions
Open the web app in your browser (automatically opens after running the app with Streamlit).
Enter your text prompt in the input box.
Optionally, upload an image.
Click Submit to generate a response from the AI.
The chatbot will generate a response based on your input, and if an image is uploaded, the AI will use both the text and image to generate a response.

# Contributing
If you wish to contribute to this project, feel free to submit a pull request. Make sure to follow best practices in coding and documentation.

# License
This project is licensed under the MIT License - see the LICENSE file for details.