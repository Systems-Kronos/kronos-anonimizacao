import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("URL")
name = os.getenv("DB_NAME")
ok = "ok"

print(url)
print(name)