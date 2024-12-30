from sentence_transformers import SentenceTransformer# Importing the SentenceTransformer model
import fitz  # PyMuPDF

# Initialize the SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to read PDF and extract text
def read_entire_pdf(file_path):
    full_text = ""
    with fitz.open(file_path) as pdf_document:
        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)
            full_text += page.get_text("text")
    return full_text
# Read the PDF file and extract the text using the file path file_path

# Function to create overlapping chunks
def create_chunks(text, chunk_size, overlap):
    chunks = []
    text_length = len(text)
    
    for i in range(0, text_length, chunk_size - overlap):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
        
        # Stop if the remaining text is smaller than the overlap
        if i + chunk_size >= text_length:
            break
    return chunks
# Created chunks  with overlap


# Function to display the chunks
def print_chunks(chunks):
    for i, chunk in enumerate(chunks, 1):
        print(f"Chunk ID: {i}")
        print(f"Chunk Text: {chunk}")
        print()

# Function to generate BERT embeddings for a list of chunks
def generate_bert_embeddings(chunks: list[str]):
    chunk_embeddings_dict = {}
    for idx, chunk in enumerate(chunks):
        # Generate embedding for the chunk
        embedding = model.encode([chunk])[0]
        # Store the chunk ID (starting from 1), its text, and its embeddings in the dictionary
        chunk_embeddings_dict[idx + 1] = {
            'id': idx + 1,  
            'text': chunk,
            'embedding': embedding
        }
    return chunk_embeddings_dict
    # Generate BERT embeddings for the chunks and create a dictionary

def print_chunk_and_embeddings(chunk_dict):
    for chunk_id, data in chunk_dict.items():
        print(f"Chunk ID: {data['id']}")  # The chunk ID from the dictionary
        print(f"Chunk Text: {data['text'][:50]}...")  # Print only the first few characters
        print(f"Chunk Embeddings: {data['embedding'][:10]}...")  # Print the first 10 embedding values
        print('======================================================================================')

# Function to generate embeddings from a PDF file from scratch
def generate_embeddnigs_from_pdf(file_path):
    fd = read_entire_pdf(file_path)  # Read the PDF file and extract the text using the file path file_path
    chunks = create_chunks(fd, 100,3)  # Create chunks with 500 characters and 50 characters overlap
    #print_chunks(chunks)  # Display the chunks
    
    # Generate BERT embeddings for the chunks and create a dictionary
    chunk_embeddings_dict = generate_bert_embeddings(chunks)
    
    #display the chunks along with their embeddings
    print_chunk_and_embeddings(chunk_embeddings_dict)
    return chunk_embeddings_dict


#test the function
a='/home/saketh/pyprojects/documentation/13.pdf'
res=generate_embeddnigs_from_pdf(a)
