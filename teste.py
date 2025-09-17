import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("URL")
name = os.getenv("DB_NAME")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
user = os.getenv("USER")
password = os.getenv("PASSWORD")

print(url)
print(name)