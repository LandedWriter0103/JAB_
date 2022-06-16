#插件導入
from mcipc.query import Client
from discord.ext import commands
# OS => 讀取 .env 檔裡的 TOKEN
# Discord => 本次的重點Package
import discord
import os

#把機器人的Command Prefix設為 = /
bot = commands.Bot(command_prefix="/")

#把預設的 /help 指令移除 => 以便未來自行設計
bot.remove_command("help")

#偵測機器人上線
@bot.event
async def on_ready():
    #傳出 機器人已上線
	print(">>> 機器人已上線 <<<")
    #客製化機器人狀態
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="自主學習"))

#在Discord中 => 載入, 卸載, 重載Cog => 可以減少大量的Debug時間

#載入Cog => /load {Cog名稱}
@bot.command()
async def load(ctx, extension):
	bot.load_extension(f"cmds.{extension}")
	await ctx.send(f"**[ {extension} ]** 載入完畢！") 

#卸載Cog => /unload {Cog名稱}
@bot.command()
async def unload(ctx, extension):
	bot.unload_extension(f"cmds.{extension}")
	await ctx.send(f"**[ {extension} ]** 卸載完畢！")

#重載Cog => /reload {Cog名稱}
@bot.command()
async def reload(ctx, extension):
	bot.reload_extension(f"cmds.{extension}")
	await ctx.send(f"**[ {extension} ]** 重載完畢！")

#找和跑 => Cog檔
for filename in os.listdir("./cmds"):
	if filename.endswith(".py"):
		bot.load_extension(f"cmds.{filename[:-3]}")

#載入密鑰 => 讓Bot活起來
if __name__ == "__main__":
	token = os.getenv("TOKEN")
	bot.run(token)
	
