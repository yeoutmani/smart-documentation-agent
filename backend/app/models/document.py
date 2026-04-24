from pydantic import BaseModel
from typing import Optional


class DocumentBase(BaseModel):
    """Base model for documents"""
    title: str
    content: str
    description: Optional[str] = None


class Document(DocumentBase):
    """Document model"""
    id: int
    
    class Config:
        from_attributes = True
