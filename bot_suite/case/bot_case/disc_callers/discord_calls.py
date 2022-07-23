from asyncio import wait_for
from asyncio.windows_events import NULL
from multiprocessing.sharedctypes import Value
import discord, discord.utils, time, sys, os, re

from discord.ext import commands
from discord import FFmpegPCMAudio

dir_path =os.path.dirname(__file__)
import youtube_calls as youtube

sys.path.append("D:/Cthings/prog/Bot-Python/bot_suite/tools")
import helpers as help
import constants as const
import fire_con as fire

sys.path.append("D:/Cthings/prog/Bot-Python/bot_suite/case/bot_case/util")
import bot_util as bot


def ready(bot):
    print(str(bot.user)+' has connected to Discord!')
    print('Bot id:')
    print(bot.user.id)

async def urbs(message):
    if message.author.id in const.allowed_users:
        embed_message = discord.Embed(title="Vitor tristão virou manobrista do habib's?", colour=discord.Colour(0x393f2e), url="https://www.youtube.com/watch?v=29Cfu-6QWEk")
        embed_message.set_image(url="https://cdn.discordapp.com/attachments/807369656021024808/807369730435973120/habobs_1.jpg")
        embed_message.set_thumbnail(url="https://cdn.discordapp.com/attachments/807369656021024808/807371639033036820/unknown.png")
        embed_message.set_author(name="Marrone do Bruno e Marrone", url="https://www.youtube.com/watch?v=29Cfu-6QWEk", icon_url="https://cdn.discordapp.com/attachments/807369656021024808/807371275277434890/unknown.png")
        embed_message.set_footer(text="Foto do local por ren...anônimo", icon_url="https://cdn.discordapp.com/attachments/549252054347153439/807369261004750858/logo_habibs_1.jpg")
        embed_message.add_field(name="😱", value="ELE DA RÉ NO QUIBE???", inline=True)
        embed_message.add_field(name= "😱",value="~~sempre deu~~ PARECE QUE SIM", inline=True)
        await message.channel.send(embed=embed_message)
    else:
        await message.channel.send(f'Você não tem permissão para usar esse comando <@{message.author.id}>, bata no vitor se concorda/discorda disso')

async def PingarVitor(ctx, arg):
    words = arg.split()
    for word in words:
        try:
            for i in range (int(word)):
                await ctx.channel.send(f'<@{206225035332026368}>, Não Sabia Que Você Tinha Virado Manobrista Do Habib\'s.')
        except:
            print("Erro ao pingar o vitor... Iniciando caçada 🥵")

async def mov(ctx, arg):
    try:
        canal_antes = ctx.message.author.voice.channel
        guild = ctx.guild
        channel = guild.get_channel(guild.afk_channel.id)
        idVitima = (((arg.split('@'))[1]).split('>'))[0]
        vitima = await guild.fetch_member(int(idVitima))
        await vitima.move_to(channel)
        time.sleep(2)
        await vitima.move_to(canal_antes)
    except Exception as e:
        print(f"Não foi possível mover o usuario {vitima.name}")

async def sair(ctx, bot):
    channel = ctx.author.voice.channel
    try:
        await bot._connection
    except:
        print("Deu não")

async def e(ctx, *arg):
    try:
        duration = NULL
        repetition = 1
        for text in arg:
            result = fire.get_command(text)
            if result > 0:
                comando = text
                duration = result
            if text.isnumeric():
                repetition = int(text)
        try:
            if duration != NULL:
                await bot.Play(ctx, comando, duration, repetition)
        except Exception as e:
                await ctx.channel.send("Deu pra tocar não 🤓")
                print(e)
    except Exception as e:
        print(e)

async def ajuda(ctx):
    embed_message = discord.Embed(title="Comandos do bot", colour=discord.Colour(0x393f2e), url="https://youtu.be/qjnREde32XM")
    embed_message.set_author(name="Jon xi nah", url="https://github.com/CaricaturiJosias/DiscordBotVilcrox", icon_url="https://i.redd.it/a1zcxisgjls71.png")
    embed_message.set_image(url="http://images7.memedroid.com/images/UPLOADED740/612ee967b8afb.jpeg")
    for k in fire.get_commands():
        embed_message.add_field(name=f'{k[0]}', value=f'Duracao: {k[1]} segundos', inline=True)
    await ctx.channel.send(embed=embed_message)

async def Novo(ctx, *arg):
    try:
        print(arg)
        if  len(arg) == 1:
            await ctx.channel.send("🤓?")
            return

        command = arg[0]
        duration = arg[1]

        if help.leitura(command, duration) == [0,0]:
            await ctx.channel.send("Tem algo errado 🤔")
            return

        if fire.insert_command(command, duration) == False:
            await ctx.channel.send("Esse comando já existe\t 🤬💢")
            return

        await ctx.channel.send("Inserido com sucesso 👍")

    except Exception as e:
        print(e)
        await ctx.channel.send("Deu não 😨")

async def delete(ctx, command : str):
    try:
        os.remove(f"D:/Cthings/prog/Bot-Python/audio/{command}.mp3")
        if not fire.delete_command(command):
            await ctx.channel.send("Esse comando não existe 👎")
            return
        print("delete")
        await ctx.channel.send("Comando deletado")
        return

    except Exception as e:
        print(e)
        await ctx.channel.send("Deu não\t🤡")

async def add (ctx, *arg):
    try:
        if len(arg) < 3:
            await ctx.channel.send("Não, não da pra fazer assim\t👀")
            return
        if not re.findall(const.YOUTUBE_REGEX, arg[0]):
            await ctx.channel.send("Esse link não é válido\t🤓")
            return

        link = arg[0]
        command = arg[1]

        if not help.isfloat(float(arg[2])):
            await ctx.channel.send("Duração do comando não válida\t😨")
            return

        duration = arg[2]

        if fire.insert_command(command, duration) == False:
            await ctx.channel.send("Esse comando já existe\t 🤬💢")
            return

        youtube.create_command(command, duration, link)

        await ctx.channel.send("Comando criado\t 🔥🚀🔥")
    except Exception as e:
        print(e)

