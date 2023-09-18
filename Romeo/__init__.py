from pyrogram import Client
from config import API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN, STRING_SESSION

spam_chats = []
SUDO_USER = SUDO_USERS
SUDO_USERS.append(OWNER_ID)

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Romeo/plugins"),
    in_memory=True,
)

client = Client(
    name="rj",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    session_string=STRING_SESSION,
    plugins=dict(root="Romeo/plugins")
)

