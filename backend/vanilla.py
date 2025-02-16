import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read system prompt from a file
system_path = os.path.join("prompts", "system.txt")
query_path = os.path.join("prompts", "query.txt")

try:
    with open(system_path, "r") as file:
        system_prompt = file.read()

    with open(query_path, "r") as file:
        query_prompt = file.read()

except FileNotFoundError:
    print("Prompt files missing")
    exit(1)

# Simulate user input
user_message = input("Enter your message: ")

# Simulate AI response
def simulate_response(user_message):
    validation = "Thank you for sharing your struggle with me. It's completely valid to feel this way, and it's important to acknowledge your emotions. You're not alone in feeling this way."
    task = "Now, let's focus on a positive task to help you improve your body image. Take a few minutes to journal about three things you appreciate about your body. Reflect on how these aspects contribute to your overall well-being."
    encouragement = "Please let me know when you have completed the task and how it made you feel."
    final_message = "Great job on completing the task! Remember, your body is amazing and deserves love and appreciation. Keep up the positive work, and I'm here to support you every step of the way."
    
    return f"{validation}\n\n{task}\n\n{encouragement}\n\n{final_message}"

bot_response = simulate_response(user_message)
print(f"Simulated AI Response: {bot_response}")