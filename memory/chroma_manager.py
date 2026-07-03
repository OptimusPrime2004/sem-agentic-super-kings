"""
ChromaDB Manager
"""

import chromadb

from config.settings import CHROMA_PATH


client = chromadb.PersistentClient(
    path=CHROMA_PATH
)

collection = client.get_or_create_collection(
    "supplier_memory"
)


def add_memory(
    memory_id,
    document,
    metadata=None
):

    collection.add(

        ids=[memory_id],

        documents=[document],

        metadatas=[metadata or {}]

    )


def search_memory(query):

    result = collection.query(

        query_texts=[query],

        n_results=3

    )

    return result