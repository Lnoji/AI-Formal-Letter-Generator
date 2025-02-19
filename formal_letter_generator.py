import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_letter(recipient, subject, body):
    prompt = (
        f"Generate a formal letter to {recipient} regarding {subject}. "
        f"The letter should include the following details: {body}. "
        "Use a professional tone and proper formatting."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional writer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    recipient = input("Enter recipient: ")
    subject = input("Enter subject: ")
    body = input("Enter letter details: ")
    letter = generate_letter(recipient, subject, body)
    print("Generated Letter:\n", letter)
