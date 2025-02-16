import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

# Set the Gemini API key from environment variables
gemini_key = os.getenv("GEMINI_API_KEY")

if not gemini_key:
    st.error("Your Gemini API key is either missing or incorrect.")
    st.stop()

# Initialize Gemini API client
genai.api_key = gemini_key

# Read system prompt from a file
system_path = os.path.join("prompts", "system.txt")
query_path = os.path.join("prompts", "query.txt")

try:
    with open(system_path, "r") as file:
        system_prompt = file.read()

    with open(query_path, "r") as file:
        query_prompt = file.read()

except FileNotFoundError:
    st.error("Prompt files missing")
    st.stop()

# Streamlit app
st.title("Simply Stunning!")
st.header("🌸 Embrace your uniqueness and celebrate your inner beauty with confidence! 💖")

st.subheader("💜 About Simply Stunning!")
st.write("Simply Stunning is all about self-love, body positivity, and mental wellness. Our mission is to empower individuals by providing valuable resources, motivation, and a supportive community.")

st.subheader("💬 Chat with SanaBot")
user_message = st.text_area("Type your message here...")

if st.button("Send"):
    if user_message:
        try:
            response = genai.models.generate_content(
                model="gemini-2.0-flash",  # Ensure you have access to this model
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message},
                ]
            )

            bot_response = response["choices"][0]["message"]["content"]
            st.write(f"**SanaBot:** {bot_response}")

        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a message.")