from utils import create_chunks  , read_entire_pdf


def main():
    pdf_path = '/home/saketh/pyprojects/pdfs-and-textfiles/3_4_merged.pdf'

    # Read all pages and combine the text into one string
    full_text = read_entire_pdf(pdf_path)

    # Generate chunks from the full text
    chunks = create_chunks(full_text, chunk_size=500, overlap=100)

    # Print the chunks with IDs
    for chunk_id, chunk in enumerate(chunks, 1):
        print(f"Chunk ID: {chunk_id}")
        print(f"{chunk}\n")

if __name__ == "__main__":
    main()
