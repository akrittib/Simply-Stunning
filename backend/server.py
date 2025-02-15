import os
from flask import Flask, request, jsonify, render_template
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key: 
    raise ValueError("Your OpenAI API key is either missing or incorrect.")

app = Flask(__name__)

@app.route("/")  # Root URL for the home page
def home(): 
    return render_template("index.html")  # Ensure this file exists in the templates folder

@app.route("/chat", methods=["POST"])  # Route for handling chatbot interactions
def chat():
    user_message = request.json.get("message")  # Get the message sent from frontend
    
    # Read system prompt from a file
    system_path = os.path.join("prompts", "system.txt")
    query_path = os.path.join("prompts", "query.txt")
    
    try:
        with open(system_path, "r") as file:
            system_prompt = file.read()

        with open(query_path, "r") as file:
            query_prompt = file.read()

    except FileNotFoundError:
        return jsonify({"error": "Prompt files missing"}), 500

    response = openai.ChatCompletion.create(
        model= "gpt-4o", #still need to get key so this may change
        messages= [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ]   
    )

    bot_response = response["choices"][0]["message"]["content"]
    
    return jsonify({"bot_response": bot_response})

if __name__ == "__main__":
    app.run(debug=True) #chnage this to flase during production

