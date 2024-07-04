import discord

class UserActions:
    def __init__(self, client):
        self.client = client

    async def warn_user(self, user, reason):
        await user.send(f'You have been warned for: {reason}')

    async def mute_user(self, user, duration, reason):
        muted_role = discord.utils.get(user.guild.roles, name='Muted')
        await user.add_roles(muted_role)
        await user.send(f'You have been muted for {duration} minutes for: {reason}')

    async def kick_user(self, user, reason):
        await user.kick(reason=reason)
        await user.send(f'You have been kicked for: {reason}')

    async def ban_user(self, user, reason):
        await user.ban(reason=reason)
        await user.send(f'You have been banned for: {reason}')