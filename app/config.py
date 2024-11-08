# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Use environment variables in your code
GOOGLE_SHEETS_CREDENTIALS_PATH = os.getenv("GOOGLE_SHEETS_CREDENTIALS_PATH")
