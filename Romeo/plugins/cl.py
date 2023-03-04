import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *
from Romeo import app
from config import *
#cloner
@app.on_message(filters.private & filters.command("cl", ["/", ".", "!"]))
async def cl(app, message):
    k = await message.reply_text("Usage:\n\n`/cl` pyro-session(V2)")
    token = message.command[1]
    try:
        await k.edit("Booting Your Client")
        r = Client(name="rj", api_id=API_ID, api_hash=API_HASH, session_string=token, plugins=dict(root="Romeo/plugins"))
        await r.start()
        user = await r.get_me()
        await k.edit(f"""
 𝐘𝐨𝐮𝐫 𝐂𝐥𝐢𝐞𝐧𝐭 𝐇𝐚𝐬 𝐁𝐞𝐞𝐧 𝐒𝐮𝐜𝐜𝐞𝐬𝐟𝐮𝐥𝐥𝐲 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐀𝐬 ☟︎︎︎ 
 𝐈𝐝 ❥︎ {user.id}
 𝐍𝐚𝐦𝐞 ❥︎ {user.first_name}
 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 ❥︎ @{user.username}
 ✅✅✅
""")
    except Exception as e:
        await k.edit(f"**ERROR:** `{str(e)}`")

MESSAGE = """
❥︎ 𝐒𝐓𝐀𝐑𝐓 ☟︎︎︎

𝐇𝐞𝐥𝐥𝐨, 
𝐈'𝐦 𝐚 𝐑𝐨𝐦𝐞𝐨 
𝐔𝐬𝐞𝐫𝐁𝐨𝐭 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐇𝐞𝐫𝐞.
"""

#start
@app.on_message(filters.command("start", ["/", ".", "!", "?"]) & filters.private)
async def start(client, message):

 #  await message.reply_text("Hey RomeoBot Assistant here")

   buttons = [
            [
                InlineKeyboardButton("• 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 •", url="t.me/RomeoBot_op"),
            ],
            [
                InlineKeyboardButton("• 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 •", url="t.me/Romeo_op"),
            ],
            ]
   reply_markup = InlineKeyboardMarkup(buttons)
   await client.send_photo(message.chat.id, photo=ALIVE_PIC, caption=MESSAGE, reply_markup=reply_markup)
