import guilded
import random
import asyncio
import os
import datetime
import time
import socket
import math
import psutil
import logging
from guilded import Member
from guilded.ext import commands 
bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    print('Yuno is running')

logger = logging.getLogger('guilded')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='yuno.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)




# If you're using a userbot, you would use UserbotBot() instead.


#Need to see if a normal user can ban or not since permission checking is not a thing yet.
#@bot.command()
#async def ban(ctx, user: guilded.Member, *, reason): # The person banning someone has to ping the user to ban, and input a reason. Remove self if you are outside a cog.
   # await ctx.guild.ban(user, reason=reason) # Bans the user.
    #await ctx.send(f"{user} has been successfully banned.") # messages channel to tell everyone it worked


#@bot.event
#async def on_message_delete(message):
    # Mention the user who's message got deleted, and send the content
    #await message.channel.send(f"I see you :miku_stare: {message.author.mention}: {message.content}")

@bot.command()
async def gm(ctx):
	author = ctx.author
	guild = ctx.guild
	em = guilded.Embed(title='Good morning <@{}>'.format(author.id), color=0x363942)
	hug = ("https://media.discordapp.net/attachments/451185459016630273/579517792286539784/good_morning.png")
	em.set_image(url=hug)
	await ctx.send(embed=em)

@bot.command()
async def test(ctx):
    await ctx.send(f'My ping is {round (bot.latency * 1000)} ms')
@bot.command()
async def ping(ctx):
    await ctx.send('pong!')
@bot.command()
async def stats(ctx):
    bedem = guilded.Embed(title = 'System Resource Usage', description = 'See CPU and memory usage of the system.')
    bedem.add_field(name = 'CPU Usage', value = f'{psutil.cpu_percent()}%', inline = False)
    bedem.add_field(name = 'Memory Usage', value = f'{psutil.virtual_memory().percent}%', inline = False)
    bedem.add_field(name = 'Available Memory', value = f'{psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}%', inline = False)
    await ctx.send(embed = bedem)

@bot.command(name='8ball')
async def _8ball(ctx):
    response = [
    "yes",
    "maybe",
    "I dont know",
    "Of course.",
    "Nope",
    "UwU",
    ]
    await ctx.send(f"{random.choice(response)}")


bot.run('token_here')
