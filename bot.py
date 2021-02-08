import discord
from discord.utils import get
mensagems = {'<@206225035332026368>, O vitor pedi pra voce abrir o portao nao as pernas','<@206225035332026368>, nao sabia que voce tinha virado manobrista do habibs'}
client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
@client.event
async def on_message(message):
    if message.author.id == 183653926598475776:
        if message.content.startswith('urbs'):  
            embedV = discord.Embed(title="Vitor tristão virou manobrista do habib's?", colour=discord.Colour(0x393f2e), url="https://www.youtube.com/watch?v=29Cfu-6QWEk")
            embedV.set_image(url="https://cdn.discordapp.com/attachments/807369656021024808/807369730435973120/habobs_1.jpg")
            embedV.set_thumbnail(url="https://cdn.discordapp.com/attachments/807369656021024808/807371639033036820/unknown.png")
            embedV.set_author(name="Marrone do Bruno e Marrone", url="https://www.youtube.com/watch?v=29Cfu-6QWEk", icon_url="https://cdn.discordapp.com/attachments/807369656021024808/807371275277434890/unknown.png")
            embedV.set_footer(text="Foto do local por:~~renan  vasconcelos~~ anônimo", icon_url="https://cdn.discordapp.com/attachments/549252054347153439/807369261004750858/logo_habibs_1.jpg")
            embedV.add_field(name="😱", value="ELE DA RÉ NO QUIBE???", inline=True)
            embedV.add_field(name= "😱",value="~~sempre deu~~ PARECE QUE SIM", inline=True)
            await message.channel.send(embed=embedV)
        else:
            await message.channel.send("<@206225035332026368>, não sabia que você tinha virado manobrista do habib\'s")
    else:
        if message.content.startswith('urbs'):  
            embedV = discord.Embed(title="Vitor tristão virou manobrista do habib's?", colour=discord.Colour(0x393f2e), url="https://www.youtube.com/watch?v=29Cfu-6QWEk")
            embedV.set_image(url="https://cdn.discordapp.com/attachments/807369656021024808/807369730435973120/habobs_1.jpg")
            embedV.set_thumbnail(url="https://cdn.discordapp.com/attachments/807369656021024808/807371639033036820/unknown.png")
            embedV.set_author(name="Marrone do Bruno e Marrone", url="https://www.youtube.com/watch?v=l68sg3D66lI", icon_url="https://cdn.discordapp.com/attachments/807369656021024808/807371275277434890/unknown.png")
            embedV.set_footer(text="Possivel local do crime", icon_url="https://cdn.discordapp.com/attachments/549252054347153439/807369261004750858/logo_habibs_1.jpg")
            embedV.add_field(name="😱", value="ELE DA RÉ NO QUIBE???", inline=True)
            embedV.add_field(name= "😱",value="~~sempre deu~~ PARECE QUE SIM", inline=True)
            await message.channel.send(embed=embedV)
        else:    
            return
client.run('ODAxMTcwNTI2MTE4MzQ2NzUy.YAcyMg.mVyRGZR1JB8OwFviA4cdR3xgx8A')


