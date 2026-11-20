from pathlib import Path
from io import BytesIO
from pypdf import PdfReader
from docx import Document as DocxDocument
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

SUPPORTED = {"pdf", "docx", "txt", "md"}


def extract_text(filename: str, payload: bytes) -> str:
    suffix = Path(filename).suffix.lower().lstrip(".")
    if suffix == "pdf":
        reader = PdfReader(BytesIO(payload))
        return "\n".join((page.extract_text() or "") for page in reader.pages)
    if suffix == "docx":
        doc = DocxDocument(BytesIO(payload))
        return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    if suffix in {"txt", "md"}:
        return payload.decode("utf-8", errors="ignore")
    raise ValueError(f"Unsupported file type: {suffix}")


def make_chunks(filename: str, payload: bytes, source_url: str = ""):
    suffix = Path(filename).suffix.lower().lstrip(".")
    splitter = RecursiveCharacterTextSplitter(chunk_size=900, chunk_overlap=150)
    page_texts = []
    if suffix == "pdf":
        reader = PdfReader(BytesIO(payload))
        page_texts = [(i + 1, page.extract_text() or "") for i, page in enumerate(reader.pages)]
    else:
        page_texts = [(None, extract_text(filename, payload))]

    docs = []
    chunk_number = 0
    for page_number, text in page_texts:
        text = text.strip()
        if not text:
            continue
        for part in splitter.split_text(text):
            chunk_number += 1
            metadata = {
                "source": filename,
                "source_url": source_url,
                "chunk": chunk_number,
            }
            if page_number is not None:
                metadata["page"] = page_number
            docs.append(Document(page_content=part, metadata=metadata))
    if not docs:
        raise ValueError("No extractable text found. Scanned PDFs need OCR before upload.")
    return docs
