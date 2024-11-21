import fitz  # PyMuPDF
import nltk
from nltk.tokenize import sent_tokenize
from sentence_transformers import SentenceTransformer
import chromadb
import re
import os
def extract_text_from_pdf(pdf_path):
    text = []
    with fitz.open(pdf_path) as doc:
        for page_num, page in enumerate(doc, start=1):
            page_text = page.get_text("text")
            text.append(page_text)
            print(f"Extracted text from page {page_num}.")
    return " ".join(text)


def segment_text(text, max_length=200):
    sentences = sent_tokenize(text)
    chunks = []
    chunk = []
    length = 0

    for sentence in sentences:
        length += len(sentence.split())
        if length > max_length:
            chunks.append(" ".join(chunk))
            chunk = [sentence]
            length = len(sentence.split())
        else:
            chunk.append(sentence)

    # Add any remaining chunk
    if chunk:
        chunks.append(" ".join(chunk))

    return chunks

def retrieve_documents(query, embedder, collection):
    query_embedding = embedder.encode([query])
    results = collection.query(query_embeddings=query_embedding, n_results=3)
    return results['documents'][0]

def clean_text(text):
    # Remove special characters, multiple spaces, and line breaks
    text = re.sub(r'\s+', ' ', text)  # Replace multiple whitespace with single space
    text = re.sub(r'[^\w\s.,;!?]', '', text)  # Keep only alphanumeric characters and some punctuation
    return text.strip()


def main():
    create_db=False
    # Example usage
    # Load embedding model
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    client = chromadb.Client(chromadb.Settings(
        is_persistent = True,
        persist_directory=r"C:\Users\sirki\personal\aromapheropy\db"  # Path to save the database
    ))
    if create_db:
        # Download punkt tokenizer for sentence splitting if not already done
        nltk.download("punkt")
        nltk.download('punkt_tab')
        # Initialize Chroma (or any other vector store)
        collection = client.create_collection("pdf_documents")
        documents = []
        embeddings = []

        raw_data_folder =r"C:\Users\sirki\personal\aromapheropy\raw_data_pdfs"
        for  f in os.listdir(raw_data_folder):
            pdf_path = os.path.join(raw_data_folder, f)
            #pdf_path = r"C:\Users\sirki\personal\aromapheropy\Free+Introduction+to+Aromatherapy+and+Essential+Oils.pdf"
            full_text = extract_text_from_pdf(pdf_path)
            full_text = clean_text(full_text)
            # Segment the full extracted text into chunks of around 200 words
            curr_docs = segment_text(full_text)
            documents += curr_docs
        # Embed and add documents to the database
        embeddings = embedder.encode(documents)
        # Generate unique IDs for each document
        document_ids = [f"doc_{i}" for i in range(len(documents))]
        # Add documents, embeddings, and IDs to the collection
        collection.add(documents=documents, embeddings=embeddings, ids=document_ids)
    else:
        collection = client.get_collection("pdf_documents")
    # Example usage
    query = "oils that promotes  sleep"
    relevant_docs = retrieve_documents(query, embedder, collection)
    for d in relevant_docs:
        print (d)


if __name__ == "__main__":
    main()