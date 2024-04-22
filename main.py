import os
from dotenv import load_dotenv

load_dotenv()
webhook = os.environ["DISCORD_WEBHOOK"]
print(type(webhook))
print(len(webhook))
