# Kyle Harris
# dis is a the prototype for the Elms Discord Bot.
# THIS IS NOT THE FINAL CODE!!!!!!

from email.mime import message
import os
from urllib import response
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Insert AI here:
from openai import OpenAI

intents = discord.Intents.default()
intents.message_content = True  # Needed if your bot reads message text

# Not needed apparently
#client = discord.Client(intents=intents) 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

bot = commands.Bot(command_prefix='!', intents=intents)



#Insert Commands below here:
@bot.command()
async def hello(ctx):
    """Says hello!"""
    await ctx.send(f'Hello {ctx.author.mention}! 👋')

@bot.command()
async def ping(ctx):
    """Check bot latency"""
    await ctx.send(f'Pong! 🏓 Latency: {round(bot.latency * 1000)}ms')

bot.run(TOKEN)
