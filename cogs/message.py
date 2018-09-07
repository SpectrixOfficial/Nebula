import discord, asyncio, logging, time, datetime
from discord.ext import commands

class MessageManagement:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.has_permissions(manage_messages=True)
    @commands.command(aliases=["purge", "c"])
    async def clear(self, ctx, *, number : int):
        if number > 1000:
            number = 1000
        num = await ctx.channel.purge(limit=number + 1)
        await asyncio.sleep(1)
        await ctx.send(f"Deleted `{len(num) - 1}` messages", delete_after=1.8)
    
def setup(bot):
    bot.add_cog(MessageManagement(bot))