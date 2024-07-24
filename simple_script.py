import os
import base64
from PIL import Image
import io
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Anthropic client
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
if not anthropic_api_key:
    raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
client = Anthropic(api_key=anthropic_api_key)

def resize_image(image_path, max_size=(1024, 1024)):
    with Image.open(image_path) as img:
        img.thumbnail(max_size, Image.DEFAULT_STRATEGY)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG')
        return base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')

def send_image_to_claude(image_path, prompt):
    try:
        # Resize and encode the image
        image_base64 = resize_image(image_path)

        # Prepare the message
        message = {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": image_base64
                    }
                },
                {
                    "type": "text",
                    "text": prompt
                }
            ]
        }

        # Send the message to Claude
        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            messages=[message]
        )

        return response.content[0].text

    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    image_path = input("Enter the path to your image: ")
    prompt = input("Enter your prompt for the image: ")

    response = send_image_to_claude(image_path, prompt)
    print("\nClaude's response:")
    print(response)