from tkinter import *   
import random

janela = Tk()

def sorteia_casa():
    casas = ["Grifinória", "Sonserina", "Lufa-lufa", "Corvinal"]
    random.shuffle(casas)
    casa_sorteada = casas[0]

    if casa_sorteada == "Grifinória":
        janela.configure(bg="orange")
        texto_padrao = Label(janela, text="Descubra sua casa de Hogwarts", bg="orange", fg="black", font="Georgia")
        texto_padrao.grid(column=0, row=0)
        texto_botao = Label(janela, text="", fg="black", bg="orange", font="Georgia")
        texto_botao.grid(column=0, row=2)
        casa_sorteada_return = f'Parabéns, você foi sorteado para a casa {casas[0]}'
        texto_botao["text"] = casa_sorteada_return

    elif casa_sorteada == "Sonserina":
        janela.configure(bg="green")
        texto_padrao = Label(janela, text="Descubra sua casa de Hogwarts", bg="green", fg="black", font="Georgia")
        texto_padrao.grid(column=0, row=0)
        texto_botao = Label(janela, text="", fg="black", bg="green", font="Georgia")
        texto_botao.grid(column=0, row=2)
        casa_sorteada_return = f'Parabéns, você foi sorteado para a casa {casas[0]}'
        texto_botao["text"] = casa_sorteada_return

    elif casa_sorteada == "Lufa-lufa":
        janela.configure(bg="yellow")
        texto_padrao = Label(janela, text="Descubra sua casa de Hogwarts", bg="yellow", fg="black", font="Georgia")
        texto_padrao.grid(column=0, row=0)
        texto_botao = Label(janela, text="", fg="black", bg="yellow", font="Georgia")
        texto_botao.grid(column=0, row=2)
        casa_sorteada_return = f'Parabéns, você foi sorteado para a casa {casas[0]}'
        texto_botao["text"] = casa_sorteada_return

    else:
        janela.configure(bg="blue")
        texto_padrao = Label(janela, text="Descubra sua casa de Hogwarts", bg="blue", fg="black", font="Georgia")
        texto_padrao.grid(column=0, row=0)
        texto_botao = Label(janela, text="", fg="black", bg="blue", font="Georgia")
        texto_botao.grid(column=0, row=2)
        casa_sorteada_return = f'Parabéns, você foi sorteado para a casa {casas[0]}'
        texto_botao["text"] = casa_sorteada_return

janela.geometry("400x200")

janela.title("Chapéu Seletor")

janela.configure(bg="")

texto_padrao = Label(janela, text="Descubra sua casa de Hogwarts")

texto_padrao.grid(column=0, row=0)

botao = Button(janela, text="Sortear casa", command=sorteia_casa)

botao.grid(column=0, row=1)

texto_botao = Label(janela, text="")

texto_botao.grid(column=0, row=2)

janela.mainloop()
