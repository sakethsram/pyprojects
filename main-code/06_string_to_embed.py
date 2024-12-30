import fitz
from vertexai.language_models import TextEmbeddingModel
import fitz
from vertexai.language_models import TextEmbeddingModel
from utils import create_chunks, display_chunk_info , process_text_and_display_info , final ,generate_bert_embeddings

model = SentenceTransformer('all-MiniLM-L6-v2')
# Load the pretrained embedding model once, so it can be reused.
t='6.pdf'
chunks=create_chunks(t,100,50)
for i, chunk in enumerate(chunks, 1):
        print(f"Chunk id: {i}\n  {chunk}")
