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

conversation_history = {} #Store what's said here

async def on_ready():
    print(f'{client.user} has connected to Discord!')
##########################################################################

@bot.event
async def on_ready():
    print(f'✅ {bot.user} is online and ready!')
    # Optional: change status

    await bot.change_presence(activity=discord.Game(name="with Python!"))

# Add that Microslop (AI) here.
@bot.event
async def on_message(message):

    print(f'✅ {bot.user} Testing!')

    if message.author == bot.user:
        return

##########################################################################
    channel_id = message.channel.id

    # Add user message to memory
    add_to_history(channel_id, "user", message.content)
##########################################################################

    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[{"role":"user","content":message.content},*conversation_history[channel_id]]
    )

    # Store bot reply
    add_to_history(channel_id, "assistant", response.choices[0].message.content)

    await message.channel.send(response.choices[0].message.content)

    print(conversation_history)  # Debug: Print conversation history for this channel

##########################################################################

##########################################################################

    # Allow commands to work
    await bot.process_commands(message)

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
