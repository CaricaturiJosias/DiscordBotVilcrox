#This is a discord bot made to annoy a friend, please be gentle 
from asyncio.windows_events import NULL
from logging import NullHandler
import discord, os, discord.utils, time, _thread as thread
import HabibsDB as HDB
from dotenv import load_dotenv
from discord.ext import commands
from discord import FFmpegPCMAudio
load_dotenv()
bot = commands.Bot(command_prefix = "h ", owner_id = 183653926598475776)

DB = HDB.Database()
@bot.before_invoke
async def common(message):
       DB.user_check(str(message.author.id), message.author.display_name)

MensagemProibida = ["lepo","lepo lepo", "kid abelha", "coringatron"]
habibsalvos= [206225035332026368, 338052801286635520, 183653926598475776, 266301388059967489, 266301388059967489]
@bot.event
async def on_ready():
    print(str(bot.user)+' has connected to Discord!')
    print('Bot id:')
    print(bot.user.id)

@bot.command(name="PingarVitor")
async def PingarVitor(ctx, arg):
    words = arg.split()
    for word in words:
        try:
            i= 0
            while i<int(word):
                await ctx.channel.send(f'<@{206225035332026368}>, Não Sabia Que Você Tinha Virado Manobrista Do Habib\'s.')
                i += 1
        except:
            print("Erro ao pingar o vitor")

@PingarVitor.error
async def PingarVitor(ctx, error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.channel.send(f'<@{206225035332026368}>, Não Sabia Que Você Tinha Virado Manobrista Do Habib\'s.')

@bot.command(name="urbs")    
async def urbs(message):
    if message.author.id in habibsalvos:
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

@bot.command(pass_context = True)
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

@mov.error
async def mov(ctx):
    await ctx.channel.send(f"Você não possui a permissão necessária para fazer isso, bata no <@{206225035332026368}>"+
                            " para tentar conseguir a permissão (Drop raro [0.005% de não conseguir])")

#####
@bot.command(name="m")
async def m(ctx, *arg):
    duracao = NULL 
    repeticao = 1
    for text in arg:
        resultado = DB.Comando(text)
        if resultado != 0:
            comando = text
            duracao = resultado

        if text.isnumeric():
            repeticao = int(text)
    if duracao != NULL:
        await Play(ctx, comando, duracao, repeticao)

async def Play(ctx, comando, duracao, repeticao):
    channel = ctx.author.voice.channel
    if channel != type(None):

        try: 
            vc = await channel.connect()
        except:
            sair(channel)

        else:
            try:
                i = 0
                while i < repeticao:
                    vc.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source=f'D:\\Audio_Bot\\{comando}.mp3'))
                    time.sleep(duracao)
                    i += 1
                await sair(vc)
            except:
                print("lmao")
#####

####

@bot.command(name="Novo")
@commands.is_owner()
async def Novo(ctx, *arg):
    duracao = NULL 
    for text in arg:
        resultado = DB.Comando(text)
        if resultado == 0:
            comando = text
        try:
            duracao = float(text)
        except:
            continue

    if duracao != NULL:
        print(DB.Comando_insert(comando, duracao))

####

@bot.command
async def sair(vc):
    await sair(vc)


async def sair(vc):
    await vc.disconnect()

token = os.getenv('token')
bot.run(token)

