import asyncio, discord, json
from discord.ext import commands

class RoleCommands:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print("RoleCommands is Loaded")

def setup(bot):
    bot.add_cog(RoleCommands(bot))