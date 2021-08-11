import discord, os, discord.utils, time, psycopg2, string
from HabibsDB import conexao, inicio
from dotenv import load_dotenv
from discord.ext import commands
from discord import FFmpegPCMAudio
load_dotenv()

bot = commands.Bot(command_prefix = "h ")
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
@commands.has_any_role(437122446890631168, 437122570563878915, 804899470864023572, 731743081812066334, 447916692912472064, 736291367302594704, 663501855657164814, 374020042360094730)
async def mov(ctx, arg):
    try:
        canal_antes = ctx.message.author.voice.channel
        guild = ctx.guild
        channel = guild.get_channel(206234863747989505)
        idVitima = (((arg.split('!'))[1]).split('>'))[0]
        vitima = await guild.fetch_member(int(idVitima))
        await vitima.move_to(channel)
        time.sleep(2)
        await vitima.move_to(canal_antes)
    except:
        print(f"Não foi possível mover o usuario {vitima.name}")

@mov.error
async def bemtevi(ctx, error):
    await ctx.channel.send(f"Você não possui a permissão necessária para fazer isso, bata no <@{206225035332026368}>"+
                            " para tentar conseguir a permissão")

@bot.command(pass_context = True)
async def vitor(ctx):
    try:
        canal_antes = ctx.message.author.voice.channel
        guild = ctx.guild
        channel = guild.get_channel(206234863747989505)
        vitima = await guild.fetch_member(206225035332026368)
        await vitima.move_to(channel)
        time.sleep(2)
        await vitima.move_to(canal_antes)
    except:
        print("Não foi possível mover o vitor")

@bot.command(pass_context = True)
async def renan(ctx):
    canal_antes = ctx.message.author.voice.channel
    guild = ctx.guild
    channel = guild.get_channel(206234863747989505)
    vitima = await guild.fetch_member(206225185605419008)
    await vitima.move_to(channel)
    time.sleep(2)
    await vitima.move_to(canal_antes)

@bot.command(name="mama")
async def mama(message):
    vc = message.author.voice.channel
    if vc != type(None):
        try: 
            channel = await vc.connect()
        except:
            await sair(vc.connect())
        else:
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\mama.mp3"))
            time.sleep(3.2)
            await sair(channel)
    else:
        await message.channel.send("Você não está em um canal de voz")


@bot.command(name="oof")
async def oof(message):
    vc = message.author.voice.channel
    if vc != type(None):
        try: 
            channel = await vc.connect()
        except:
            await sair(vc.connect())
        else:
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\oof.mp3"))
            time.sleep(0.5)
            await sair(channel)
    else:
        await message.channel.send("Você não está em um canal de voz")

@bot.command(name="bemtevi")
async def bemtevi(ctx, arg):
    #try:
        #conexao(con, ctx.author.name, ctx.author.id)
    #except:
    #    print("Conexão não foi possível")
    vc = ctx.author.voice.channel
    if vc != type(None):
        try: 
            channel = await vc.connect()
        except:
            sair(vc)
        else:
            try:
                i = 0
                while i<int(arg):
                    channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\bemtevi.mp3"))
                    time.sleep(1.45)
                    i += 1
                await sair(channel)
            except:
                print("Não conseguiu cantar")
            await sair(channel)
    else:
        await ctx.channel.send("Você não está em um canal de voz")

@bemtevi.error
async def bemtevi(ctx, error):
    if isinstance(error,commands.MissingRequiredArgument):
        try: 
            vc = ctx.author.voice.channel
            channel = await vc.connect()
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\bemtevi.mp3"))
            time.sleep(1.3)
            await sair(channel)
        except:
            sair(vc)

@bot.command(name="sokser")
async def sokser(ctx, arg):
    vc = ctx.author.voice.channel
    if vc != type(None):
        try: 
            channel = await vc.connect()
        except:
            sair(vc)
        else:
            try:
                i = 0
                while i<int(arg):
                    channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\sokser.mp3"))
                    time.sleep(2.5)
                    i += 1
                await sair(channel)
            except:
                print("Não conseguiu cantar")
            await sair(channel)
    else:
        await ctx.channel.send("Você não está em um canal de voz")

@sokser.error
async def sokser(ctx, error):
    if isinstance(error,commands.MissingRequiredArgument):
        try: 
            vc = ctx.author.voice.channel
            channel = await vc.connect()
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\sokser.mp3"))
            time.sleep(2.5)
            await sair(channel)
        except:
            sair(vc)

@bot.command(name="socser")
async def socser(message):
    vc = message.author.voice.channel
    if vc != type(None):
        try: 
            channel = await vc.connect()
        except:
            await sair(vc.connect())
        else:
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\socser.mp3"))
            time.sleep(15)
            await sair(channel)
    else:
        await message.channel.send("Você não está em um canal de voz")

@bot.command(name="max")
async def max(message):
    vc = message.author.voice.channel
    if vc != type(None):
        try: 
            channel = await vc.connect()
        except:
            await sair(vc.connect())
        else:
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\max.mp3"))
            time.sleep(28)
            await sair(channel)
    else:
        await message.channel.send("Você não está em um canal de voz")

@bot.command(name="coringa")
async def coringa(message):
    vc = message.author.voice.channel
    if vc != type(None):
        try: 
            channel = await vc.connect()
        except:
            await sair(vc.connect())
        else:
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\coringa.mp3"))
            time.sleep(15)
            await sair(channel)
    else:
        await message.channel.send("Você não está em um canal de voz")

@bot.command(name="jogos")
async def jogos(message):
    vc = message.author.voice.channel
    if vc != type(None):
        try: 
            channel = await vc.connect()
        except:
            await sair(vc.connect())
        else:
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\jogos.mp3"))
            time.sleep(16.5)
            await sair(channel)
    else:
        await message.channel.send("Você não está em um canal de voz")

@bot.command(name="jogos?")
async def jogos(message):
    vc = message.author.voice.channel
    if vc != type(None):
        try: 
            channel = await vc.connect()
        except:
            await sair(vc.connect())
        else:
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\jogoss.mp3"))
            time.sleep(17.1)
            await sair(channel)
    else:
        await message.channel.send("Você não está em um canal de voz")

@bot.command(name="sexta")
async def rico(message):
    vc = message.author.voice.channel
    if vc != type(None):
        try: 
            channel = await vc.connect()
        except:
            await sair(vc.connect())
        else:
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\sexta.mp3"))
            time.sleep(29.75)
            await sair(channel)
    else:
        await message.channel.send("Você não está em um canal de voz") 

@bot.command(name="quinta")
async def rico(message):
    vc = message.author.voice.channel
    if vc != type(None):
        try: 
            channel = await vc.connect()
        except:
            await sair(vc.connect())
        else:
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\quinta.mp3"))
            time.sleep(6)
            await sair(channel)
    else:
        await message.channel.send("Você não está em um canal de voz") 

@bot.command(name="rico")
async def rico(message):
    vc = message.author.voice.channel
    if vc != type(None):
        try: 
            channel = await vc.connect()
        except:
            await sair(vc.connect())
        else:
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\rico.mp3"))
            time.sleep(6)
            await sair(channel)
    else:
        await message.channel.send("Você não está em um canal de voz")        

@bot.command(name="li")
async def li(message):
    vc = message.author.voice.channel
    if vc != type(None):
        try: 
            channel = await vc.connect()
        except:
            await sair(vc.connect())
        else:
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\pc.mp3"))
            time.sleep(6.5)
            await sair(channel)
    else:
        await message.channel.send("Você não está em um canal de voz")

@bot.command(name="intro")
async def intro(ctx, arg):
    vc = ctx.author.voice.channel
    if vc != type(None):
        try: 
            channel = await vc.connect()
        except:
            sair(vc)
        else:
            try:
                i = 0
                while i<int(arg):
                    channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\intro.mp3"))
                    time.sleep(6.5)
                    i += 1
                await sair(channel)
            except:
                print("Não conseguiu cantar")
            await sair(channel)
    else:
        await ctx.channel.send("Você não está em um canal de voz")

@intro.error
async def intro(ctx, error):
    if isinstance(error,commands.MissingRequiredArgument):
        try: 
            vc = ctx.author.voice.channel
            channel = await vc.connect()
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\intro.mp3"))
            time.sleep(6.5)
            await sair(channel)
        except:
            sair(vc)

@bot.command(name="whatsapp")
async def whatsapp(message):
    vc = message.author.voice.channel
    if vc != type(None):
        try: 
            channel = await vc.connect()
        except:
            await sair(vc.connect())
        else:
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\whatsapp.mp3"))
            time.sleep(2)
            await sair(channel)
    else:
        await message.channel.send("Você não está em um canal de voz")

@bot.command(name="parabains")
async def parabains(message):
    vc = message.author.voice.channel
    if vc != type(None):
        try:
            channel = await vc.connect()
        except:
            await sair(vc)
        else:   
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\parabains.mp3"))
            time.sleep(11.3)
            await sair(channel)
    else:
        await message.channel.send("Você não está em um canal de voz")

@bot.command(name="hamster")
async def hamster(message):
    vc = message.author.voice.channel
    if vc != type(None):
        try:
            channel = await vc.connect()
        except:
            sair(vc)
        else:
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\hamster.mp3"))
            time.sleep(3.7)
            await sair(channel)
    else:
        await message.channel.send("Você não está em um canal de voz")

@bot.command(name="hatsune")
async def hatsune(message):
    vc = message.author.voice.channel
    if vc != type(None):
        try:   
            channel = await vc.connect()
        except:
            sair(vc)
        else:
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\hatsune.mp3"))
            time.sleep(3.8)
            await sair(channel)
    else:
        await message.channel.send("Você não está em um canal de voz")

@bot.command(name="kkkk")
async def kkkk(ctx, arg):
    vc = ctx.author.voice.channel
    if vc != type(None):
        try: 
            channel = await vc.connect()
        except:
            sair(vc)
        else:
            try:
                i = 0
                while i<int(arg):
                    channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\topgear.mp3"))
                    time.sleep(1.5)
                    i += 1
                await sair(channel)
            except:
                print("Não conseguiu peidar")
    else:
        await ctx.channel.send("Você não está em um canal de voz")

@kkkk.error
async def kkkk(ctx, error):
    if isinstance(error,commands.MissingRequiredArgument):
        try: 
            vc = ctx.author.voice.channel
            channel = await vc.connect()
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\topgear.mp3"))
            time.sleep(1.5)
            await sair(channel)
        except:
            sair(vc)

@bot.command(name="fart")
async def fart(ctx, arg):
    vc = ctx.author.voice.channel
    if vc != type(None):
        try: 
            channel = await vc.connect()
        except:
            sair(vc)
        else:
            try:
                i = 0
                while i<int(arg):
                    channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\fart.mp3"))
                    time.sleep(2)
                    i += 1
                await sair(channel)
            except:
                print("Não conseguiu peidar")
    else:
        await ctx.channel.send("Você não está em um canal de voz")

@fart.error
async def fart(ctx, error):
    if isinstance(error,commands.MissingRequiredArgument):
        try: 
            vc = ctx.author.voice.channel
            channel = await vc.connect()
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\fart.mp3"))
            time.sleep(2)
            await sair(channel)
        except:
            sair(vc)
        
@bot.command(name="bonequinha")
async def bonequinha(message):
    vc = message.author.voice.channel
    if vc != type(None):
        try:
            channel = await vc.connect()
        except:
            sair(vc)
        else:
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\boneca.mp3"))
            time.sleep(3)
            await sair(channel)
    else:
        await message.channel.send("Você não está em um canal de voz")

@bot.command(name="eeeeh")
async def eeeeh(ctx, arg):
    vc = ctx.author.voice.channel
    if vc != type(None):
        try: 
            channel = await vc.connect()
        except:
            sair(vc)
        else:
            try:
                i = 0
                while i<int(arg):
                    channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\eeeeh.mp3"))
                    time.sleep(1.1)
                    i += 1
                await sair(channel)
            except:
                print("Não conseguiu cantar")
            await sair(channel)
    else:
        await ctx.channel.send("Você não está em um canal de voz")

@eeeeh.error
async def eeeeh(ctx, error):
    if isinstance(error,commands.MissingRequiredArgument):
        try: 
            vc = ctx.author.voice.channel
            channel = await vc.connect()
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\eeeeh.mp3"))
            time.sleep(1)
            await sair(channel)
        except:
            sair(vc)

@bot.command(name="fartr")
async def fartr(ctx, arg):
    vc = ctx.author.voice.channel
    if vc != type(None):
        try: 
            channel = await vc.connect()
        except:
            sair(vc)
        else:
            try:
                i = 0
                while i<int(arg):
                    channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\reverb.mp3"))
                    time.sleep(6.3)
                    i += 1
                await sair(channel)
            except:
                print("Não conseguiu peidar")
    else:
        await ctx.channel.send("Você não está em um canal de voz")

@fartr.error
async def fartr(ctx, error):
    if isinstance(error,commands.MissingRequiredArgument):
        try: 
            vc = ctx.author.voice.channel
            channel = await vc.connect()
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\reverb.mp3"))
            time.sleep(6.3)
            await sair(channel)
        except:
            sair(vc)

@bot.command(name="pex")
async def pex(message):
    vc = message.author.voice.channel
    if vc != type(None):
        try:
            channel = await vc.connect()
        except:
            sair(vc)
        else:
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\pedrero.mp3"))
            time.sleep(8)
            await sair(channel)
    else:
        await message.channel.send("Você não está em um canal de voz")

@bot.command(name="banner")
async def banners(message):
    vc = message.author.voice.channel
    if vc != type(None):
        try:
            channel = await vc.connect()
        except:
            sair(vc)
        else:
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\banner.mp3"))
            time.sleep(5)
            await sair(channel)
    else:
        await message.channel.send("Você não está em um canal de voz")

@bot.command(name="habibs")
async def habibs(message):
    vc = message.author.voice.channel
    if vc != type(None):
        try:
            channel = await vc.connect()
        except:
            sair(vc)
        else:
            channel.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source="C:\\Users\\Gabriel\\Desktop\\prog\\Python\\habibs.mp3"))
            time.sleep(29)
            await sair(channel)
    else:
        await message.channel.send("Você não está em um canal de voz")
#try:
#    con = psycopg2.connect(database="Habibs", user="postgres", password="postgres", host="localhost", port="5432")
#    print("Database opened successfully")
#    inicio(con)
#except:
#    print("Não foi possível iniciar o banco de dados")

@bot.command(name="sair")
async def sair(message):
    await sair(message.channel)

async def sair(vc):
    await vc.disconnect()
token = os.getenv('token')
bot.run(token)

