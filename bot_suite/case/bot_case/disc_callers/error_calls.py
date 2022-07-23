from asyncio import wait_for
from asyncio.windows_events import NULL
import discord, discord.utils, time, sys, os

from discord.ext import commands
from discord import FFmpegPCMAudio

dir_path =  os.path.dirname(__file__)

sys.path.append("D:/Cthings/prog/Bot-Python/bot_suite/tools")
import helpers as help
import constants as const

async def pingar_vitor(ctx, error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.channel.send(f'<@{206225035332026368}>, Não Sabia Que Você Tinha Virado Manobrista Do Habib\'s.')

async def mov(ctx, error):
    await ctx.channel.send(f"Você não possui a permissão necessária para fazer isso, bata no <@{206225035332026368}>"+
                            " para tentar conseguir a permissão (Drop raro [0.005% de não conseguir])")
    print(error)

async def urbs(ctx, error):
    await ctx.channel.send('Não se pode chamar a grande propaganda da urbs  😂💦')

async def sair(ctx, error):
    await ctx.channel.send('Não foi possível sair')
    print(f"Não foi possível sair do canal {ctx.message.author.voice.channel}")

async def e(ctx, error):
    await ctx.channel.send('Não foi possível iniciar um turbulhão itararé  😛💦')

async def Novo(ctx, error):
    await ctx.channel.send('Houve algum problema inserindo o comando')

async def ajuda(ctx, error):
    await ctx.channel.send('Houve algum problema mostrando os comandos')

async def delete(ctx, error):
    await ctx.channel.send('Houve algum problema deletando o comando')

async def add(ctx, error):
    await ctx.channel.send('Houve algum problema baixando e criando o comando')