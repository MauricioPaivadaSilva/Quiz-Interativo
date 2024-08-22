import sqlite3 as db
from random import randint as rd

rt_db = ".\\src\\db"

class dataBase:
    def __init__():
        ...

    def convertForDB(filename):
        with open(filename, 'rb') as file:
            data = file.read()
        return data

    @staticmethod
    def create(dbName, conteudo):
        con = db.connect("{}\\{}.db".format(rt_db, dbName))
        cursor = con.cursor()
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {conteudo} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image BLOB NOT NULL,
            resultado TEXT NOT NULL
        )
        ''')

        con.commit()

        con.close()

    @staticmethod
    def add(dbName, conteudo, questao):
        con = db.connect(f"{rt_db}\\{dbName}.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{conteudo}';")
        table_exist = cursor.fetchone()
        if not table_exist:
            dataBase.create(dbName, conteudo)

        binary = dataBase.convertForDB(questao[0])

        cursor.execute(f"""
            INSERT INTO {conteudo} (image, resultado) VALUES (?, ?)
        """, (binary, questao[1]))

        con.commit()
        con.close()

    @staticmethod
    def find(dbName, conteudo, idS):
        con = db.connect("{}\\{}.db".format(rt_db, dbName))
        cursor = con.cursor()

        cursor.execute(f"SELECT COUNT(*) FROM {conteudo}")
        tableSize = cursor.fetchone()[0]

        if idS > tableSize:
            num = rd(1, tableSize)
        else:
            num = idS
        
        cursor.execute(f"SELECT image, resultado FROM {conteudo} WHERE id = ?", (num,))
        line = cursor.fetchone()
        if line:
            print(f"\n\tResultado: {line[1]}")

if __name__ == "__main__":
    dados = [(".\\src\\img\\Eq1.png", "-1")]

    for i in dados:
        dataBase.add("2023", "trigonometria", i)

    dataBase.find("2023", "trigonometria", 1)