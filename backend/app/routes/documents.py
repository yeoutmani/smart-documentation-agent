from fastapi import APIRouter
from app.models.document import Document, DocumentBase

router = APIRouter(prefix="/api/v1/documents", tags=["documents"])


@router.get("/", response_model=list[Document])
async def list_documents():
    """List all documents"""
    return []


@router.post("/", response_model=Document)
async def create_document(document: DocumentBase):
    """Create a new document"""
    return {"id": 1, **document.dict()}


@router.get("/{doc_id}", response_model=Document)
async def get_document(doc_id: int):
    """Get a specific document"""
    return {"id": doc_id, "title": "Document", "content": ""}
