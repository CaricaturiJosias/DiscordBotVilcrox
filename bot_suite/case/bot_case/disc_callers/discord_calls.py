from asyncio import wait_for
from asyncio.windows_events import NULL
import discord, discord.utils, time, sys, os

from discord.ext import commands
from discord import FFmpegPCMAudio

dir_path =  os.path.dirname(__file__)
print(dir_path)

sys.path.append("D:/Cthings/prog/Bot-Python/bot_suite/tools")
import helpers as help
import constants as const

def ready(bot):
    print(str(bot.user)+' has connected to Discord!')
    print('Bot id:')
    print(bot.user.id)

async def urbs(message):
    if message.author.id in const.allowed_users:
        embedV = discord.Embed(title="Vitor tristão virou manobrista do habib's?", colour=discord.Colour(0x393f2e), url="https://www.youtube.com/watch?v=29Cfu-6QWEk")
        embedV.set_image(url="https://cdn.discordapp.com/attachments/807369656021024808/807369730435973120/habobs_1.jpg")
        embedV.set_thumbnail(url="https://cdn.discordapp.com/attachments/807369656021024808/807371639033036820/unknown.png")
        embedV.set_author(name="Marrone do Bruno e Marrone", url="https://www.youtube.com/watch?v=29Cfu-6QWEk", icon_url="https://cdn.discordapp.com/attachments/807369656021024808/807371275277434890/unknown.png")
        embedV.set_footer(text="Foto do local por ren...anônimo", icon_url="https://cdn.discordapp.com/attachments/549252054347153439/807369261004750858/logo_habibs_1.jpg")
        embedV.add_field(name="😱", value="ELE DA RÉ NO QUIBE???", inline=True)
        embedV.add_field(name= "😱",value="~~sempre deu~~ PARECE QUE SIM", inline=True)
        await message.channel.send(embed=embedV)
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
        print(str(channel))
        idVitima = (((arg.split('!'))[1]).split('>'))[0]
        vitima = await guild.fetch_member(int(idVitima))
        await vitima.move_to(channel)
        time.sleep(2)
        await vitima.move_to(canal_antes)
    except:
        print(f"Não foi possível mover o usuario {vitima.name}")

async def sair(ctx, bot):
    channel = ctx.author.voice.channel
    try:
        await bot._connection
    except:
        print("Deu não")

async def é(ctx, *arg):
    duracao = NULL 
    repeticao = 1
    for text in arg:
        resultado = DB.Comando(text)
        if resultado != 0:
            comando = text
            duracao = resultado

        if text.isnumeric():
            repeticao = int(text)
    try:
        if duracao != NULL:
            if help.checagem(queue, ctx.author.id, ctx.author.name, comando) == 1 and len(queue) == 1:
                await Play(ctx, comando, duracao, repeticao)
                queue.pop(0)
            elif len(queue) > 1:
                await ctx.channel.send("Colocando na queue")
            else:
                await ctx.channel.send("Não foi possível iniciar este comando\nSinto muito")
    except:
                await saida(ctx)

async def ajuda(ctx):
    comandos = DB.comando_list()
    embedV = discord.Embed(title="Comandos do bot", colour=discord.Colour(0x393f2e), url="https://youtu.be/qjnREde32XM")
    embedV.set_author(name="Jon xi nah", url="https://github.com/CaricaturiJosias/DiscordBotVilcrox", icon_url="https://i.redd.it/a1zcxisgjls71.png")
    embedV.set_image(url="http://images7.memedroid.com/images/UPLOADED740/612ee967b8afb.jpeg")
    for k in comandos:
        embedV.add_field(name=f'{k[0]}', value=f'Duracao: {k[1]} segundos', inline=True)
    await ctx.channel.send(embed=embedV)

async def Novo(ctx, nome, duracao):
    print("Arg1 = "+str(nome))
    print("Arg2 = "+str(duracao))
    try: 
        resposta = help.leitura(nome, duracao)
        if resposta != [0,0]:
            DB.Comando_insert(resposta)
            ctx.chanel.send("Inserido com sucesso")
    except:
        print("Erro")