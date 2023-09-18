from pyrogram import Client
from config import API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN, STRING_SESSION
from datetime import datetime
import time
from aiohttp import ClientSession

spam_chats = []
SUDO_USER = SUDO_USERS
SUDO_USERS.append(OWNER_ID)
aiosession = ClientSession()

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Romeo/plugins"),
    in_memory=True,
)

if not API_ID:
   print("WARNING ⚠️  API_ID NOT FOUND PLZ ADD.")

if not BOT_TOKEN:
   print("WARNING ⚠️  API_HASH NOT FOUND PLZ ADD.")

if not BOT_TOKEN:
   print("WARNING ⚠️ BOT TOKEN NOT FOUND PLZ ADD.")
   
if STRING_SESSION:
   print("[INFO] STRING_SESSION: Found.. Starting.. Client..")
   client1 = Client(name="one", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION, plugins=dict(root="Romeo/plugins"))
