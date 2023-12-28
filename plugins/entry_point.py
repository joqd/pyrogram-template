from pyrogram import Client, filters
from pyrogram.types import Message
from pony.orm import db_session
from datetime import datetime
import models


@Client.on_message(filters.all, group=-10)
async def gate(_, message: Message) -> None:
    with db_session():
        user = models.User.get(id=str(message.from_user.id))
        if not user:
            models.User(id=str(message.from_user.id), joined_at=datetime.now())


@Client.on_message(filters.command('start') & filters.private)
async def start(client: Client, message: Message) -> None:
    await message.reply_text(f"Hi {message.from_user.first_name}")
