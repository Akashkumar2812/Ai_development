from retriver import (load_documents, retrieve)
#documents = load_documents()
# for name, content in documents.items():
#     print(f"File Name: {name}")
#     print(f"Content: {content}")
#     print("-" * 40)
#it's a simple search to demonstate the retriever functionality. It searches for  the keyword "Python" in the loaded documents and returns the filename and content of the matching document.
filename, content = retrieve("python")
print(filename)
print()
print(content)

