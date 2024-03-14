import json
import sys
import requests
import os

from SnsInfo import SnsInfo, Profile
from discord_message import Embed, Author, Image, Message
import os

try:
    TODAY = os.environ["TODAY"]
    print(TODAY)
    os.environ["TODAY"] = "test"
    print(os.environ["TODAY"])
except KeyError:
    TODAY = "Token not available!"
    # or raise an error if it's not available so that the workflow fails