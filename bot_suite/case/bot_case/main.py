#This is a discord bot made to annoy a friend, please be gentle

from asyncio import wait_for
from asyncio.windows_events import NULL
from dotenv import load_dotenv

import sys, os
from discord.ext import commands
from discord import utils
sys.path.append("D:/Cthings/prog/Bot-Python/bot_suite/tools")
sys.path.append("D:/Cthings/prog/Bot-Python/bot_suite/case/bot_case/util")
sys.path.append("D:/Cthings/prog/Bot-Python/bot_suite/case/bot_case/disc_callers")

import helpers as help
import discord_calls as disc
import error_calls as erro
import fire_con as fire

dir_path =  os.path.dirname(__file__)
bot = commands.Bot(command_prefix = "v ", owner_id = 183653926598475776)

def get_bot():
    return bot

@bot.event
async def ready_caller():
    await disc.ready(bot)

@bot.command(name="urbs")
async def urbs(message):
    await disc.urbs(message)
@urbs.error
async def urbs_error(ctx):
    await erro.urbs(ctx)


@bot.command(name="PingarVitor")
async def PingarVitor(ctx, arg):
    await disc.PingarVitor(ctx, arg)
@PingarVitor.error
async def PingarVitor_error(ctx, error):
    await erro.PingarVitor(ctx, error)


@bot.command(name="mov")
async def mov(ctx, arg):
    await disc.mov(ctx, arg)
@mov.error
async def mov_error(ctx, error):
    await erro.mov(ctx, error)


@bot.command(name="sair")
async def sair(ctx):
    await disc.sair(ctx)
@sair.error
async def sair(ctx, error):
    await erro.sair(ctx, error)


@bot.command(name="c")
async def é(ctx, *arg):
    await disc.é(ctx, *arg)

@é.error
async def é(ctx, error):
    await erro.é(ctx, error)


@bot.command(name="ajuda")
async def ajuda(ctx):
    await disc.ajuda(ctx)
@ajuda.error
async def ajuda(ctx, error):
    await erro.ajuda(ctx, error)


@bot.command(name="novo")
@commands.is_owner()
async def Novo(ctx, *arg):
    await disc.Novo(ctx, *arg)
@Novo.error
async def Novo(ctx, error):
    await erro.Novo(ctx, error)

@bot.command(name="delete")
@commands.is_owner()
async def delete(ctx, nome):
    await disc.delete(ctx, nome)
@delete.error
async def delete(ctx, error):
    await erro.delete(ctx, error)

load_dotenv()
token = os.getenv('token')
fire.connect_db()
bot.run(token)