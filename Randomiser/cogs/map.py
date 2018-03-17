from discord import *
from discord.ext import commands
from random import choice
import datetime
class Map():
    def __init__(self,bot):
        self.bot = bot
        tmp = open("map_list.txt")
        self.list = [i.strip() for i in tmp.readlines()]
        tmp.close()
    @commands.command(pass_context=True)
    async def map(self,ctx):
        map = choice(self.list)
        map = map.split(" ")
        wname = " ".join(map[slice(len(map)-1)])
        wurl = map[(len(map)-1)]
        url = ctx.author.avatar_url
        avatar = ctx.author.default_avatar_url if url == "" else url
        embed = Embed(colour=Colour(eval("0x{0}".format("".join([choice("0123456789abcdef") for i in range(6)])))), timestamp=datetime.datetime.now())
        embed.set_image(url=wurl)
        embed.set_author(name="Random Map!", icon_url="https://cdn.discordapp.com/avatars/424540163579052043/b67d194871881f83a7e67f3ed35a02ea.png?size=1024")
        embed.set_footer(text="Requested by {0}".format(str(ctx.author)), icon_url=avatar)

        embed.add_field(name="Map Chosen:", value=wname)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Map(bot))