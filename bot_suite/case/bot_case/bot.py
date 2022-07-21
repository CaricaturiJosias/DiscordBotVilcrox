#This is a discord bot made to annoy a friend, please be gentle 

from asyncio import wait_for
from asyncio.windows_events import NULL

import discord, discord.utils, time, sys, os
from discord.ext import commands

sys.path.append("D:/Cthings/prog/Bot-Python/bot_suite/tools")
sys.path.append("D:/Cthings/prog/Bot-Python/bot_suite/case/bot_case/util")
import discord_calls as disc
import error_calls as error

dir_path =  os.path.dirname(__file__)
print(dir_path)
bot = commands.Bot(command_prefix = "v ", owner_id = 183653926598475776)   

MensagemProibida = ["lepo","lepo lepo", "kid abelha", "coringatron"]
habibsalvos= [206225035332026368, 338052801286635520, 183653926598475776, 266301388059967489, 266301388059967489]

@bot.event
async def ready_caller():
    disc.ready(bot)

@bot.command(name="urbs") 
async def urbs_caller(message):
    disc.urbs(message)
@urbs_caller.error
async def urbs_error(ctx):
    error.urbs(ctx)


@bot.command(name="PingarVitor")
async def PingarVitor_caller(ctx, arg):
    disc.PingarVitor(ctx, arg)
@PingarVitor_caller.error
async def PingarVitor_error(ctx, error):
    error.PingarVitor(ctx, error)


@bot.command(name="mov")
async def mov_caller(ctx, arg):
    disc.mov(ctx, arg)
@mov_caller.error
async def mov_error(ctx, error):
    error.mov(ctx, error)


@bot.command(name="sair")
async def sair_caller(ctx):
    disc.sair(ctx)
@sair_caller.error
async def sair(ctx, error):
    error.sair(ctx, error)


@bot.command(name="c")
async def é(ctx, *arg):
    disc.é(ctx, *arg)
@é.error
async def é(ctx):
    error.é(ctx, error)


@bot.command(name="ajuda")
async def ajuda_caller(ctx):
    disc.ajuda(ctx)
@ajuda_caller.error
async def ajuda(ctx, error):
    error.ajuda(ctx, error)


@bot.command(name="novo")
@commands.is_owner()
async def Novo(ctx, nome, duracao):
    disc.Novo(ctx, nome, duracao)
@Novo.error
async def Novo(ctx, error):
    error.Novo(ctx, error)
