import discord
from discord import app_commands
import os
import random
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="ping", description="test command")
async def ping(interaction)
  interaction.response.send_message("pong")


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  print("syncing commands")
  await tree.sync()
  print("commands are Ready!")

client.run(DISCORD_TOKEN)
