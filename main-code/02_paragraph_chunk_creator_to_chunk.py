# Import the function to create chunks with overlap from chunk_util.py
from utils import create_chunks_with_overlap

def main():
    # Sample text to chunk
    small = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore
      magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
      consequat.
    """

    # Chunk the paragraph with overlap
    chunks1 = create_chunks_with_overlap(small, chunk_size=75, overlap=60)

    # Print the resulting chunks
    
    for idx, chunk in enumerate(chunks1, 1):
        print(f"Chunk id: {idx}")
        print(f"    {chunk}\n")

# Run the main function
main()
