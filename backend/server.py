from flask import Flask, request, jsonify, render_template
import openai
import os 
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPEN_API_KEY") 

app = Flask(__name__)

openai.api_key = os.getenv() #need to get key

if not openai.api_key: 
    raise ValueError("Your OpenAI API key is either missing or incorrect.")

@app.route(" ") #left blank beacuse don't have a URL for our website yet 
def home(): 
    return render_template("index.html") # might need to chnage this too if we end up using a diffrent file

@app.route (" ") # need to specify the route for handeling chatbot interactions and the endpoints
def chat():
    user_message = request.json.get() #need to imput the message sent from frontend
    
    response = openai.ChatCompletion.create(
        model= "gpt-4", #still need to get key so this may change
        messages= [{"role": "user", "content": user_message}]   
    )

    bot_response = response["choices"][0]["message"]["content"]
    
    return jsonify({"bot_response": bot_response})

if __name__ == "__main__":
    app.run(debug=True) #chnage this to flase during production
    

