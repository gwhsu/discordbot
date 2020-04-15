# -*- coding:utf-8 -*-
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')


@bot.event
async def on_ready():
    print(">>Bot is online")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(699955053255196752)
    await channel.send(f'{member}join!')
    print(F'{member}join!')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(699955080841003018)
    await channel.send(f'{member}join!')
    print(F'{member}join!')


@bot.command()
async def ping(ctx):
    await ctx.send('拉進來打出去')


@bot.command()
async def ping(ctx):
    await ctx.send(f'{bot.latency*1000}(ms)')


bot.run('Njk5OTQxMTA0Nzg2NjA0MDMz.XpbuEg.gkbvNvcERSypDmz8shgN4ZHfS3c')