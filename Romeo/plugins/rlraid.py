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
from Romeo.helper.mongo import loveub_info, rlove, runlove
from Romeo.helper.data import *
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

@Client.on_message(filters.command(["replyloveraid", "rlraid", "rlr"], ".") & (filters.private | filters.user(SUDO_USER)))
async def loveraid(client: Client, message: Message):
    await message.delete()
    m = await message.reply_text("`Processing..`")
    text_ = get_text(message)
    user, reason = get_user(message, text_)
    failed = 0
    if not user:
        await m.edit("`Reply To User Or Mention To Activate LoveRaid `")
        return
    try:
        userz = await client.get_users(user)
    except:
        await m.edit(f"`404 : User Doesn't Exists In This Chat !`")
        return
    if not reason:
        reason = "Private Reason!"
    mee= await client.get_me()
    if userz.id == mee.id:
        await m.edit("`Jaa Na Tharki Kahe Dimag Kha rha? Khudpe Raid kyu laga rha?`")
        return
    if await loveub_info(userz.id):
        await m.edit("`LoveRaid Already Activated on that User:/`")
        return
    await m.edit("`Please, Wait Fectching Using Details!`")
 #   chat_dict = await get_chats(client)
 #   chat_len = len(chat_dict)
#    if not chat_dict:
#        m.edit("`You Have No Chats! So Sad`")
 #       return
    await m.edit("`Activating LoveRaid....!`")
    await rlove(userz.id, reason)
    ab = f"LoveRaid has Been Activated On [{userz.first_name}](tg://user?id={userz.id})"
    await m.edit(ab)
    

@Client.on_message(filters.command(["dreplyloveraid", "drlraid", "drlr"], ".") & (filters.private | filters.user(SUDO_USER)))
async def dreplyramd(client: Client, message: Message):
    await message.delete()
    m = await message.reply_text("`Processing..`")
    text_ = get_text(message)
    user = get_user(message, text_)[0]
    failed = 0
    if not user:
        await m.edit("`Reply To User Or Mention To Deactivate LoveRaid`")
        return
    try:
        userz = await client.get_users(user)
    except:
        await m.edit(f"`404 : User Doesn't Exists!`")
        return
    mee= await client.get_me()
    if userz.id == mee.id:
        await m.edit("`Soja Tharki`")
        return
    if not await loveub_info(userz.id):
        await m.edit("`When I LoveRaid Activated? On That User?:/`")
        return
    await m.edit("`Please, Wait Fectching User details!`")
#    chat_dict = await get_chats(client)
#    chat_len = len(chat_dict)
#    if not chat_dict:
#        m.edit("`You Have No Chats! So Sad`")
#        return
    await m.edit("`De-Activating LoveRaid Raid....!`")
    await runlove(userz.id)
    dab = f"**De-activated LoveRaid Raid [{userz.first_name}](tg://user?id={userz.id})"
    await m.edit(dab)
