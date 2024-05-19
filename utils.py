import os
import base64
import openai  # Corrected the import for OpenAI
import logging
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()

# Retrieve OpenAI API key and Organization ID from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_ORG_ID = os.getenv("OPENAI_ORG_ID")

# Initialize OpenAI client
openai.api_key = OPENAI_API_KEY
openai.organization = OPENAI_ORG_ID

def encode_image(image_path):
    """
    Encodes an image to a base64 string.

    Args:
    - image_path (str): Path to the image file.

    Returns:
    - str: Base64 encoded string of the image.
    """
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        logging.error(f"An error occurred while encoding the image: {e}")
        return None

def analyze_chart(chart_path):
    """
    Analyzes a chart image using OpenAI's GPT-4o model.

    Args:
    - chart_path (str): Path to the chart image file.

    Returns:
    - str: Analysis result from GPT-4o.
    """
    try:
        base64_image = encode_image(chart_path)
        if base64_image:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": "Analyze this chart. Include the symbol and discuss the price action."
                    },
                    {
                        "role": "user",
                        "content": f"data:image/jpeg;base64,{base64_image}"
                    }
                ]
            )
            return response.choices[0].message['content']
        else:
            logging.error("Failed to encode image for analysis.")
            return "Image encoding failed."
    except Exception as e:
        logging.error(f"An error occurred while analyzing the chart: {e}")
        return "Chart analysis failed."

# Example usage (for testing purposes)
if __name__ == "__main__":
    chart_path = "path_to_your_chart_image.jpg"
    result = analyze_chart(chart_path)
    print(result)
