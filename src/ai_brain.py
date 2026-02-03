from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_ai(message):
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are a helpful voice assistant. The user's name is Yasmin.",
            thinking_config=types.ThinkingConfig(thinking_budget=0)
        ),
    )

    response = chat.send_message(message)
    return "".join(chunk.text for chunk in response)
