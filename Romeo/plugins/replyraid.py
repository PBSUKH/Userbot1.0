import asyncio
import random
import asyncio
import time
from typing import Tuple
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import filters, Client
from traceback import format_exc
from typing import Tuple

from Romeo.helper.data import *
from Romeo import SUDO_USER

SUDO_USERS = SUDO_USER

#LOCAL STORAGE
ACTIVATE_LIST = []


# CREATE LINK
def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


#REPLYLOVERAID
@Client.on_message(
    filters.command(["rr", "replyraid"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def rlr(client: Client, message: Message):
    r= await message.edit_text("**Processing**")
    reply = message.reply_to_message
    if reply:
        user = reply.from_user.id
    else:
        user = get_arg(message)
        if not user:
            await r.edit("**Provide Me A USER_ID or reply to someone**")
            return
    user = await client.get_users(user)
    if int(message.chat.id) in GROUP:
        await r.edit("`You Cannnot Spam In DeadlyChats`")
        return
    if int(user.id) in VERIFIED_USERS:
        await r.edit("You Cannot Spam On Developers")
        return
    elif int(user.id) in SUDO_USERS:
        await r.edit("That Guy Is part of sudo user.")
        return
    elif int(user.id) in ACTIVATE_LIST:
        await r.edit("User Already in Raidlist.")
        return
    ACTIVATE_LIST.append(user.id)
    await r.edit(f"**Replyraid Activated On {user.first_name} Successfully ✅**")


#DREPLYLOVERAID
@Client.on_message(
    filters.command(["drr", "dreplyraid"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def drlr(client: Client, message: Message):
    r= await message.edit_text("**Processing**")
    reply = message.reply_to_message
    if reply:
        user = reply.from_user.id
    else:
        user = get_arg(message)
        if not user:
            await r.edit("Provide me username/userid or reply to user for deactivating lovereplyraid")
            return
    user = await client.get_users(user)
    if int(user.id) not in ACTIVATE_LIST:
        await r.edit("User Not in Replyraid.")
        return
    ACTIVATE_LIST.remove(user.id)
    await r.edit(f"**Reply Raid has Been Removed {user.first_name}, enjoy!**")


#WATCHER
@Client.on_message(filters.all)
async def check_del(client: Client, message: Message):
    if not message:
        return
    if int(message.chat.id) in GROUP:
        return
    try:
        if not message.from_user.id in ACTIVATE_LIST:
            return
    except AttributeError:
        return
    try:
        await message.reply_text(f"{random.choice(RAID)}")
    except:
        pass
        return
