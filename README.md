Image Question Answering with Gemini Flash API

This repository demonstrates how to use the Gemini Flash API in conjunction with LangChain and Python to build a system that can analyze images and provide answers based on the information contained within them.
Features

    Image Analysis: Upload images and the system will analyze them to extract relevant information.
    Question Answering: Provide questions related to the content of the images, and receive answers based on the extracted information.
    Integration with LangChain: Uses LangChain for enhanced language processing and interaction capabilities.

Prerequisites

Before you begin, ensure you have met the following requirements:

    Python 3.x installed
    Gemini Flash API key
    LangChain library installed

Installation

    Clone the Repository

    bash

git clone "link"
cd image-question-answering

Create and Activate a Virtual Environment

bash

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install Dependencies

bash

pip install -r requirements.txt

Setup Environment Variables

Create a .env file in the root directory and add your Gemini Flash API key:

plaintext

    GEMINI_FLASH_API_KEY=your_gemini_flash_api_key

Usage

    Run the Application

    bash

    python app.py

    Upload an Image and Ask a Question

    Navigate to http://localhost:5000 in your browser. You will be able to upload an image and ask a question related to the content of that image.

Code Overview

    app.py: Main application script that handles image upload, question processing, and interaction with the Gemini Flash API.
    utils.py: Contains utility functions for interacting with the Gemini Flash API and LangChain.
    requirements.txt: Lists all the required Python packages.

API Documentation

For detailed information on the Gemini Flash API, refer to the Gemini Flash API Documentation.
Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Contact

For any questions or feedback, please contact your-email@example.com.
