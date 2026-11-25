
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing. Please check your .env file.")

client = Groq(api_key=api_key)


def generate_response(user_message):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        raise RuntimeError(
            f"Groq API request failed: {str(e)}"
        ) from e
