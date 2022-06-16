from mcipc.query import Client

#try:
with Client("mc.yuwuy.com", 25576) as client:
    full_stats = client.stats(full=True)

players = full_stats.players

status = "<:Bot:949197512684740618> 伺服器上線中"

#except:
    #status = "<:Bot:949197512684740618> 伺服器自閉中"

print(full_stats)

#try:
    #for player in players:
        #print(player)

#except:
    #player = ""