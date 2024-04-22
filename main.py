import json
import sys
import requests
import os

from SnsInfo import SnsInfo, Profile
from discord_message import Embed, Author, Image, Message
import os
from dotenv import load_dotenv

load_dotenv()
try:
    print(os.environ["TODAY"])
except:
    print("TODAY not found")
