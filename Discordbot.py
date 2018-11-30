import discord
from discord.ext.commands import Bot

TOKEN = 'NTE1NTI0MTE3MTk0MDgwMjU3.DtmXJg.xwwK9uDmA3jNUmJnk4fqyO3SnaI'
BOT_PREFIXES = ('!')
mybot = Bot(command_prefix=BOT_PREFIXES)

@mybot.command(aliases=['tere', 'tervist'], pass_context=True)
async def hello(context):
    response = ['tere maailm']

    channel = context.channel
    await channel.send(response + ", " + context.message.author.mention)

mybot.run(TOKEN)
    
