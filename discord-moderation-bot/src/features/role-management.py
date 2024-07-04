import discord
from discord.ext import commands

class RoleManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='assign_role')
    async def assign_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.add_roles(role)
            await ctx.send(f"Role {role.name} has been assigned to {member.display_name}.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    @commands.command(name='remove_role')
    async def remove_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.remove_roles(role)
            await ctx.send(f"Role {role.name} has been removed from {member.display_name}.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

    @commands.command(name='list_roles')
    async def list_roles(self, ctx, member: discord.Member):
        try:
            roles = [role.name for role in member.roles]
            await ctx.send(f"{member.display_name} has the following roles: {', '.join(roles)}")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

def setup(bot):
    bot.add_cog(RoleManagement(bot))