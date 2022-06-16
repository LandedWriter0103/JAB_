#插件導入
from discord.ext import commands
from MainCore.Classes import Cog_Core
# OS => 讀取 .env 檔裡的 TOKEN
# Discord => 本次的重點Package
import discord

class commands(Cog_Core):

    @commands.command()
    async def help(self, ctx):
        pass

def setup(bot):
    bot.add_cog(commands(bot))