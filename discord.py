import discord
import yaml

with open("config.yaml", "r") as stream:
    config = yaml.safe_load(stream)

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

if config['message_on_join']:
    @client.event
    async def on_member_join(member):
        for channel_id in config['channel_ids']:
            channel = client.get_channel(channel_id)
            await channel.send(f'{member} has joined the server.')

if config['message_on_leave']:
    @client.event
    async def on_member_remove(member):
        for channel_id in config['channel_ids']:
            channel = client.get_channel(channel_id)
            await channel.send(f'{member} has left the server.')

for bot_token in config['bot_tokens']:
    client.run(bot_token)
