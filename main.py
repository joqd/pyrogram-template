from dotenv import load_dotenv
from pyrogram import Client
import os

# Load values from .env file
load_dotenv()

# Get the values of the environment variables
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')

# Check if the required environment variables are set
if not api_id or not api_hash or not bot_token:
    raise ValueError("\033[32mAPI_ID\033[0m, \033[32mAPI_HASH\033[0m, and \033[32mBOT_TOKEN\033[0m environment variables must be set")

# Create a Pyrogram Client instance
client = Client(
    name='client',
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
    plugins=dict(root='plugins')
)

# Main entry point of the program
if __name__ == '__main__':
    # Start the Pyrogram Client and automatically close the session when finished
    with client:
        # Get the details of the bot account
        bot = client.get_me()
        print(f"\033[32m@{bot.username}\033[0m started")
    client.run()
