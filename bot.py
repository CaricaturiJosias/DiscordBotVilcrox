import discord
import asyncio
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Cog, Greedy
from discord.ext.commands import CheckFailure
from discord.ext.commands import command, has_permissions, bot_has_permissions
from dotenv import load_dotenv
import os

load_dotenv()
client = discord.Client()
commands = discord.ext.commands
MensagemProibida = ["lepo","lepo lepo", "kid abelha", "madrid","coringatron"]
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print('Bot id:')
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.id == 206225035332026368:
        if message.content.startswith('urbs'): 
            embedV = discord.Embed(title="Vitor tristão virou manobrista do habib's?", colour=discord.Colour(0x393f2e), url="https://www.youtube.com/watch?v=29Cfu-6QWEk")
            embedV.set_image(url="https://cdn.discordapp.com/attachments/807369656021024808/807369730435973120/habobs_1.jpg")
            embedV.set_thumbnail(url="https://cdn.discordapp.com/attachments/807369656021024808/807371639033036820/unknown.png")
            embedV.set_author(name="Marrone do Bruno e Marrone", url="https://www.youtube.com/watch?v=29Cfu-6QWEk", icon_url="https://cdn.discordapp.com/attachments/807369656021024808/807371275277434890/unknown.png")
            embedV.set_footer(text="Foto do local porren...anônimo", icon_url="https://cdn.discordapp.com/attachments/549252054347153439/807369261004750858/logo_habibs_1.jpg")
            embedV.add_field(name="😱", value="ELE DA RÉ NO QUIBE???", inline=True)
            embedV.add_field(name= "😱",value="~~sempre deu~~ PARECE QUE SIM", inline=True)
            await message.channel.send(embed=embedV)
        else:
            await message.channel.send("<@206225035332026368>, Não Sabia Que Você Tinha Virado Manobrista Do Habib's.")
    elif message.content.startswith('urbs'):
        embedV = discord.Embed(title="Vitor tristão virou manobrista do habib's?", colour=discord.Colour(0x393f2e), url="https://www.youtube.com/watch?v=29Cfu-6QWEk")
        embedV.set_image(url="https://cdn.discordapp.com/attachments/807369656021024808/807369730435973120/habobs_1.jpg")
        embedV.set_thumbnail(url="https://cdn.discordapp.com/attachments/807369656021024808/807371639033036820/unknown.png")
        embedV.set_author(name="Marrone do Bruno e Marrone", url="https://www.youtube.com/watch?v=29Cfu-6QWEk", icon_url="https://cdn.discordapp.com/attachments/807369656021024808/807371275277434890/unknown.png")
        embedV.set_footer(text="Foto do local por ren...anônimo", icon_url="https://cdn.discordapp.com/attachments/549252054347153439/807369261004750858/logo_habibs_1.jpg")
        embedV.add_field(name="😱", value="ELE DA RÉ NO QUIBE???", inline=True)
        embedV.add_field(name= "😱",value="~~sempre deu~~ PARECE QUE SIM", inline=True)
        await message.channel.send(embed=embedV)

    palavras = message.content
    words = palavras.split()
    if any(word in MensagemProibida for word in words) and message.author.id != 801170526118346752:  
            proibido = []
            contador = 0
            for palavra in words:
                if palavra in MensagemProibida:
                    proibido.append(palavra)
                    contador += 1
            mensagem = proibido[0]
            if contador != 1:
                for palavra in proibido[1:len(proibido)]:
                    if palavra != '':
                        mensagem += ' '+palavra
            await message.delete()
            await message.channel.send(f'<@{message.author.id}> tentou utilizar {mensagem}')
            return        
    else:
        return
token = os.getenv('token')
print(token)
client.run(token)


