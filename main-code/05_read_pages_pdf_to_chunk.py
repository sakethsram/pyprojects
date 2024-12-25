# Import required library for reading PDFs
import fitz
from chunk_util import create_chunks_with_overlap

def read_entire_pdf(file_path):
    """Reads and combines text from all pages in a PDF into a single string."""
    full_text = ""
    with fitz.open(file_path) as pdf_document:
        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)
            full_text += page.get_text("text")
    return full_text

def main():
    pdf_path = '/home/saketh/pyprojects/pdfs-and-textfiles/3_4_merged.pdf'

    # Read all pages and combine the text into one string
    full_text = read_entire_pdf(pdf_path)

    # Generate chunks from the full text
    chunks = create_chunks_with_overlap(full_text, chunk_size=500, overlap=100)

    # Print the chunks with IDs
    for chunk_id, chunk in enumerate(chunks, 1):
        print(f"Chunk ID: {chunk_id}")
        print(f"{chunk}\n")

if __name__ == "__main__":
    main()
