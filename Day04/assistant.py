#Memory enabled AI assistant using OpenAI API
from openai import OpenAI
from dotenv import load_dotenv
import os
from tool_manager import execute_tool

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
 