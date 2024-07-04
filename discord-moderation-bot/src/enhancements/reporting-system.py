import discord
from discord.ext import commands

class ReportingSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content.startswith('!report'):
            reported_user = message.mentions[0]
            await message.channel.send(f'{message.author.mention} has reported {reported_user.mention} for violating the rules. Moderators will review this report.')

def setup(bot):
    bot.add_cog(ReportingSystem(bot))