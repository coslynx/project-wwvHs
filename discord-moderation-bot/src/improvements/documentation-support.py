import discord
from discord.ext import commands

class DocumentationSupport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user} has connected to Discord!')

    @commands.command(name='help')
    async def display_help(self, ctx):
        help_message = "Welcome to the documentation support section!\n" \
                       "Here you can find all the necessary information to manage the bot effectively.\n" \
                       "Please refer to the official documentation for detailed instructions."
        await ctx.send(help_message)

def setup(bot):
    bot.add_cog(DocumentationSupport(bot))