"""Memory store module for persistent memory management.

This module provides storage backends for memory chunks and file metadata,
including SQLite-based, ChromaDB-based, and pure-Python local implementations
with vector and full-text search.
"""

from .base_memory_store import BaseMemoryStore
from .local_memory_store import LocalMemoryStore
from .sqlite_memory_store import SqliteMemoryStore
from ..context import R

# Lazy import for ChromaMemoryStore to avoid loading chromadb at startup
# This is needed because chromadb has pydantic v1 compatibility issues with Python 3.14
def get_chroma_memory_store():
    """Lazy import ChromaMemoryStore to avoid chromadb import issues."""
    from .chroma_memory_store import ChromaMemoryStore
    return ChromaMemoryStore

__all__ = [
    "BaseMemoryStore",
    "ChromaMemoryStore",
    "LocalMemoryStore",
    "SqliteMemoryStore",
]

R.memory_stores.register("sqlite")(SqliteMemoryStore)
R.memory_stores.register("chroma")(lambda **kwargs: get_chroma_memory_store()(**kwargs))
R.memory_stores.register("local")(LocalMemoryStore)
