#Memory enabled AI assistant using OpenAI API
from openai import OpenAI
from dotenv import load_dotenv
import os
from tool_manager import execute_tool
from tools import (
    get_current_time,
    roll_dice,
    generate_password,
    read_text_file
)
# this is to load the environment variables from the .env file
load_dotenv()
# Initialize the OpenAI client with the base URL and API key from environment variables
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("=" * 40)
print("       My AI Assistant")
print("=" * 40)
role={
    "1": "You are a friendly school teacher. Explain every concept using simple language and real-life examples.",  
    "2": "You are a senior Python developer. Explain programming concepts clearly and always include Python examples.",
    "3": "You are an experienced travel guide. Recommend places, food, transportation and travel tips.",
    "4": "You are a motivational coach. Encourage the user and give practical advice with a positive attitude.",
    "5": "You are a professional interviewer. Ask one interview question at a time and provide feedback after each answer."
}
print("\nChoose Your Assistant\n")
print("1. Teacher")
print("2. Python Expert")
print("3. Travel Guide")
print("4. Motivational Coach")
print("5. Interviewer")
choice = input("\nEnter your choice : ")
messages = [
    {
        "role": "system",
        "content": role.get(
            choice,
            "You are a helpful assistant."
        )
    }
]
while True:

    user_input = input("\nYou: ")
    text = user_input.lower()
    if text.startswith("summarize"):
        file_name =user_input[10:].strip()
        file_content = read_text_file("data/"+ file_name)
        prompt = f"""Summarize the following content:
         Document:
        {file_content}"""
        response = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages= [
                {"role": "system", "content": role.get(choice, "You are a helpful assistant.")},
                {"role": "user", "content": prompt}
            ]
        )
        ai_response = response.choices[0].message.content
        print("\nAI:", ai_response)
        continue
    if text.startswith("ask"):
            parts = user_input.split(maxsplit=2)
            print(parts)
            file_name = parts[1]
            question = parts[2]
            file_content = read_text_file("data/"+ file_name)
            prompt = f""" you are given a document.
            Answer the users questions based on the information 
            present in the document. If the answer is not present in the document,
            respond with "I Couldn't Find the answer in the document".

             Document:
            {file_content}
            Question:
            {question}
            """
            response = client.chat.completions.create(
                model=os.getenv("MODEL"),
                messages= [
                    {"role": "system", "content": role.get(choice, "You are a helpful assistant.")},
                    {"role": "user", "content": prompt}
                ]
            )
            ai_response = response.choices[0].message.content
            print("\nAI:", ai_response)
            continue
    execute_tool_response = execute_tool(user_input) 
    if execute_tool_response:
        print("\nAI:", execute_tool_response)
        continue
   
    messages.append(
        {"role": "user", "content": user_input}
        )

    if user_input.lower() in ["exit", "quit"]:
        print("\nAI: Exiting the chat. Goodbye!")
        break
 
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages= messages
        
    )
    ai_response = response.choices[0].message.content
    messages.append(
        {"role": "assistant", "content": ai_response}
    )
    
    print("\nAI:", ai_response)
 