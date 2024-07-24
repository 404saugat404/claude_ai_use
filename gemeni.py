import os
import base64
from PIL import Image
import io
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Initialize the Gemini client
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=gemini_api_key)

def resize_image(image_path, max_size=(1024, 1024)):
    with Image.open(image_path) as img:
        img.thumbnail(max_size, Image.DEFAULT_STRATEGY)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG')
        return img_byte_arr.getvalue()

def send_image_to_gemini(image_path, prompt):
    try:
        # Resize and get image bytes
        image_bytes = resize_image(image_path)

        # Set up the model
        model = genai.GenerativeModel('gemini-1.5-flash')


        # Prepare the message
        message = [
            prompt,
            {"mime_type": "image/jpeg", "data": image_bytes}
        ]

        # Send the message to Gemini
        response = model.generate_content(message)

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    image_path = input("Enter the path to your image: ")
    prompt = input("Enter your prompt for the image: ")

    response = send_image_to_gemini(image_path, prompt)
    print("\nGemini's response:")
    print(response)