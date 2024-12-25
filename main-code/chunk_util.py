def create_chunks_with_overlap(text, chunk_size=250, overlap=80):
    # Initialize an empty list to store the chunks
    chunks = []
    
    # Convert the text to bytes for chunking
    text_bytes = text.encode('utf-8')
    i = 0
    
    # Loop to create chunks with overlap
    for i in range(0, len(text_bytes) - chunk_size + 1, chunk_size - overlap):
        # Append each chunk to the chunks list
        chunks.append(text_bytes[i:i + chunk_size].strip())
    
    # Check if no chunks were created initially, add the remaining text
    if i == 0:
        chunks.append(text_bytes)
    else:
        # Append the last chunk with the remaining text
        chunks.append(text_bytes[i + chunk_size:].strip())

    # Decode each chunk from bytes back to string and return the list
    return [chunk.decode('utf-8', errors='ignore') for chunk in chunks]
