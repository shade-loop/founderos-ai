import os
from dotenv import load_dotenv
from fireworks.client import Fireworks

load_dotenv()

client = Fireworks(
    api_key=os.getenv("FIREWORKS_API_KEY")
)

MODEL = "accounts/fireworks/models/deepseek-v4-flash"

def ask_llm(prompt: str):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert startup analyst. "
                    "Follow the user's instructions exactly."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=1000
    )

    return response.choices[0].message.content
