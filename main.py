from tkinter import *
from PIL import Image, ImageTk
import random
import io

from src.init import dataBase as db

VALUES = 0
A = 0
B = 0

def displayImage(canvas):
    image_data = VALUES[0]
    image = Image.open(io.BytesIO(image_data))
    img = ImageTk.PhotoImage(image)
    canvas.create_image(500, 25, image=img, anchor=CENTER)
    canvas.image = img

def getDB(canvas):
    get = db.find('2023', "trigonometria", int(random.random()))
    VALUES = get
    displayImage(canvas)

def validateA(canvas):
    global A
    global B

    result = str(resposta.get())
    Result = str(VALUES[1])
    if(result == Result):
        A += 1
        scoreA.configure(text=str(A))
        getDB(canvas)
    else:
        B += 1
        scoreB.configure(text=str(B))
        getDB(canvas)

def validateB(canvas):
    global A
    global B

    result = str(resposta.get())
    Result = str(VALUES[1])
    if(result == Result):
        B += 1
        scoreB.configure(text=str(B))
        getDB(canvas)
    else:
        A += 1
        scoreA.configure(text=str(A))
        getDB(canvas)

window = Tk()
window.geometry("1080x600")

canvas = Canvas(window, width=1000, height=50)
canvas.configure(bg="white")
canvas.pack(side=TOP, padx=10, pady=10)

VALUES = [db.find("2023", "trigonometria", 1)[0], db.find("2023", "trigonometria", 1)[1]]
displayImage(canvas)

resposta = Entry(window, width=70, font= "Times 20 bold")
resposta.pack(padx=10, pady=10)

botao_A =Button(window, text="time A", width=10, height=5)
botao_A.configure(bg="yellow", font="Times 24 bold", command=lambda: validateA(canvas))
botao_A.pack(side=LEFT, padx=10, pady=10)

botao_B =Button(window, text="time B", width=10, height=5)
botao_B.configure(bg="blue", font="Times 24 bold", command=lambda: validateB(canvas))
botao_B.pack(side=RIGHT, padx=10, pady=10)

scoreA = Label(window, text=str(A))
scoreA.configure(bg="yellow", font="Times 24 bold")
scoreA.pack(side=LEFT, padx=10, pady=10)

scoreB = Label(window, text=str(B))
scoreB.configure(bg="blue", font="Times 24 bold")
scoreB.pack(side=RIGHT, padx=10, pady=10)


window.mainloop()
