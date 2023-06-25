from pyrogram import Client, filters
from pyrogram.types import Message
from db import ext


@Client.on_message(filters.command('start') & filters.private)
async def start(client: Client, message: Message) -> None:
    user_id = message.from_user.id
    name = message.from_user.first_name
    user = ext.get_user(user_id)
    
    if user is None:
        user = ext.add_user(user_id, name)
    
    await message.reply_text(f"Hi {name}")
