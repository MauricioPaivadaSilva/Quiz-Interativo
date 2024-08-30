from tkinter import * # Importando a biblioteca para iniciar a janela
from PIL import Image, ImageTk # Importando funções que facilitam a manipulação de imagens em janelas
import random # Biblioteca para gerar números pseudo aleatórios
import io # Biblioteca para trabalhar com entrada e saida de dados.

from router.src.contact import dataBase as db # Importândo o módulo de comunicação com o banco de dados

VALUES = 0 # Variável global para armazenar os dados oriundos do banco de dados
A = 0 # Variável global que armazena a pontuação de A
B = 0 # Variável global que armazena a pontuação de B

window = Tk() # Chamando a janela de window
window.geometry("1080x600") # Especificando as dimenções da janela
window.title("Quiz de matemática") # Nome da janela

def cleanWindow():
    for widget in window.winfo_children(): # Limpa os dados anteriores da janela, para poder iniciar a janela nova
        widget.destroy()

def windowGame(): # Cria a janela do jogo

    cleanWindow()

    global VALUES

    def home(): # Retorna a tela inicial
        ...
    
    def restart(): # Zera as pontuações
        ...

    def displayImage(canvas): # Função que apresenta a questão como imagem
        image_data = VALUES[0]
        image = Image.open(io.BytesIO(image_data))
        img = ImageTk.PhotoImage(image)
        canvas.create_image(500, 25, image=img, anchor=CENTER)
        canvas.image = img

    def getDB(canvas): # Função que pede para o banco de dados a nova imagem e a resposta
        global VALUES
        get = db.find('2023', "funcoes", random.randint(1, 10000))
        VALUES = get
        resposta.delete(0, 100)
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

    canvas = Canvas(window, width=1000, height=50) # Iniciando o ambiente da imagem
    canvas.configure(bg="white") # Especificando a cor de fundo do ambiente da imagem
    canvas.pack(side=TOP, padx=10, pady=10) # Posicionando o ambiente da imagem

    VALUES = [db.find("2023", "funcoes", 2)[0], db.find("2023", "funcoes", 2)[1]] # Iniciando a variável global com um exercício e uma resposta
    displayImage(canvas) # Iniciando a apresentação da imagem

    resposta = Entry(window, width=70, font= "Times 20 bold") # Iniciando o campo de resposta
    resposta.pack(padx=10, pady=10) # Determinando especificações do campo de resposta

    botao_A =Button(window, text="time A", width=10, height=5) # Iniciando o botão A
    botao_A.configure(bg="yellow", font="Times 24 bold", command=lambda: validateA(canvas)) # Configurando o botão A
    botao_A.pack(side=LEFT, padx=10, pady=10) # Posicionando o botão A

    botao_B =Button(window, text="time B", width=10, height=5) # Iniciando o botão B
    botao_B.configure(bg="blue", font="Times 24 bold", command=lambda: validateB(canvas)) # Configurando o botão B
    botao_B.pack(side=RIGHT, padx=10, pady=10) # Posicionando o botão B

    scoreA = Label(window, text=str(A)) # Apresentando a pontuação de A
    scoreA.configure(bg="yellow", font="Times 24 bold") # Configurando a apresentação da pontuação de A
    scoreA.pack(side=LEFT, padx=10, pady=10) # Posicionando a pontuação de A

    scoreB = Label(window, text=str(B)) # Apresentando a pontuação de B
    scoreB.configure(bg="blue", font="Times 24 bold") # Configurando a apresentação da pontuação de B
    scoreB.pack(side=RIGHT, padx=10, pady=10) # Posicionando a pontuação de B

def windowAdd(): # Janela para adicionar novas questões ao jogo
    ...

def windowHome(): # Cria a janela de início do jogo
    cleanWindow()

    img = Image.open(".\\router\\img\\logo.png")
    img = ImageTk.PhotoImage(img)

    canvas = Canvas(window, width=250, height=250) # Iniciando o ambiente da imagem
    canvas.configure(bg="white") # Especificando a cor de fundo do ambiente da imagem
    canvas.pack(side=TOP, padx=10, pady=10) # Posicionando o ambiente da imagem
    canvas.create_image(125, 125, image=img, anchor=CENTER)
    canvas.image = img

    start = Button(window, text="Start", command=windowGame)
    start.pack(padx=10, pady=10)

windowHome()

window.mainloop() # Forçando a janela a rodar em loop