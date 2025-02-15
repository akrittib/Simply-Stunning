from flask import Flask, request, jsonify, render_template
import openai
import os 
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPEN_API_KEY") 

if not openai.api_key: 
    raise ValueError("Your OpenAI API key is either missing or incorrect.")

app = Flask(__name__)

@app.route(" ") #left blank beacuse don't have a URL for our website yet 
def home(): 
    return render_template("index.html") # might need to chnage this too if we end up using a diffrent file

@app.route (" ") # need to specify the route for handeling chatbot interactions and the endpoints
def chat():
    user_message = request.json.get() #need to imput the message sent from frontend
    
    # Read system prompt from a file
    system_path = os.path.join("prompts", "system.txt")
    query_path = os.path.join("prompts", "query.txt")
    
    try:
        with open(system_path, "r") as file:
            system_prompt = file.read()

        with open(query_path, "r") as file:
            default_query = file.read()

    except FileNotFoundError:
        return jsonify({"error": "Prompt files missing"}), 500

    response = openai.ChatCompletion.create(
        model= "gpt-4o-mini", #still need to get key so this may change
        messages= [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ]   
    )

    bot_response = response["choices"][0]["message"]["content"]
    
    return jsonify({"bot_response": bot_response})

if __name__ == "__main__":
    app.run(debug=True) #chnage this to flase during production
    

