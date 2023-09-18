import os
import asyncio
from pyrogram import Client,filters, idle
from pyrogram.types import *
import logging
from pyrogram.errors import (ChatAdminRequired)
from config import*
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)

@Client.on_message(filters.command(["banall", "ball"], "®") & (filters.group | filters.user(SUDO_USER)))
def banall(client: Client, message: Message):
    logging.info("new chat {}".format(message.chat.id))
    logging.info("getting memebers from {}".format(message.chat.id))
    a= client.get_chat_members(message.chat.id)
    for i in a:
        try:
            client.ban_chat_member(chat_id =message.chat.id,user_id=i.user.id)
            logging.info("kicked {} from {}".format(i.user.id,message.chat.id))
        except Exception:
            logging.info(" failed to kicked {} from {}".format(i.user.id,message.chat.id))
    logging.info("process completed")
