from pyrogram import Client
from config import API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN, STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4, STRING_SESSION5, STRING_SESSION6, STRING_SESSION7, STRING_SESSION8, STRING_SESSION9, STRING_SESSION10
from datetime import datetime
import time
from aiohttp import ClientSession

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
SUDO_USER = SUDO_USERS
clients = []
ids = []

SUDO_USERS.append(OWNER_ID)
aiosession = ClientSession()

if API_ID:
   API_ID = API_ID
else:
   print("WARNING: API ID NOT FOUND USING ROMEO API.")
   API_ID = "13335263"

if API_HASH:
   API_HASH = API_HASH
else:
   print("WARNING: API HASH NOT FOUND USING ROMEO API.")   
   API_HASH = "16743e0ded6547061df2f1087fe354df"

if not BOT_TOKEN:
   print("WARNING: BOT TOKEN NOT FOUND PLZ ADD.")   

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Romeo/plugins"),
    in_memory=True,
)

if STRING_SESSION1:
   print("[INFO] STRING_SESSION1: Found.. Starting.. Client1..")
   client1 = Client(name="one", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION1, plugins=dict(root="Romeo/plugins"))
   clients.append(client1)

if STRING_SESSION2:
   print("[INFO] STRING_SESSION2: Found.. Starting.. Client2..")
   client2 = Client(name="two", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION2, plugins=dict(root="Romeo/plugins"))
   clients.append(client2)

if STRING_SESSION3:
   print("[INFO] STRING_SESSION3: Found.. Starting.. Client3..")
   client3 = Client(name="three", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION3, plugins=dict(root="Romeo/plugins"))
   clients.append(client3)

if STRING_SESSION4:
   print("[INFO] STRING_SESSION4: Found.. Starting.. Client4..")
   client4 = Client(name="four", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION4, plugins=dict(root="Romeo/plugins"))
   clients.append(client4)

if STRING_SESSION5:
   print("[INFO] STRING_SESSION5: Found.. Starting.. Client5..")
   client5 = Client(name="five", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION5, plugins=dict(root="Romeo/plugins"))
   clients.append(client5)

if STRING_SESSION6:
   print("[INFO] STRING_SESSION6: Found.. Starting.. Client6..")
   client6 = Client(name="six", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION6, plugins=dict(root="Romeo/plugins"))
   clients.append(client6)

if STRING_SESSION7:
   print("[INFO] STRING_SESSION7: Found.. Starting.. Client7..")
   client7 = Client(name="seven", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION7, plugins=dict(root="Romeo/plugins"))
   clients.append(client7)

if STRING_SESSION8:
   print("[INFO] STRING_SESSION8: Found.. Starting.. Client8..")
   client8 = Client(name="eight", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION8, plugins=dict(root="Romeo/plugins"))
   clients.append(client8)

if STRING_SESSION9:
   print("[INFO] STRING_SESSION9: Found.. Starting.. Client9..")
   client9 = Client(name="nine", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION9, plugins=dict(root="Romeo/plugins"))
   clients.append(client9)

if STRING_SESSION10:
   print("[INFO] STRING_SESSION10: Found.. Starting.. Client10..")
   client10 = Client(name="ten", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION10, plugins=dict(root="Romeo/plugins")) 
   clients.append(client10)
