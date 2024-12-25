# Import the function to create chunks with overlap from the chunk_util.py
from chunk_util import create_chunks_with_overlap

def main():
    # Define a small string
    small_str = "This is a small string for chunking."
    
    # Call the chunking function to create chunks from the string with overlap
    small_chunks = create_chunks_with_overlap(small_str, chunk_size=12, overlap=4)
    
    # Print each chunk with its ID
    print("Small String Chunks:")
    for i, chunk in enumerate(small_chunks, 1):
        print(f"Chunk id: {i}\n    {chunk}")

if __name__ == "__main__":
    main()
