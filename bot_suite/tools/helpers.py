def leitura(texto, tempo):
    if isfloat(tempo):
        tempo = float(tempo)
        return [texto, tempo]
    return [0, 0]

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

async def saida(vc):
    try:
        await vc.disconnect()
    except Exception as e:
        print(e)

def create_command_json(command_name : str, duration) -> str:
    """
        Create a 'query' to insert into firebase
        
        Parameters
        ----------
        - command_name -> str
            * name of the command to be recorded
        - duration -> either int or float (doesn't matter)
            * duration of the command in seconds
    """
    return(f"""{{\n\t"{command_name}":\n\t{{\n\t\t"duration": {duration}\n\t}}\n}}""")