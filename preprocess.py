from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma


def build_index():
    loader = PyPDFLoader("corpus/hiscox_policy.pdf")
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=4096, chunk_overlap=1024)
    documents = text_splitter.split_documents(data)
    embeddings = OpenAIEmbeddings()
    index = Chroma.from_documents(documents, embeddings)
    return index


if __name__ == "__main__":  # For tests
    build_index()
