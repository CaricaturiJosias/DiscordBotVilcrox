import time, sys, os
from asyncio import wait_for
from asyncio.windows_events import NULL
from discord import FFmpegPCMAudio

dir_path = os.path.dirname(__file__)
sys.path.append("D:/Cthings/prog/Bot-Python/bot_suite/tools")
import helpers as help
import constants as const

async def Play(ctx, comando, duracao, repeticao):
    channel = ctx.author.voice.channel
    if channel == type(None):
        return None
    try: 
        vc = await channel.connect()
    except:

        try:
            vc.disconnect()
        except:
            await ctx.channel.send("Não consegui me conectar")

        await ctx.channel.send("Algo deu errado")

    else:

        try:
            i = 0
            while i < repeticao:
                vc.play(FFmpegPCMAudio(executable="C:/Program Files/ffmpeg/bin/ffmpeg.exe", source=f'D:/Cthings/prog/Bot-Python/audio/{comando}.mp3'))
                time.sleep(duracao)
                i += 1
            await help.saida(vc)

        except:
            await help.saida(vc)

    