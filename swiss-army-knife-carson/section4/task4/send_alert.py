import os
import requests
from dotenv import load_dotenv


load_dotenv("../.env")


webhook_url = os.environ["DISCORD_WEBHOOK_URL"]


message = {
    "content": "WARNING: This is a test alert from my Ubuntu system."
}


response = requests.post(webhook_url, json=message)


if response.status_code == 204:
    print("Alert sent.")
else:
    print("Alert failed.")
