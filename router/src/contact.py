import sqlite3 as db # Importando a biblioteca que trabalha com banco de dados
from random import randint as rd # Importanto biblioteca para geração de números pseudo aleatórios

rt_db = ".\\router\\db" # Especificando o caminho total até o banco de dados a partir do programa lider

class dataBase:
    def __init__():
        ...

    def convertForDB(filename): # Função que converte a imagem para ser inserida no banco de dados
        with open(filename, 'rb') as file:
            data = file.read()
        return data

    @staticmethod
    def create(dbName, conteudo): # Função que cria o banco de dados, com os parâmetros (id; image; resultado)
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
    def add(dbName, conteudo, questao): # Função para adicionar novas questões
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

        return "Inserido"

    @staticmethod
    def find(dbName, conteudo, idS): # Função para procurar as questões no banco de dados com base no id
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

        con.close()
        return line

    @staticmethod
    def tables(dbName):
        con = db.connect("{}\\{}.db".format(rt_db, dbName))
        cursor = con.cursor()

        cursor.execute("SELECT name FROM sqlite_sequence")
        tabelas = cursor.fetchall()

        return tabelas

if __name__ == "__main__":

    i = 1

    dados = []

    while i < 8:
        dados.append((f".\\src\\img\\Eq{i}.png", "-1"))
        i += 1
    
    #dados = [(".\\src\\img\\Eq1.png", "-1")]

    for i in dados:
        dataBase.add("2023", "funcoes", i)

    dataBase.find("2023", "funcoes", 1)