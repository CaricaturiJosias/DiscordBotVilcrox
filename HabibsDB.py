#This is a py code trying to integrate Habib's manager with MySQL server
import os, mysql.connector as mysql
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

    def user_check(self, id_user, nome):
        cursor = self.db.cursor(buffered=True)
        cursor.execute(f'SELECT EXISTS(SELECT * from Bot_Usuario WHERE ID_Usuario= "{id_user}")')

        if (cursor.fetchall()[0][0] == 1):                                                  # Se já estiver cadastrado o ID
            cursor.execute(f'SELECT EXISTS(SELECT * from Aliases WHERE ID_Usuario= "{id_user}" AND Alias = "{nome}")')

            if (cursor.fetchall()[0][0] == 0):                                              # SE não estiver cadastrado o Alias
                cursor.execute(f'INSERT INTO Aliases VALUES ("{id_user}", "{nome}")')

        else:
            cursor.execute(f'INSERT INTO Bot_Usuario VALUES ("{id_user}")')         #Registra o ID
            cursor.execute(f'INSERT INTO Aliases VALUES ("{id_user}","{nome}")')    #Registra o Alias
        cursor.close()
        self.db.commit()

    def Comando(self, comando):
        cursor = self.db.cursor(buffered=True)
        cursor.execute(f'SELECT EXISTS(SELECT * from Bot_Comando WHERE nome= "{comando}")')
        i = deepcopy(cursor.fetchall()[0][0])
        print(i)
        if (i == 1):
            cursor.execute(f'SELECT tempo FROM Bot_Comando WHERE nome = "{comando}"')
            a = deepcopy(cursor.fetchall()[0][0])
            self.close(cursor)
            return a # retorna a duracao do comando
        else:
            print("Não foi encontrado o comando")
            self.close(cursor)
            return 0
        

    def Comando_insert(self, comando, duracao):
        cursor = self.db.cursor()
        cursor.execute(f'SELECT NOT EXISTS(SELECT * FROM Bot_Comando WHERE nome = "{comando}")')
        if (cursor.fetchall()[0][0] == 1):
            cursor.execute(f'INSERT INTO Bot_Comando VALUES ("{comando}", {str(duracao)})')
            cursor.execute(f'SELECT EXISTS(SELECT * FROM Bot_Comando WHERE nome = "{comando}")')
            cursor.commit()
            a = deepcopy(cursor.fetchall()[0][0])
            self.close(cursor)
            return a #1 se funcionou
        else:
            cursor.execute(f'SELECT EXISTS(SELECT * FROM Bot_Comando WHERE nome = "{comando}" AND tempo = {duracao})')
            a = deepcopy(cursor.fetchall()[0][0])
            self.close(cursor)
            return a #1 se já existe
            

