import sys

sys.path.append("D:/Cthings/prog/Bot-Python/bot_suite/tools")
import helpers as help
import constants as const

"""
    Made for storing constants
"""

allowed_users = [ 206225035332026368
                , 338052801286635520
                , 183653926598475776
                , 266301388059967489
                , 266301388059967489]

MensagemProibida = [ "lepo"
                    ,"lepo lepo"
                    , "kid abelha"
                    , "coringatron"]
YOUTUBE_REGEX       : str = "^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
SECONDS_0_5         : int = 3
SECONDS_60          : int = 60