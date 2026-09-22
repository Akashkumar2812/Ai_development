from openai import OpenAI
from similarity import cosine_similarity
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

text1 = "Python is a programming language."
text2 = "Pizza is very delicious."
embedding1 = client.embeddings.create(
    model="nomic-embed-text",
    input=text1
).data[0].embedding

embedding2 = client.embeddings.create(
    model="nomic-embed-text",  
    input=text2
).data[0].embedding
#this is the function to calculate the cosine similarity between two vectors. It takes two vectors as input and returns a value between -1 and 1, where 1 indicates that the vectors are identical, 0 indicates that they are orthogonal (i.e., unrelated), and -1 indicates that they are diametrically opposed.   
similarity_score = cosine_similarity(embedding1, embedding2)
print(f"Similarity score between the two texts: {similarity_score:.4f}")


def create_embedding(content):
    embedding = client.embeddings.create(
        model="nomic-embed-text",
        input=content
    ).data[0].embedding
    return embedding
# print(len(embedding1))
# print(len(embedding2))
# print(type(embedding1))
# print(type(embedding2))
