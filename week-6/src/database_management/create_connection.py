import psycopg2 as psycopg
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Connection
conn = psycopg.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT")
)

cursor = conn.cursor()