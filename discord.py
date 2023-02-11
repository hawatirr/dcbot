import discord
import json

class DiscordBot:
    def __init__(self, token):
        self.token = token
        self.client = discord.Client()

    async def run(self):
        @self.client.event
        async def on_ready():
            print(f'Logged in as {self.client.user}')

        @self.client.event
        async def on_member_join(member):
            print(f'{member} has joined the server.')

        @self.client.event
        async def on_member_remove(member):
            print(f'{member} has left the server.')

        await self.client.start(self.token)

def load_config(filename):
    try:
        with open(filename, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        return {}

def save_config(filename, config):
    with open(filename, 'w') as f:
        json.dump(config, f, indent=4)

def main():
    config = load_config('config.json')
    tokens = config.get('tokens', [])

    while True:
        token = input('Enter a Discord bot token (or "done" to finish): ')
        if token == 'done':
            break
        tokens.append(token)

    config['tokens'] = tokens
    save_config('config.json', config)

    bots = [DiscordBot(token) for token in tokens]

    for bot in bots:
        bot.run()

if __name__ == '__main__':
    main()
