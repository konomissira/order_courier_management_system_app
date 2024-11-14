import psycopg2 as psycopg
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Connection
try:
    conn = psycopg.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT")
    )
    cursor = conn.cursor()
    print("Database connection established successfully.")
except psycopg.OperationalError as e:
    print(f"Failed to connect to the database: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
