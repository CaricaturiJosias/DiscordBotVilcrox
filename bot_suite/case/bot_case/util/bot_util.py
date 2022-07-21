import time, sys
from asyncio import wait_for
from asyncio.windows_events import NULL
from discord import FFmpegPCMAudio

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
        ctx.channel.send("Não consegui me conectar")
    else:
        try:
            i = 0
            while i < repeticao:
                vc.play(FFmpegPCMAudio(executable="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe", source=f'D:\\Audio_Bot\\{comando}.mp3'))
                time.sleep(duracao)
                i += 1
            await help.register(comando, ctx.author.id, ctx.author.voice.channel, ctx.channel, ctx.guild.id, repeticao)
            await saida(vc)
        except:
            await saida(vc)

    