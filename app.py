from pyrogram import Client
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

client = Client(
    name='client',
    api_id=config['bot']['api_id'],
    api_hash=config['bot']['api_hash'],
    bot_token=config['bot']['bot_token'],
    plugins=dict(root='plugins')
)


if __name__ == '__main__':
    with client:
        bot = client.get_me()
        print(f"\033[32m@{bot.username}\033[0m started")
    client.run()
