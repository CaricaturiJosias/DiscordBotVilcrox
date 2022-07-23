import time, sys, os
from asyncio import wait_for
from asyncio.windows_events import NULL
from discord import FFmpegPCMAudio

dir_path = os.path.dirname(__file__)
sys.path.append("D:/Cthings/prog/Bot-Python/bot_suite/tools")
import helpers as help
import constants as const

async def Play(ctx, comando, duracao, repetition):
    channel = ctx.author.voice.channel
    if channel == type(None):
        return None
    try: 
        vc = await channel.connect()
    except:

        try:
            vc.disconnect()
        except:
            print("Não consegui me conectar")

        print("Algo deu errado")

    else:

        try:
            print(repetition)
            for i in range(repetition):
                try:
                    vc.play(FFmpegPCMAudio(executable="C:/Program Files/ffmpeg/bin/ffmpeg.exe", source=f'D:/Cthings/prog/Bot-Python/audio/{comando}.mp3'))
                    time.sleep(const.SECONDS_0_5)
                except Exception as e:
                    print(e)
            await help.saida(vc)

        except:
            await help.saida(vc)

    