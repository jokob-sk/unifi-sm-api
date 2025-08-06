import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
VERSION = os.getenv("VERSION")
VERIFY_SSL = os.getenv("VERIFY_SSL", "true").lower() in ("true", "1", "yes")