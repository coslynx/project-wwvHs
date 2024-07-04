import discord

class WelcomeMessage:
    def __init__(self, client):
        self.client = client

    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel:
            await channel.send(f'Welcome {member.mention} to the server! Please read the rules and enjoy your stay.')

def setup(client):
    welcome_message = WelcomeMessage(client)
    client.add_cog(welcome_message)