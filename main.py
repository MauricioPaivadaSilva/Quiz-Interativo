from tkinter import *

window = Tk()
window.geometry("1080x600")

canvas = Canvas(window, width=1000, height=50)
canvas.configure(bg="white")
canvas.pack(side=TOP, padx=10, pady=10)

resposta = Entry(window, width=70, font= "Times 20 bold")
resposta.pack(padx=10, pady=10)

botao_A =Button(window, text="time A", width=10, height=5)
botao_A.configure(bg="yellow", font="Times 24 bold")
botao_A.pack(side=LEFT, padx=10, pady=10)

botao_B =Button(window, text="time B", width=10, height=5)
botao_B.configure(bg="blue", font="Times 24 bold")
botao_B.pack(side=RIGHT, padx=10, pady=10)

img = PhotoImage(file="src/img/Eq1.png")
canvas.create_image(500, 25, image=img, anchor=CENTER)


window.mainloop()
