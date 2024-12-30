# Import required library for reading PDFs
import fitz  # PyMuPDF
from utils import create_chunks_with_overlap

def read_pdf_page(file_path, page_number=0):
    # Open the PDF file and read the specified page
    with fitz.open(file_path) as pdf_document:
        page = pdf_document.load_page(page_number)
        page_text = page.get_text("text")
    return page_text

def main():
    pdf_path = "pdfs-and-textfiles/1.pdf"
    page_number = 0  # Start with the first page (page_number starts from 0)

    # Read the first page of the PDF
    page_text = read_pdf_page(pdf_path, page_number)

    # Get chunks from the PDF page text
    pdf_chunks = create_chunks_with_overlap(page_text, chunk_size=250, overlap=80)

    # Print out the chunks
    print("PDF Page Chunks (First Page):")
    for idx, chunk in enumerate(pdf_chunks, 1):
        print(f"Chunk id: {idx}")
        print(f"    {chunk}\n")

if __name__ == "__main__":
    main()
