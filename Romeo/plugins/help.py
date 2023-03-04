from pyrogram import Client, filters
from pyrogram.types import Message

from Romeo import SUDO_USER
from config import *

@Client.on_message(
    filters.command(["help"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def help(client: Client, message: Message):
    await message.reply_text("wait..")
    CD = """
`.ping` - chek bot alive or not
`.spam` - .spam (count) (message)
`.sspam` - .sspam (count) (reply massage)
`.delayspam` - .delayspam (time in second) (count) (text)
`.uff` - reply any documents 
`.help` - To get commands
`.restart` - restart the bot
"""
    await message.delete()
    await message.reply_photo(photo=ALIVE_PIC, caption=CD)
