import os
from dotenv import load_dotenv

load_dotenv()

TOKEN: str = os.getenv('TOKEN')
CLIENT_ID: str = os.getenv('CLIENT_ID')
TOKEN_URL: str = os.getenv('TOKEN_URL')

