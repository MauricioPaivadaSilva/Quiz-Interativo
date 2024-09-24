import tkinter as tk
from tkinter import * # Importando a biblioteca para iniciar a janela
from tkinter import ttk
from tkinter import filedialog as fl # Importando a parte da biblioteca Tk para trabalhar com arquivos.
from PIL import Image, ImageTk # Importando funções que facilitam a manipulação de imagens em janelas
import random # Biblioteca para gerar números pseudo aleatórios
import io # Biblioteca para trabalhar com entrada e saida de dados.
import os # Para listar todos os meus DBs

from router.src.contact import dataBase as db # Importândo o módulo de comunicação com o banco de dados

DBS = []

ANO = ""
CONTEUDO = ""
VALUES = 0 # Variável global para armazenar os dados oriundos do banco de dados
A = 0 # Variável global que armazena a pontuação de A
B = 0 # Variável global que armazena a pontuação de B

def findDBS():
    files = os.listdir(".\\router\\db")
    for file in files:
        DBS.append(str(file[:-3]))

window = Tk() # Chamando a janela de window
window.geometry("1080x600") # Especificando as dimenções da janela
window.title("Quiz de matemática") # Nome da janela
#window.config(bg='grey')

def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb

def cleanWindow():
    for widget in window.winfo_children(): # Limpa os dados anteriores da janela, para poder iniciar a janela nova
        widget.destroy()

def windowGame(): # Cria a janela do jogo

    cleanWindow()

    def restart(canvas): # Zera as pontuações
        global A
        global B
        A = 0
        B = 0
        getDB(canvas)

    blue_rgb = (47, 111, 173)
    hex_blue = rgb_to_hex(blue_rgb)

    menuBar = tk.Menu(window)
    menu = tk.Menu(menuBar, tearoff=0)
    menu.add_command(label="Voltar", command=windowHome)
    menu.add_command(label="Novo Jogo", command=windowGame)
    window.config(menu=menu)

    global VALUES
    global CONTEUDO
    global ANO

    def displayImage(canvas): # Função que apresenta a questão como imagem
        image_data = VALUES[0]
        image = Image.open(io.BytesIO(image_data))
        img = ImageTk.PhotoImage(image)
        canvas.create_image(150, 100, image=img, anchor=CENTER)
        canvas.image = img

    def getDB(canvas): # Função que pede para o banco de dados a nova imagem e a resposta
        global VALUES
        global ANO
        global CONTEUDO
        get = db.find(ANO, CONTEUDO, random.randint(1, 10000))
        VALUES = get
        try:
            resposta.delete(0, 100)
        except:
            pass
        displayImage(canvas)

    def validateA(canvas): # Função para validação da resposta de A
        global A
        global B

        result = str(resposta.get())
        Result = str(VALUES[1])
        if(result != ""):
            if(result == Result):
                A += 1
                scoreA.configure(text=str(A))
                getDB(canvas)
            else:
                B += 1
                scoreB.configure(text=str(B))
                getDB(canvas)

    def validateB(canvas): # Função para validação da resposta de B
        global A
        global B

        result = str(resposta.get())
        Result = str(VALUES[1])
        if(result != ""):
            if(result == Result):
                B += 1
                scoreB.configure(text=str(B))
                getDB(canvas)
            else:
                A += 1
                scoreA.configure(text=str(A))
                getDB(canvas)

    #######################################################
    ### ==> !!! IMPORTANTE FICAR TUDO ONDE ESTÁ !!! <== ###
    #######################################################

    canvas = Canvas(window, width=300, height=200) # Iniciando o ambiente da imagem
    canvas.configure(bg="white") # Especificando a cor de fundo do ambiente da imagem
    canvas.pack(side=TOP, padx=10, pady=10) # Posicionando o ambiente da imagem

    if(A != 0 or B != 0):
        restart(canvas)

    n = random.randint(1, 1000)

    VALUES = [db.find(ANO, CONTEUDO, n)[0], db.find(ANO, CONTEUDO, n)[1]] # Iniciando a variável global com um exercício e uma resposta
    displayImage(canvas) # Iniciando a apresentação da imagem

    resposta = Entry(window, font="Times 20 bold") # Iniciando o campo de resposta
    resposta.pack(fill='x', padx=10, pady=10) # Determinando especificações do campo de resposta

    botao_A =Button(window, text="time A", width=10, height=5) # Iniciando o botão A
    botao_A.configure(bg="yellow", font="Times 24 bold", command=lambda: validateA(canvas)) # Configurando o botão A
    botao_A.pack(side=LEFT, padx=10, pady=10) # Posicionando o botão A

    botao_B =Button(window, text="time B", width=10, height=5) # Iniciando o botão B
    botao_B.configure(bg=hex_blue, font="Times 24 bold", command=lambda: validateB(canvas)) # Configurando o botão B
    botao_B.pack(side=RIGHT, padx=10, pady=10) # Posicionando o botão B

    scoreA = Label(window, text=str(A)) # Apresentando a pontuação de A
    scoreA.configure(bg="yellow", font="Times 24 bold") # Configurando a apresentação da pontuação de A
    scoreA.pack(side=LEFT, padx=10, pady=10) # Posicionando a pontuação de A

    scoreB = Label(window, text=str(B)) # Apresentando a pontuação de B
    scoreB.configure(bg=hex_blue, font="Times 24 bold") # Configurando a apresentação da pontuação de B
    scoreB.pack(side=RIGHT, padx=10, pady=10) # Posicionando a pontuação de B

def windowAdd(): # Janela para adicionar novas questões ao jogo
    cleanWindow()

    menuBar = tk.Menu(window)
    menu = tk.Menu(menuBar, tearoff=0)
    menu.add_command(label="Voltar", command=windowHome)
    window.config(menu=menu)

    FILEPWD = ""

    def fileFind():
        global FILEPWD
        filePwd = fl.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Arquivos de imagem", "*.jpg;*.jpeg;*.png;*.gif")]
        )
        if filePwd:
            FILEPWD = filePwd
            caminho = filePwd.split("/")
            inicio = 0
            final = len(caminho) - 1
            quest.configure(text=str(f"{caminho[inicio]}/.../{caminho[final]}"))

    def send():
        global FILEPWD
        conteudo = table.get().split(" ")
        tabela = ""
        for i in conteudo:
            if(tabela == ""):
                tabela = f"{i}"
            else:
                tabela = f"{tabela}_{i}"
        print(f"\n{tabela}\n")
        pwd = str(FILEPWD)
        rp = str(resp.get())
        ad = (pwd, rp)
        db.add(str(year.get()), tabela, ad)
        resp.delete(0, 100)

    infoYear = Label(window, text="Turma:")
    infoYear.configure(font="Times 18 bold")
    infoYear.grid(row=0, column=0, padx=10, pady=10)

    year = Entry(window, width=20, font="Times 14 bold")
    year.grid(row=0, column=1, padx=10, pady=10)

    infoTable = Label(window, text="Conteúdo:")
    infoTable.configure(font="Times 18 bold")
    infoTable.grid(row=0, column=2, padx=10, pady=10)

    table = Entry(window, width=20, font="Times 14 bold")
    table.grid(row=0, column=3, padx=10, pady=10)

    buttonQuest = Button(window, text="Adicionar questão", font="Times 18 bold", command=fileFind)
    buttonQuest.grid(row=1, column=0, padx=10, pady=10)

    quest = Label(window, text="", font="Times, 18")
    quest.grid(row=1, column=1, padx=10, pady=10)

    infoResp = Label(window, text="Resposta:")
    infoResp.configure(font="Times 18 bold")
    infoResp.grid(row=1, column=2, padx=10, pady=10)

    resp = Entry(window, width=20, font="Times 14 bold")
    resp.grid(row=1, column=3, padx=10, pady=10)

    buttonSend = Button(window, text="Adicionar", font="Times 18 bold", command=send)
    buttonSeld.grid(row=2, column=0, padx=10, pady=10)

def windowSet():
    cleanWindow()
    global DBS
    DBS = []
    findDBS()

    tabelas = []

    def update(event):
        tabelas = []
        dbName = str(year.get())
        conteudos = db.tables(dbName=dbName)
        for conteudo in conteudos:
            conteudo = conteudo[0]
            tabelas.append(conteudo)

        # Atualiza o Combobox
        table['values'] = tabelas


    def start():
        global ANO
        global CONTEUDO
        ANO = year.get().lower()
        CONTEUDO = table.get().lower()
        if(CONTEUDO != "" and ANO != ""):
            windowGame()
        

    menuBar = tk.Menu(window)
    menu = tk.Menu(menuBar, tearoff=0)
    menu.add_command(label="Voltar", command=windowHome)
    window.config(menu=menu)

    infoYear = Label(window, text="Turma:")
    infoYear.configure(font="Times 18 bold")
    infoYear.grid(row=0, column=0, padx=10, pady=10)

    year = ttk.Combobox(window, values=DBS)
    year.grid(row=0, column=1, padx=10, pady=10)
    year.bind("<<ComboboxSelected>>", update)

    infoTable = Label(window, text="Conteúdo:")
    infoTable.configure(font="Times 18 bold")
    infoTable.grid(row=1, column=0, padx=10, pady=10)

    table = ttk.Combobox(window, values=tabelas)
    table.grid(row=1, column=1, padx=10, pady=10)

    buttonSend = Button(window, text="Iniciar jogo", font="Times 18 bold", command=start)
    buttonSend.grid(row=4, column=0, padx=10, pady=10)

def windowHome(): # Cria a janela de início do jogo
    cleanWindow()

    img = Image.open(".\\router\\img\\logo.png")
    img = ImageTk.PhotoImage(img)

    canvas = Canvas(window, width=250, height=250) # Iniciando o ambiente da imagem
    canvas.configure(bg="white") # Especificando a cor de fundo do ambiente da imagem
    canvas.pack(side=TOP, padx=10, pady=10) # Posicionando o ambiente da imagem
    canvas.create_image(125, 125, image=img, anchor=CENTER)
    canvas.image = img

    start = Button(window, text="Jogo", font="Times 18 bold", command=windowSet)
    start.pack(padx=10, pady=10)

    addQuest = Button(window, text="Modo professor", font="Times 18 bold", command=windowAdd)
    addQuest.pack(padx=10, pady=10)

windowHome()

window.mainloop() # Forçando a janela a rodar em loop