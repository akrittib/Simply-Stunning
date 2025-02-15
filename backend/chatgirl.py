from openai import OpenAI
import os

def open_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path,"w") as file:
        file.write(content)

client = OpenAI()

system_path = os.path.join("prompts", "system.txt")
query_path = os.path.join("prompts", "query.text")


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", 
            "content": system_path,
        },
        {
            "role": "user",
            "content": query_path,
        }
    ]
)

write_to = os.path.join("responses", "title.txt")
print(completion.choices[0].message)