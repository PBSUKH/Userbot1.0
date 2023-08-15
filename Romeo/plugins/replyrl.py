from pyrogram import filters, Client
from traceback import format_exc
from typing import Tuple
import asyncio
import random
from pyrogram import Client
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import (
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message)
from Romeo.helper.data import RAID, LOVE, GROUP, VERIFIED_USERS
from Romeo.helper.mongo import loveub_info, raidub_info
from Romeo import SUDO_USER

@Client.on_message( ~filters.me & filters.incoming)
async def watch_raids(client: Client, message: Message):
    if not message:
        return
    if not message.from_user:
        return
    user = message.from_user.id
    userr = await client.get_users(message.from_user.id)
    mention = f"[{userr.first_name}](tg://user?id={userr.id})"
    raid = f"{mention} {random.choice(RAID)}"
    love = f"{mention} {random.choice(LOVE)}"
    if int(user) in VERIFIED_USERS:
        return
    elif int(user) in SUDO_USER:
        return
    if int(message.chat.id) in GROUP:
        return
    if await raidub_info(user):
        try:
            await message.reply_text(raid)
        except:
            return
    if await loveub_info(user):
        try:
            await message.reply_text(love)
        except:
            return
