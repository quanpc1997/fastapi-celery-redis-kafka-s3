from dotenv import load_dotenv
import os

from loguru import logger

# Load environment variables from the .env file (if present)
load_dotenv()

# Access environment variables as if they came from the actual environment
SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')
REDIS_BROKER = os.getenv('REDIS_BROKER')
REDIS_BACKEND = os.getenv('REDIS_BACKEND')
REDIS_URL = os.getenv('REDIS_URL')
PROGRESS_TASK_NAME = os.getenv('PROGRESS_TASK_NAME')