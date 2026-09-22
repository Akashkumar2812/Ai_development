from openai import OpenAI
from similarity import cosine_similarity
from test_embedding import create_embedding
from dotenv import load_dotenv
from retriver import load_documents
import os

load_dotenv()
#returns list of the documents with thrie content and the file name
documents = load_documents() 
#we are actually embedding all the documents 
document_embeddings = {}
for filename, content in documents.items():
    document_embeddings[filename] = create_embedding(
        content
    )
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)
print("=" * 40)
print("      My AI RAG Assistant")
print("=" * 40)

while True:
    user_input = input("\nYou : ")

    if user_input.lower() == "quit":
        print("\nAI  : Goodbye! Have a great day.")
        break
#here we are creating an embedding for the user input question using the create_embedding function. This embedding will be used to compare with the embeddings of the documents to find the most relevant document based on cosine similarity.
    question_embedding = create_embedding(
        user_input
    )

    best_score = -1
    best_document = None

    for filename, embedding in document_embeddings.items():
        score = cosine_similarity(
            question_embedding,
            embedding
        )
        if score > best_score:
            best_score = score
            best_document = filename
            
    context = documents[best_document]
    prompt= f"""
    Answer the question based on the context below. If the question can't be answered using the context, say "I don't know".
    Context: {context}
    Question: {user_input}
    """  
    response = client.chat.completions.create(
        model = os.getenv("MODEL"),
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    print("\nAI  : " , response.choices[0].message.content)        