import json
import sys
import requests
import os

from SnsInfo import SnsInfo, Profile
from discord_message import Embed, Author, Image, Message
import os

try:
    DISCORD_WEBHOOK = os.environ["DISCORD_WEBHOOK"]
    os.environ["DISCORD_WEBHOOK"] = "test"
except KeyError:
    DISCORD_WEBHOOK = "Token not available!"
    # or raise an error if it's not available so that the workflow fails