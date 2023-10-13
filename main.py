import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send('he' * count_heh)

@bot.command()
async def goodbye(ctx, count_bye = 5):
    await ctx.send('bye' * count_bye)

bot.run('MTE1OTg3OTg3NzExODQwMjU3Mg.GKjfK2.QtgaWW2uvi-YKjPfm-ielXA75KMpjCWMgCBMKQ')
