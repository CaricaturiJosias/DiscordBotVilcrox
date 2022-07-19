from dotenv import load_dotenv
import os

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

def get_env(bot):
  load_dotenv()
  token = os.getenv('token')
  bot.run(token)
