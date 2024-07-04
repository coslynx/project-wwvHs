import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.command()
async def update(ctx):
    await ctx.send('Updating bot...')

@bot.command()
async def bug_fix(ctx):
    await ctx.send('Fixing bugs...')

bot.run('YOUR_BOT_TOKEN')