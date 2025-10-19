import os
from dotenv import load_dotenv

load_dotenv()

# External API configuration
CAT_FACT_API = os.getenv("CAT_FACT_API")
API_TIMEOUT = int(os.getenv("API_TIMEOUT"))  # default 5 seconds
