import os
from dotenv import load_dotenv


load_dotenv("../../.env")

key = os.environ["SUPER_SECRET_KEY"]

masked_key = "*" * len(key[:-3]) + key[-3:]

print("Accessing system with key:", masked_key)
