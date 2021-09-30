def leitura(texto, tempo):
    if isfloat(tempo):
        tempo = float(tempo)
        return [texto, tempo]

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False
