def leitura(texto, tempo):
    print("Comado: "+texto+"\nDuracao: "+tempo)
    if isfloat(tempo):
        tempo = float(tempo)
        return [texto, tempo]

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

class comandoVoice:
    def __init__(self, user, qntt, comand):
        self.user   = user
        self.qntt   = qntt
        self.comand = comand

def checagem(queue, id, user, comand): 
  try:
    comando = comandoVoice(id, user, comand)
    queue.append(comando)
    return 1
  except: 
    print("Falha ao tentar criar comando")
    return 0

async def waiting(queue):
    value = len(queue)-1
    
    while (value != len(queue)):
        pass
    return 1
  
async def register(comando, id_user, id_vc, id_canal_texto, id_guild, repeticao):
    # await DB.Comando_register(comando, id_user, id_vc, id_canal_texto, id_guild, repeticao)
    return None

async def waiting(queue):
    value = len(queue)-1
    
    while (value != len(queue)):
        pass
    return 1

async def register(comando, id_user, id_vc, id_canal_texto, id_guild, repeticao):
    # await DB.Comando_register(comando, id_user, id_vc, id_canal_texto, id_guild, repeticao)
    return None

async def saida(ctx):
    await ctx.disconnect()
    ctx.cleanup()