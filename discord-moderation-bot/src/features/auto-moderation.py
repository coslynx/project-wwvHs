import discord
from discord.ext import commands

class AutoModeration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Implement auto-moderation for filtering out inappropriate content
        if message.author == self.bot.user:
            return
        if "inappropriate_word" in message.content:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please refrain from using inappropriate language.")

    @commands.command()
    async def warn(self, ctx, user: discord.Member, *, reason=None):
        # Implement warning functionality
        if user == ctx.author:
            await ctx.send("You cannot warn yourself.")
        else:
            await ctx.send(f"{user.mention} has been warned for {reason}.")

    @commands.command()
    async def mute(self, ctx, user: discord.Member, duration: int, *, reason=None):
        # Implement muting functionality
        if user == ctx.author:
            await ctx.send("You cannot mute yourself.")
        else:
            await ctx.send(f"{user.mention} has been muted for {duration} minutes for {reason}.")

    @commands.command()
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        # Implement kicking functionality
        if user == ctx.author:
            await ctx.send("You cannot kick yourself.")
        else:
            await ctx.send(f"{user.mention} has been kicked for {reason}.")

    @commands.command()
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        # Implement banning functionality
        if user == ctx.author:
            await ctx.send("You cannot ban yourself.")
        else:
            await ctx.send(f"{user.mention} has been banned for {reason}.")

def setup(bot):
    bot.add_cog(AutoModeration(bot))