import discord, asyncio, logging, aiohttp, requests, json, time, datetime
from discord.ext import commands
from time import ctime

with open("data.json") as f:
    config = json.load(f)

class Handler:
    def __init__(self, bot):
        self.bot = bot
 
    async def on_command_error(self, ctx, error):
        if isinstance (error, commands.MissingPermissions):
            if ctx.author.id == 373256462211874836:
                try:
                    return await ctx.reinvoke()
                except Exception as e:
                    return await ctx.send(f"```fix\n{e}\n```")
            elif ctx.guild.owner:
                try:
                    return await ctx.reinvoke()
                except Exception as e:
                    return await ctx.send(f"<:tickNo:490607198443929620> ***{e}***")
            return await ctx.send(f"<:tickNo:490607198443929620> ***Sorry, But You Have No Permission(s) for The `{ctx.command}` Command***")
        elif isinstance(error, commands.BotMissingPermissions):
            return await ctx.send(f"<:tickNo:490607198443929620> ***Sorry, But I Don't Have No Permission(s) To Run The `{ctx.command}` Command***")
        elif isinstance(error, commands.NoPrivateMessage):
            return await ctx.send(f"<:tickNo:490607198443929620> Hey, {ctx.command} isn't allowed in DMs, Try It In A Server Please")
        elif isinstance(error, commands.CheckFailure):
            return await ctx.send("***<:tickNo:490607198443929620> These Commands are Only For My Developers***")
        elif isinstance(error, commands.CommandNotFound):
            pass
        else:
            print(error)
            await ctx.send(f"*** <:tickNo:490607198443929620> {error}***")
            
    async def on_guild_join(self, guild):
        try:
            embed = discord.Embed(color=discord.Color(value=0x1c407a))
            embed.set_author(name="Thanks For Inviting Nebula")
            embed.add_field(name="My Prefix is `.`", value=f"[Support](https://discord.gg/Xgt67WV)")
            embed.add_field(name="Need Help?", value="[Click here](https://enternewname.me/nebula/commands)")
            await guild.system_channel.send(embed=embed)
        except:
            pass

    async def on_ready(self):
        print("Handler Is Loaded")
        while True:
            await self.bot.change_presence(activity=discord.Activity(name=f".help in {len(self.bot.guilds)} Servers", url="https://www.twitch.tv/ninja", type=1))
            await asyncio.sleep(15)

        
    async def on_message(self, message):
        if message.author.bot:
            return

    async def on_message_edit(self, old, new):
        await self.bot.process_commands(new)
        # Restricts Bot Users to Use Commands, This is Why This is the Core Of Nebula
def setup(bot):
    bot.add_cog(Handler(bot))