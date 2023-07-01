from pyrogram import Client, filters
from pyrogram.types import Message
from db import do



@Client.on_message(filters.all, group=-1)
async def gate(client: Client, message: Message):
    if not do.get_user(message.from_user.id):
        do.add_user(user_id=message.from_user.id, name=message.from_user.first_name)


@Client.on_message(filters.command('start') & filters.private)
async def start(client: Client, message: Message) -> None:
    await message.reply_text(f"Hi {message.from_user.first_name}")
