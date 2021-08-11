#This is a py code trying to integrate Habib's manager with a postgreSQL server
import psycopg2
def inicio(con):
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Habibs_Reg( usuario VARCHAR(50) NOT NULL, idDiscord VARCHAR(20) NOT NULL UNIQUE, NUM_COMANDOS INT DEFAULT 0);")
    con.commit()
    print("Records inserted successfully")

def conexao(con, usuario, id):
    cur = con.cursor()
    try:
        cur.execute(f"INSERT INTO habibs_reg VALUES('{usuario}','{id}');")
        con.commit()
    except:
        print("Erro tentando registrar o usuario de esfiha "+usuario+ " de id "+str(id))
    try:
        cur.execute(f"UPDATE habibs_reg SET num_comandos = num_comandos+1 WHERE iddiscord = '{id}';")
    except:
        print("Erro ao incrementar")