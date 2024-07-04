import discord

class MultiServerSupport:
    def __init__(self):
        self.servers = {}

    async def add_server(self, server_id):
        if server_id not in self.servers:
            self.servers[server_id] = {}
            return True
        return False

    async def remove_server(self, server_id):
        if server_id in self.servers:
            del self.servers[server_id]
            return True
        return False

    async def get_server_settings(self, server_id):
        if server_id in self.servers:
            return self.servers[server_id]
        return None

    async def update_server_settings(self, server_id, settings):
        if server_id in self.servers:
            self.servers[server_id] = settings
            return True
        return False

    async def get_all_servers(self):
        return self.servers.keys()