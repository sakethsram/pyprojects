# Import the necessary functions to read the text file and chunk the text
from utils import create_chunks

def read_text_file(file_path):

    # Read and return the content of the file as a string
    with open(file_path, 'r', encoding='utf-8') as file:
        file_text = file.read()
    return file_text

def main():
    file_path = "chunks_for_text_file.txt"
    
    # Read the file content
    file_text = read_text_file(file_path)
    print(file_text) 
    #Get chunks with overlap from the text
    text_chunks = create_chunks(file_text, chunk_size=250, overlap=150)

    # Print the chunks
    # print("Text File Chunks:")
    for idx, chunk in enumerate(text_chunks, 1):
        print(f"Chunk id: {idx}")
        print(f"    {chunk}\n")

if __name__ == "__main__":
    main()
