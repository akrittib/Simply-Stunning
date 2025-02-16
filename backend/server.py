import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

# Set the Gemini API key from environment variables
gemini_key = os.getenv("GEMINI_API_KEY")

if not gemini_key: 
    raise ValueError("Your Gemini API key is either missing or incorrect.")

# Initialize Gemini API client
client = genai.Client(api_key=gemini_key,
                      http_options={'api_version': 'v1alpha'})

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

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

    response = client.models.generate_content(
        model="gemini-2.0-flash",  # Ensure you have access to this model
        contents=[
            system_prompt,
            user_message
        ]
    )

    bot_response = response.text
    
    return jsonify({"bot_response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)  # Change this to False during production