#Memory enabled AI assistant using OpenAI API
from openai import OpenAI
from dotenv import load_dotenv
import os
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

# we are setting the role of the assistant and the system message to guide the AI's behavior, the content part is called as called as system prompt which is used to guide the AI's behavior and set the context for the conversation.  
messages = [
    {"role": "system",
    "content": "you are a friendly Aiteacher Expalin every concepts in simple language with real life examples."}
]
while True:

    user_input = input("\nYou: ")
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
    # print("--------------Conversation History--------------")
    # for msg in messages:
    #    print(f"{msg['role'].capitalize()}: {msg['content']}")
    # print("--------------End of Conversation History--------------")   
    print("\nAI:", ai_response)
 