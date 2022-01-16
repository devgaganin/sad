# (C) Arunkumar Shibu 

# January 15th 2022

import os
from pyrogram import Client, filters
from helpers import copy_msg, force_sub



Bot = Client(session_name="forwardfsub",
             api_id=int(os.environ.get("API_ID")),
             api_hash=os.environ.get("API_HASH"),
             bot_token=os.environ.get("BOT_TOKEN"))


@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, message):
    await message.reply(f"<b>Hello {message.from_user.mention}</b>")



@Bot.on_message(filters.group)
async def group(bot, message):
    try:
       await force_sub(bot, message)
       if message.document or message.video:
           await copy_msg(message)
       else:
           return
    except Exception as e:
       print(e)
       
    
    
