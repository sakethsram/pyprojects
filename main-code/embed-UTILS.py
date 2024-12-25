from vertexai.language_models import TextEmbeddingModel
from string_chunk_creator_01 import create_chunks_with_overlap

text_embedding_model = TextEmbeddingModel.from_pretrained("text-embedding-004")

def clean_print(chunk_id, chunk_text, chunk_embedding):
    print(f"chun    k id: {chunk_id}")
    print(f"chunk text: {chunk_text[:50]}...") 
    print(f"chunk's embeddings: {chunk_embedding[:10]}")  # Print the first 10 embedding values
    print()

def text_to_embed(text):
    embeddings = text_embedding_model.get_embeddings([text])
    return embeddings[0].values

def text_to_chunk_embed(text, chunk_size=256, overlap=32):
    chunks = create_chunks_with_overlap(text, chunk_size, overlap)
    chunk_embeddings = []
    
    for idx, chunk in enumerate(chunks, 1):
        embeddings = text_embedding_model.get_embeddings([chunk])
        chunk_embedding = embeddings[0].values
        chunk_embeddings.append((idx, chunk, chunk_embedding))
    
    return chunk_embeddings
