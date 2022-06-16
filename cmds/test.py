#Only For Testing Code 
#Ignore it
from discord.ext import commands
from MainCore.Classes import Cog_Core

import discord
import asyncio

class test(Cog_Core):
    @commands.command()
    async def countdown(self, ctx):
        for i in range(10):
            await ctx.send(i)
            await asyncio.sleep(15)

    @commands.command()
    async def recall(self, ctx):
        await ctx.send("Bot Is Now Usable")

def setup(bot):
    bot.add_cog(test(bot))