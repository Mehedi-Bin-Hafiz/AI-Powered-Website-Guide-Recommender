from WebChatbot.daily_scrapping import daily_scraper
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from tqdm import tqdm
# Step 1: Scraping the website data

url = str(input("Give me website link:")).strip()
links_data = daily_scraper(url)
print('Learning the data')

# Step 2: Initialize ChromaDB Client and SentenceTransformerEmbeddingFunction
client = chromadb.Client()
embedding_function = SentenceTransformerEmbeddingFunction(
    model_name="paraphrase-MiniLM-L6-v2")  # Using a Sentence-Transformers model

# Step 3: Create a ChromaDB collection to store the data (if not already exists)
collection = client.create_collection(name="links")

# Step 4: Store embeddings of links' text in ChromaDB
for idx, item in tqdm(enumerate(links_data)):
    text = item['text']
    link = item['link']
    # Generate the embedding for the text
    embedding = embedding_function([text])  # Embedding the text (embedding function expects a list)

    # Generate a unique ID for each entry, here using the index
    doc_id = str(idx)  # Convert index to string to make it a valid ID

    # Add the document with embedding to the ChromaDB collection
    collection.upsert(
        ids=[doc_id],  # Unique ID for each document
        documents=[text],
        metadatas=[{"link": link}],
        embeddings=[embedding[0]],  # Only the first embedding in the list

    )


# Step 5: Function to process user query and find the best matching link
def find_best_link(query):
    # Embed the user query using the same SentenceTransformer model
    query_embedding = embedding_function([query])  # Embed query as a list

    # Perform the search query in the vector database and find the most similar link
    results = collection.query(query_embeddings=query_embedding, n_results=1)
    # Get the link with the highest similarity
    best_link = results['metadatas'][0][0]['link']  # This gives the best match link
    return best_link


# Step 6: Continuous querying with while loop
print('\nLearning complete! Ask me anything or type "exit" to stop:')
while True:
    user_query = input("Enter your query: ")

    # If the user types 'exit', break the loop
    if user_query.lower() == 'exit':
        print("Exiting the chatbot...")
        break

    # Find the best matching link for the user's query
    best_matching_link = find_best_link(user_query)

    # Output the best matching link
    print(f"The best matching link for your query is: {best_matching_link}")
