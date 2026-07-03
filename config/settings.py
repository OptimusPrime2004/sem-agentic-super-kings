import os
from dotenv import load_dotenv

load_dotenv()

# Azure OpenAI
AZURE_API_KEY = os.getenv("AZURE_API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_DEPLOYMENT = os.getenv("AZURE_DEPLOYMENT")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION")
MODEL_NAME = os.getenv("MODEL_NAME")

# ChromaDB
CHROMA_PATH = os.getenv("CHROMA_PATH")

# Streamlit
STREAMLIT_SERVER_PORT = int(os.getenv("STREAMLIT_SERVER_PORT", "8501"))

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")