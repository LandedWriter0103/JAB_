#載入插件
import discord
from discord.ext import commands

class Cog_Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
