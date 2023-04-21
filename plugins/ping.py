from pyrogram import Client, filters
from pyrogram.types import Message


# Define a ping command handler
@Client.on_message(filters.command('ping') & filters.private)
async def ping(client: Client, message: Message) -> None:
    """
    Handler for the /ping command in private chats.
    """
    # when using Pyrogram's Client methods, you may encounter exceptions such as
    # pyrogram.errors.FloodWait when hitting rate limits
    # pyrogram.errors.Unauthorized when encountering authorization issues, or
    # pyrogram.errors.NetworkError when facing network connectivity issues
    # Handling these exceptions properly can help your code to be more robust and resilient.
    try:
        await message.reply_text("pong")
    except Exception as e:
        # Handle any exceptions that may occur during execution
        print(f"Error handling /ping command: {e}")
