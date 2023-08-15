from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.gm import *

from Romeo.modules.help import add_command_help
from Romeo import spam_chats


@Client.on_message(filters.command(["morning", "gm", "g"], [".", "?", "/"]) & filters.me)
async def gm(client: Client, message: Message):
    chat_id = message.chat.id
    reply = GGM
    await message.delete()
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}), "
        if usrnum == 4:
            if reply:   
                S = choice(GGM)
                p = f"ㅤ"
                txt = f"{p}\n{usrtxt}\n{p}"
                await client.send_video(chat_id, video=S, caption=txt)
            await sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@Client.on_message(filters.command(["smorning", "sgm", "sg"], [".", "?", "/"]) & filters.me)
async def sgm(client: Client, message: Message):
    chat_id = message.chat.id
    sreply = GGM
    await message.delete()
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id})"
        if usrnum == 1:
            if sreply:
                R = choice(GGM)
                q = f"ㅤ"
                txt = f"{q}\n{usrtxt}\n{q}"
                await client.send_video(chat_id, video=R, caption=txt)
            await sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass
        
'''

@Client.on_message(filters.command(["morning", "gm", "g"], [".", "?", "/"]) & filters.me)
async def gm(client: Client, message: Message):
    chat_id = message.chat.id
    reply = GM
    await message.delete()
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}), "
        if usrnum == 4:
            if reply:   
                r = choice(GM)
                txt = f"{r}\n\n{usrtxt}"
                await client.send_message(chat_id, txt)
            await sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@Client.on_message(filters.command(["smorning", "sgm", "sg"], [".", "?", "/"]) & filters.me)
async def gm(client: Client, message: Message):
    chat_id = message.chat.id
    reply = GM
    await message.delete()
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}), "
        if usrnum == 1:
            if reply:   
                r = choice(GM)
                txt = f"{r}\n\n{usrtxt}"
                await client.send_message(chat_id, txt)
            await sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass
        
'''
