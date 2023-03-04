from time import time
from datetime import datetime
from pyrogram import __version__, filters, Client
from pyrogram.types import Message
from platform import python_version
from Romeo import SUDO_USER
from config import*

@Client.on_message(
    filters.command(["alive"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def help(client: Client, message: Message):
    start = time()
    current_time = datetime.utcnow()
    uptime = time() - start
    txt = (
        f"❥︎ 𝐀𝐋𝐈𝐕𝐄 ☟︎︎︎\n\n"
        f"🇻𝐄𝐑𝐒𝐈𝐎𝐍 ❥︎ 1.0\n"
        f"🇺𝐏★🇹𝐈𝐌𝐄 ❥︎ {uptime * 1000:.3f}ᴍs\n"
        f"🇵𝐘𝐓𝐇𝐎𝐍 ❥︎ {python_version()}`\n"
        f"🇵𝐘𝐑𝐎𝐆𝐑𝐀𝐌 ❥︎ {__version__}\n"
        f"🇴𝐖𝐍𝐄𝐑 ❥︎ {client.me.mention}"    
    )
    await message.delete()
    await message.reply_photo(photo=ALIVE_PIC, caption=txt)

@Client.on_message(
    filters.command(["ping"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def pingme(client: Client, message: Message):
    r = await message.reply_text("**🇵𝐎𝐍𝐆**")
    start = time()
    current_time = datetime.utcnow()
    uptime = time() - start
    await message.delete()
    await r.edit(
        f"**❂ 🇵𝐎𝐍𝐆 ❂**\n\n"
        f"**🇺𝐏★🇹𝐈𝐌𝐄 ❥︎** {uptime * 1000:.3f}ᴍs\n"
        f"**🇴𝐖𝐍𝐄𝐑 ❥︎** {client.me.mention}"
    )
