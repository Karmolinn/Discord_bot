import os
import discord
from discord.ext.commands import Bot

TOKEN = 'NTE4MTAwNTA4NjkxNTI5NzM5.DxomZQ.AR9DQ3pSLwU7eNhF_l3wa8cME-M'

BOT_PREFIXES = ('!')
mybot = Bot(command_prefix=BOT_PREFIXES)

@mybot.command(pass_context=True)
async def save_image(context,message):
        imglist = os.listdir("$$$save_image")

mybot.run(TOKEN)






