from configparser import ConfigParser
from pyrogram import Client

# Read configuration from config.ini file
config = ConfigParser()
config.read('auth.ini')

# Extract API credentials from the configuration
api_id = config.get('bot', 'api_id')
api_hash = config.get('bot', 'api_hash')
bot_token = config.get('bot', 'bot_token')

# Create a Pyrogram Client instance
client = Client(
    name='client',
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

# Main entry point of the program
if __name__ == '__main__':
    # Start the Pyrogram Client and automatically close the session when finished
    with client:
        # Get the details of the bot account
        bot = client.get_me()
        print(f"{bot.username} started")
    client.run()
