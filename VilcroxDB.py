#This is a py code trying to integrate Habib's manager with MySQL server
import os, mysql.connector as mysql
from datetime import datetime
from copy import deepcopy
from dotenv import load_dotenv
class Database:

    def __init__(self):
        load_dotenv()
        Host = os.getenv('host')
        User = os.getenv('user')
        Password = os.getenv('passwd')
        db = os.getenv('database')
        self.db = mysql.connect(
            host = Host,
            user = User,
            passwd = Password,
            database = db
        )

    def close(self, cursor):
        cursor.close()
        self.db.commit()   

    def guild_check(self, id_guild, nome):
        cursor = self.db.cursor(buffered=True)
        cursor.execute(f'SELECT EXISTS(SELECT * from Guilds WHERE ID_Guild= "{id_guild}")')

        if (cursor.fetchall()[0][0] == 1):                                                  # Se já estiver cadastrado o ID
            cursor.execute(f'SELECT EXISTS(SELECT * from Aliases_Guilds WHERE ID_Guild= "{id_guild}" AND Alias_Guild = "{nome}")')

            if (cursor.fetchall()[0][0] == 0):                                              # SE não estiver cadastrado o Alias
                            cursor.execute(f'INSERT INTO Aliases_Guilds VALUES ("{id_guild}", "{nome}")')

        else:
            cursor.execute(f'INSERT INTO Guilds VALUES ("{id_guild}")')                     #Registra o ID
            cursor.execute(f'INSERT INTO Aliases_Guilds VALUES ("{id_guild}","{nome}")')    #Registra o Alias
        cursor.close()
        self.db.commit()

    def user_check(self, id_user, id_guild, nome):
        cursor = self.db.cursor(buffered=True)
        cursor.execute(f'SELECT EXISTS(SELECT * from Usuarios WHERE ID_Usuario= "{id_user}")')

        if (cursor.fetchall()[0][0] == 1):                                                  # Se já estiver cadastrado o ID
            cursor.execute(f'SELECT EXISTS(SELECT * from Aliases_Usuario WHERE ID_Usuario= "{id_user}" AND Alias_Usuario = "{nome}" and ID_Guild = "{id_guild}")')

            if (cursor.fetchall()[0][0] == 0):                                              # SE não estiver cadastrado o Alias
                cursor.execute(f'INSERT INTO Aliases_Usuario VALUES ("{id_user}", "{id_guild}", "{nome}")')
        else:
            cursor.execute(f'INSERT INTO Usuarios VALUES ("{id_user}")')         #Registra o ID
            cursor.execute(f'INSERT INTO Aliases_Usuario VALUES ("{id_user}", "{id_guild}", "{nome}")')    #Registra o Alias
        cursor.close()
        self.db.commit()

    def Comando(self, comando):
        cursor = self.db.cursor(buffered=True)
        cursor.execute(f'SELECT EXISTS(SELECT * from ComandosVoz WHERE Comando= "{comando}")')
        i = deepcopy(cursor.fetchall()[0][0])
        if (i == 1):
            cursor.execute(f'SELECT Duracao FROM ComandosVoz WHERE Comando = "{comando}"')
            a = deepcopy(cursor.fetchall()[0][0])
            self.close(cursor)
            return a # retorna a duracao do comando
        else:
            print("Não foi encontrado o comando")
            self.close(cursor)
            return 0
        

    def Comando_insert(self, bus):
        cursor = self.db.cursor()
        print (f'INSERT INTO ComandosVoz VALUES ("{bus[0]}", {str(bus[1])})')
        cursor.execute(f'SELECT NOT EXISTS(SELECT * FROM ComandosVoz WHERE Comando = "{bus[0]}")')
        if (cursor.fetchall()[0][0] == 1):
            cursor.execute(f'INSERT INTO ComandosVoz VALUES ("{bus[0]}", {str(bus[1])})')
            cursor.execute(f'SELECT EXISTS(SELECT * FROM ComandosVoz WHERE Comando = "{bus[0]}")')
            a = deepcopy(cursor.fetchall()[0][0])
            self.close(cursor)
            return a #1 se funcionou
        else:
            cursor.execute(f'SELECT EXISTS(SELECT * FROM ComandosVoz WHERE Comando = "{bus[0]}" AND Duracao = {bus[1]})')
            a = deepcopy(cursor.fetchall()[0][0])
            self.close(cursor)
            return a #1 se já existe

    def comando_list(self):
        cursor = self.db.cursor()
        try:
            cursor.execute('SELECT Comando, Duracao FROM ComandosVoz ORDER BY Comando')
            a = deepcopy(cursor.fetchall())
            return a
        except:
            print("ono")

    async def Comando_register(self, comando, id_user, id_vc, id_canal_texto, id_guild, repeticao):
        cursor = self.db.cursor()
        try:
            cursor.execute(f'SELECT EXISTS(SELECT * FROM ComandosVoz WHERE nome = "{comando}")')
            if cursor.fetchall()[0][0] == 1:
                cursor.execute(f'INSERT INTO UsoComandosVoz VALUES ("{id_user}", "{id_guild}", "{id_vc}", "{id_canal_texto}", "{datetime.date(datetime.now())}", "{comando}", "{str(repeticao)}")')
            self.close(cursor)
        except:
            print("Erro no comando_register")

        

