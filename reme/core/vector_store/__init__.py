"""vector store"""

from .base_vector_store import BaseVectorStore
from .es_vector_store import ESVectorStore
from .local_vector_store import LocalVectorStore
from .pgvector_store import PGVectorStore
from .qdrant_vector_store import QdrantVectorStore
from ..context import R

# Lazy import for ChromaVectorStore to avoid loading chromadb at startup
# This is needed because chromadb has pydantic v1 compatibility issues with Python 3.14
def get_chroma_vector_store():
    """Lazy import ChromaVectorStore to avoid chromadb import issues."""
    from .chroma_vector_store import ChromaVectorStore
    return ChromaVectorStore

__all__ = [
    "BaseVectorStore",
    "ChromaVectorStore",
    "ESVectorStore",
    "LocalVectorStore",
    "PGVectorStore",
    "QdrantVectorStore",
]

R.vector_stores.register("chroma")(lambda **kwargs: get_chroma_vector_store()(**kwargs))
R.vector_stores.register("es")(ESVectorStore)
R.vector_stores.register("local")(LocalVectorStore)
R.vector_stores.register("pgvector")(PGVectorStore)
R.vector_stores.register("qdrant")(QdrantVectorStore)
