import fitz
from vertexai.language_models import TextEmbeddingModel
from string_chunk_creator_01 import create_chunks_with_overlap
text_embedding_model = TextEmbeddingModel.from_pretrained("text-embedding-004")


import fitz
from vertexai.language_models import TextEmbeddingModel
from string_chunk_creator_01 import create_chunks_with_overlap

# Load the pretrained embedding model once, so it can be reused.
text_embedding_model = TextEmbeddingModel.from_pretrained("text-embedding-004")

def get_chunk_embeddings(text, page_number=0,chunk_size=256, overlap=32):
     # Step 1: Create chunks from the input text using the external create_chunks_with_overlap function
    chunks = create_chunks_with_overlap(text, chunk_size, overlap)

    # Step 2: Generate embeddings for each chunk using the pretrained model
    chunk_embeddings = []
    for chunk in chunks:
        embeddings = text_embedding_model.get_embeddings([chunk])  # Get embeddings for each chunk
        chunk_embedding = embeddings[0].values  # Extract the embedding values from the result
        chunk_embeddings.append({
            "chunk-text": chunk,
            "chunk-embedding": chunk_embedding
        })

    return chunk_embeddings

def clean_print(chunk_embeddings):
    """
    This function prints the chunk details in a clean and formatted way.
    """
    for i, chunk in enumerate(chunk_embeddings, 1):
        print(f"Chunk ID: {i}")
        print(f"Chunk Text: {chunk['chunk-text'][:50]}...")  # Print the first 50 characters of the chunk text
        print(f"Chunk's Embeddings: {chunk['chunk-embedding'][:5]}")  # Print only the first 5 embedding values
        print()

# Example usage
if __name__ == "__main__":
    text = "This is a small string for chunking."  
    
    # Get chunk embeddings for the provided text
    chunk_embeddings = get_chunk_embeddings(text, chunk_size=256, overlap=32)

    # Print the chunk embeddings with clean format
    clean_print(chunk_embeddings)
