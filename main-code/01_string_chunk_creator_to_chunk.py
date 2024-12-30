# Import the function to create chunks with overlap from the chunk_util.py
from utils import create_chunks

def main():
    # Define a small string
    small_str = "This is the first class itself."
    
    # Call the chunking function to create chunks from the string with overlap
    small_chunks = create_chunks(small_str, chunk_size=5, overlap=1)
    
    # Print each chunk with its ID
    print("This is the first class itself:")
    for i, chunk in enumerate(small_chunks, 1):
        print(f"Chunk id: {i}\n    {chunk}")

if __name__ == "__main__":
    main()
