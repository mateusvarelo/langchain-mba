from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path

# Path(__file__).parent localiza a pasta onde o seu script .py está
caminho_v2 = Path(__file__).parent / "gpt5.pdf"

loader = PyPDFLoader(str(caminho_v2))
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

chunks = splitter.split_documents(docs)

print(len(chunks))
