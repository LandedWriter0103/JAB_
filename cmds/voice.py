#插件導入
from discord.ext import commands
from MainCore.Classes import Cog_Core
# OS => 讀取 .env 檔裡的 TOKEN
# Discord => 本次的重點Package
import discord

class voice(Cog_Core):

    #語音房進出通知
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, after, before):

        #變數
        Target_User = member.name
        VC_Join = str(after.channel)
        VC_Leave = str(before.channel)
        TC_IN_OUT = self.bot.get_channel(980750990934413352)
        VC_BlackList = []
        VC_BlackList.append(980762407976730684) #temp
        VC_BlackList.append(0) #temp
            
        #進入語音房
        if VC_Join == str(None):
            embed=discord.Embed(color=0x00aaaa)
            embed.set_author(name=f"{Target_User} 進入了語音房", icon_url=member.avatar_url)
            await TC_IN_OUT.send(embed=embed)

        #離開語音房
        if VC_Leave == str(None):
            embed=discord.Embed(color=0xb99090)
            embed.set_author(name=f"{Target_User} 離開了語音房", icon_url=member.avatar_url)
            await TC_IN_OUT.send(embed=embed)
                
            #把沒有人的語音房刪除
            if after.channel.members == []:
                if after.channel.id not in VC_BlackList:
                    await after.channel.delete()

    @commands.Cog.listener()
    async def on_message(self, msg):

        #用指令創造語音頻道
        TC_Create = self.bot.get_channel(964414872332951572)
        if TC_Create == msg.channel and msg.author != self.bot.user:
            try:
                if msg.content.startswith("create"):
                    TM_Command = msg.content.split()
                    VC_Name = TM_Command[2]
                    VC_Name = "✿｜" + VC_Name

                    try:
                        VC_Limits = int(TM_Command[4])
                    except:
                        VC_Limits = 0

                    TG = self.bot.get_guild(908594682626469928)
                    CA_Voice = TC_Create.category
                    await TG.create_voice_channel(VC_Name, category=CA_Voice, user_limit=VC_Limits, position=1)
            except:
                await TC_Create.send(content="**格式錯誤了喔** <:Minecraft_Heart:924321182768058369>")

def setup(bot):
    bot.add_cog(voice(bot))
