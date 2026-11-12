
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Groq API Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# AI Model
GROQ_MODEL = "openai/gpt-oss-120b"

# Application Configuration
APP_NAME = "AI Code Reviewer"
APP_VERSION = "1.0.0"

# Validate API Key
if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. Please configure your .env file."
    )
