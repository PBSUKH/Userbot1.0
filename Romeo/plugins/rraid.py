import random
from typing import Tuple
from pyrogram import Client
from pyrogram import filters
from traceback import format_exc
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import (
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message)
from Romeo.helper.mongo import raidub_info, rraid, runraid
from Romeo.helper.data import RAID, VERIFIED_USERS
from Romeo import SUDO_USER

async def get_chats(client: Client):
    """Iter Your All Chats"""
    chats = []
    async for dialog in client.get_dialogs():
        if dialog.chat.type in ["supergroup", "channel"]:
            chats.append(dialog.chat.id)
    return chats
'''
async def iter_chats(client: Client):
    """Iter Your All Chats"""
    chats = []
    async for dialog in client.iter_dialogs():
        if dialog.chat.type in ["supergroup", "channel"]:
            chats.append(dialog.chat.id)
    return chats
'''

def get_user(message: Message, text: str) -> [int, str, None]:
    """Get User From Message"""
    if text is None:
        asplit = None
    else:
        asplit = text.split(" ", 1)
    user_s = None
    reason_ = None
    if message.reply_to_message:
        user_s = message.reply_to_message.from_user.id
        reason_ = text if text else None
    elif asplit is None:
        return None, None
    elif len(asplit[0]) > 0:
        if message.entities:
            if len(message.entities) == 1:
                required_entity = message.entities[0]
                if required_entity.type == "text_mention":
                    user_s = int(required_entity.user.id)
                else:
                    user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        else:
            user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        if len(asplit) == 2:
            reason_ = asplit[1]
    return user_s, reason_
async def edit_or_send_as_file(
    text: str,
    message: Message,
    client: Client,
    caption: str = "`Result!`",
    file_name: str = "result",
    parse_mode="md",
):
    """Send As File If Len Of Text Exceeds Tg Limit Else Edit Message"""
    if not text:
        await message.edit("`Wait, What?`")
        return
    if len(text) > 1024:
        await message.edit("`OutPut is Too Large, Sending As File!`")
        file_names = f"{file_name}.text"
        open(file_names, "w").write(text)
        await client.send_document(message.chat.id, file_names, caption=caption)
        await message.delete()
        if os.path.exists(file_names):
            os.remove(file_names)
        return
    else:
        return await message.edit(text, parse_mode=parse_mode)
def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

@Client.on_message(filters.command(["replyraid", "rraid", "rr"], ".") & (filters.private | filters.user(SUDO_USER)))
async def replyraid(client: Client, message: Message):
    raid = await message.reply_text("`Processing..`")
    text_ = get_text(message)
    user, reason = get_user(message, text_)
    failed = 0
    if not user:
        await raid.edit("`Reply To User Or Mention To Activate Replyraid `")
        return
    try:
        userz = await client.get_users(user)
    except:
        await raid.edit(f"`404 : User Doesn't Exists In This Chat !`")
        return
    if not reason:
        reason = "Private Reason!"
    mee= await client.get_me()
    if userz.id == mee.id:
        await raid.edit("`Jaa Na  Kahe Dimag Kha rha? Khudpe Raid kyu laga rha?`")
        return
    if await raidub_info(userz.id):
        await raid.edit("Reply Raid Already Activated on that User`")
        return
    if int(userz.id) in SUDO_USER:
        await raid.edit("Abe chal that guy part of my devs.")
        return
    if int(userz.id) in VERIFIED_USERS:  
        await raid.edit("Abe chal that guy part of my devoloper.")
        return
    await raid.edit("`Please, Wait Fectching Using Details!`")
  #  chat_dict = await get_chats(client)
 #   chat_len = len(chat_dict)
 #   if not chat_dict:
  #      raid.edit("`You Have No Chats! So Sad`")
  #      return
    await raid.edit("`Activating Replyraid....!`")
    await rraid(userz.id, reason)
    ab = f"Reply Raid has Been Activated On {userz.first_name}"
    await raid.edit(ab)

@Client.on_message(filters.command(["dreplyraid", "drraid", "drr"], ".") & (filters.private | filters.user(SUDO_USER)))
async def dreplyraid(client: Client, message: Message):
    raid = await message.reply_text("`Processing..`")
    text_ = get_text(message)
    user = get_user(message, text_)[0]
    failed = 0
    if not user:
        await raid.edit("`Reply To User Or Mention To Deactivate Replyraid`")
        return
    try:
        userz = await client.get_users(user)
    except:
        await raid.edit(f"`404 : User Doesn't Exists!`")
        return
    mee= await client.get_me()
    if userz.id == mee.id:
        await raid.edit("`Soja Lomde`")
        return
    if not await raidub_info(userz.id):
        await raid.edit("`When I Replyraid Activated? On That User?:/`")
        return
    await raid.edit("`Please, Wait Fectching User details!`")
 #   chat_dict = await get_chats(client)
  #  chat_len = len(chat_dict)
  #  if not chat_dict:
 #       raid.edit("`You Have No Chats! So Sad`")
 #       return
    await raid.edit("`De-Activating Replyraid Raid....!`")
    await runraid(userz.id)
    dab = f"**De-activated Replyraid Raid [{userz.first_name}](tg://user?id={userz.id})"
    await raid.edit(dab)
