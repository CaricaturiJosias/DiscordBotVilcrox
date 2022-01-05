#This is a discord bot made to annoy a friend, please be gentle 
from asyncio.windows_events import NULL
import discord, os, discord.utils, time
import VilcroxDB as VDB
import checagem as check
from dotenv import load_dotenv
from discord.ext import commands
from discord import FFmpegPCMAudio

load_dotenv()
bot = commands.Bot(command_prefix = "v ", owner_id = 183653926598475776)

DB = VDB.Database()
@bot.before_invoke
async def common(message):
        DB.guild_check(str(message.guild.id), message.guild.name)
        DB.user_check(str(message.author.id), str(message.guild.id), message.author.display_name)
        

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
              

@bot.command(name="mov")
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
@bot.command(name="c")
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
            await Play(ctx, comando, duracao, repeticao)
    except:
                await sair(ctx)
                print("lmao")

async def Play(ctx, comando, duracao, repeticao):
    channel = ctx.author.voice.channel
    if channel != type(None):

        try: 
            vc = await channel.connect()
        except:
            await sair(ctx)

        else:
            try:
                i = 0
                while i < repeticao:
                    vc.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source=f'D:\\Audio_Bot\\{comando}.mp3'))
                    time.sleep(duracao)
                    i += 1
                await register(comando, ctx.author.id, ctx.guild.id, ctx.channel, ctx.channel.voice, repeticao)
                await sair(ctx)
            except:
                await sair(ctx)
                print("lmao")
#####
@bot.command(name="ajuda")
async def ajuda(ctx):
    comandos = DB.comando_list()
    embedV = discord.Embed(title="Comandos do bot", colour=discord.Colour(0x393f2e), url="https://youtu.be/qjnREde32XM")
    embedV.set_author(name="Jon xi nah", url="https://github.com/CaricaturiJosias/DiscordBotVilcrox", icon_url="https://i.redd.it/a1zcxisgjls71.png")
    embedV.set_image(url="http://images7.memedroid.com/images/UPLOADED740/612ee967b8afb.jpeg")
    for k in comandos:
        embedV.add_field(name=f'{k[0]}', value=f'Duracao: {k[1]} segundos', inline=True)
    await ctx.channel.send(embed=embedV)
####

@bot.command(name="novo")
@commands.is_owner()
async def Novo(ctx, arg1, arg2):
    resposta = check.leitura(arg1, arg2)
    if resposta != [0,0]:
        DB.Comando_insert(resposta)

####

async def register(comando, id_user, id_vc, id_canal_texto, id_guild, repeticao):
    await DB.Comando_register(comando, id_user, id_vc, id_canal_texto, id_guild, repeticao)

@bot.command(name="sair")
async def sair(ctx):
    await sair(ctx)


async def sair(ctx):
    await ctx.voice_client.disconnect()

token = os.getenv('token')
bot.run(token)

