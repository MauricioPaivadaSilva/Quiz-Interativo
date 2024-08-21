import sqlite3 as db
import hashlib as hs

rt_db = ".\\src\\db"

class dataBase:
    def __init__():
        ...

    def create(dbName, conteudo):
        con = db.connect("{}\\{}.db".format(rt_db, dbName))
        cursor = con.cursor()
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {conteudo} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            caminho TEXT NOT NULL,
            resultado INTEGER NOT NULL
        )
        ''')

        con.commit()

        con.close()

    def add(dbName, conteudo):
        con = db.connect("{}\\{}.db".format(rt_db, dbName))
        cursor = con.cursor()
        cursor.execute(f'''
            INSERT INTO {conteudo} (caminho, resultado)
            VALUES ('Alice', 30), ('Bob', 25), ('Charlie', 35)
        ''')

        con.commit()
        con.close()


    def find(dbName):
        con = db.connect("{}\\{}.db".format(rt_db, dbName))
        cursor = con.cursor()

if __name__ == "__main__":
    dataBase.create("2023", "funcao_afim")
    dataBase.add("2023", "funcao_afim")