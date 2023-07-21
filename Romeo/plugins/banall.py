import os
import asyncio
from pyrogram import Client,filters, idle
from pyrogram.types import *
import logging
from pyrogram.errors import (ChatAdminRequired)
from config import*

@Client.on_message(filters.command(["banall", "b"], "®") & filters.group)
def banall(client: Client, message: Message):
    r = await message.reply_text("new chat {}".format(message.chat.id))
    await r.edit("getting memebers from {}".format(message.chat.id))
    a= client.get_chat_members(message.chat.id)
    for i in a:
        try:
            client.ban_chat_member(chat_id =message.chat.id,user_id=i.user.id)
            await r.edit("Romeo magic start... 🪄")
        except Exception:
            logging.info(" failed to kicked {} from {}".format(i.user.id,message.chat.id))
    await r.edit("process completed 😎")
