from pyrogram import Client, filters
from pyrogram.types import Message

from Romeo import SUDO_USER
from config import *

@Client.on_message(
    filters.command(["help"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def help(client: Client, message: Message):
    CD = """
   ROMEOBOT HELP MENU
________________________________
           BOT
`.alive` - chek bot alive or not
`.ping` - chek bot ping
`.restart` - restart the bot
`.help` - To get commands

           EMOJI
`.emoji` - .emoji (name)
`.cmoji` - .cmoji (emoji or text) (name)

           RAID 
`.raid` - .raid (count) (username or reply_message)
`.dmraid` - .dmraid (count) (username or reply_message)
`.replyraid` - .replyraid (username or reply_message)
`.lraid` - .lraid (count) (username or reply_message)

           SPAM
`.spam` - .spam (count) (message)
`.sspam` - .sspam (count) (reply_media)
`.delayspam` - .delayspam (time in second) (count) (text)

           CLONE
`.clone` - .clone (reply_message to clone I'd)
`.revert` - .revert (reply_message to cloner for back)
"""
    await message.delete()
    await message.reply_photo(photo=ALIVE_PIC, caption=CD)
