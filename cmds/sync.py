#插件導入
from discord.ext import commands
from MainCore.Classes import Cog_Core
# OS => 讀取 .env 檔裡的 TOKEN
# Discord => 本次的重點Package
import discord
import aiohttp

class sync(Cog_Core):
    
    @commands.Cog.listener()
    async def on_message(self, msg):

        #伺服器連動
        async with aiohttp.ClientSession() as session:
            if msg.webhook_id == None:
                UserAvatar = msg.author.avatar_url
                UserName = msg.author.display_name
                Content = msg.content
                
                MyServer = 908594682626469928
                MyServer_Chat = 908594682626469930
                MyServer_Webhook = discord.Webhook.from_url("https://discord.com/api/webhooks/965274765831045211/a8JLzy0tOJDpY_nlyLCpTvL7WDTowr55CkMw63394-z5Pyxud8FzSFJFp69fftdKuTk8", adapter=discord.AsyncWebhookAdapter(session))
                
                SharkParty = 922465596602470420
                SharkParty_Chat = 922873935421390930
                SharkParty_Webhook = discord.Webhook.from_url("https://discord.com/api/webhooks/965258114507083847/He-LV8QtVXQhrIzs3PXHHK7z5Blnwdl10SDEtVUgSPiKsbUaXLlXpdMuHxq3WD3ulhHA", adapter=discord.AsyncWebhookAdapter(session))

                ServerList = []
                ServerList.append(MyServer)
                ServerList.append(SharkParty)
                if msg.guild.id == MyServer:
                    if msg.channel.id == MyServer_Chat:
                        await SharkParty_Webhook.send(content=Content, username=UserName, avatar_url=UserAvatar)
                elif msg.guild.id == SharkParty:
                    if msg.channel.id == SharkParty_Chat:
                        await MyServer_Webhook.send(content=Content, username=UserName, avatar_url=UserAvatar)

def setup(bot):
    bot.add_cog(sync(bot))