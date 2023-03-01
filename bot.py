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

resourceTables = {}

#Prints a given dictionary
def dictString(dict):
  output = ""
  for key, value in dict.items():
    output = output + (key + ": " + str(value) + "\n")
  return output

@tree.command(name="ping", description="test command")
async def ping(interaction):
  await interaction.response.send_message("pong")

#this is the generic template for creating drop table embeds - will probably delete/comment out
@tree.command(name="template", description="template for pulling resources")
async def template(interaction):
  embedVar = discord.Embed(title="<item> best drop tables", color=0x00ff00)
  embedVar.add_field(name= "<best location>", value="<rate w/ unit>\n<average runs/kills>\n<average time?>", inline=False)
  await interaction.response.send_message(embed=embedVar)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  print("syncing commands")
  await tree.sync()
  print("commands are Ready!")

client.run(DISCORD_TOKEN)
