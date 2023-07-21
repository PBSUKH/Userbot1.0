import asyncio
import importlib
from pyrogram import Client, idle
from Romeo.plugins import ALL_MODULES
from Romeo import clients, app, ids

async def start_bot():
    await app.start()
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module("Romeo.plugins" + all_module)
        print(f"Successfully Imported {all_module} 😭")
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await cli.join_chat("RomeoBot_op")
            print(f"Successfully Imported {all_module} 💫")
            print(f"Started {ex.first_name} 🔥")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
            print(f"Successfully Imported {all_module} 😎")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
