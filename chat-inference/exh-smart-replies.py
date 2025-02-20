#!/usr/bin/env python3

import requests
from dotenv import load_dotenv
import os

load_dotenv()

EX_HUMAN_API_KEY = os.getenv("EX_HUMAN_API_KEY")

context = [
    {
        "turn": "user",
        "message": "Hello there. What's your name?"
    },
    {
        "turn": "bot",
        "message": "My name is Cyber Dog, and you are?",
    },
    {
        "turn": "user",
        "message": "My name is Dave. So you are not a human?"
    },
    {
        "turn": "bot",
        "message": "No, I'm not a human. I am a virtual reality traveler and cyber virus fighter.",
    },
    {
        "turn": "user",
        "message": "Wow can you really fight viruses?  What else can you do?"
    }
]

url = "https://api.exh.ai/chatbot/v2/get_smart_replies"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer " + EX_HUMAN_API_KEY
}

response = requests.post(url, json={"context": context, "candidates_num": 4}, headers=headers)
if response.status_code == 200:
    print(response.json()["smart_replies"])
else:
    print(f"Error {response.status_code}: {response.text}")
