from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command(["uff", "oh", "o"], ".") & filters.me)
async def downloader(client: Client, message: Message):
    await message.delete()
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            r = await convert_to_image(message, client)
        else:
            r = await message.reply_to_message.download()
        await client.send_document("me", r)
