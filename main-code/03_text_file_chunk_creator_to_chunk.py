# Import the necessary functions to read the text file and chunk the text
from chunk_util import create_chunks_with_overlap

def read_text_file(file_path):
    # Read and return the content of the file as a string
    with open(file_path, 'r', encoding='utf-8') as file:
        file_text = file.read()
    return file_text

def main():
    file_path = "pdfs-and-textfiles/chunks_for_text_file.txt"
    
    # Read the file content
    file_text = read_text_file(file_path)
    
    # Get chunks with overlap from the text
    text_chunks = create_chunks_with_overlap(file_text, chunk_size=250, overlap=80)

    # Print the chunks
    print("Text File Chunks:")
    for idx, chunk in enumerate(text_chunks, 1):
        print(f"Chunk id: {idx}")
        print(f"    {chunk}\n")

if __name__ == "__main__":
    main()
