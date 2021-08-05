from tkinter import *

interface_calculadora = Tk()

#Funções executadas na calculadora#
def click_igual():
    segundo_numero = visor_calculadora.get()
    visor_calculadora.delete(0, END)
    if operacao == "soma":
        visor_calculadora.insert(0, prim_numero + float(segundo_numero))
    if operacao == "subtracao":
        visor_calculadora.insert(0, prim_numero - float(segundo_numero))
    if operacao == "divisao":
        visor_calculadora.insert(0, prim_numero / float(segundo_numero))
    if operacao == "multiplicacao":
        visor_calculadora.insert(0, prim_numero * float(segundo_numero))

def click_multiplicacao():
    primeiro_numero = visor_calculadora.get()
    global prim_numero
    global operacao
    operacao = "multiplicacao"
    prim_numero = float(primeiro_numero)
    visor_calculadora.delete(0, END)

def click_divisao():
    primeiro_numero = visor_calculadora.get()
    global prim_numero
    global operacao
    operacao = "divisao"
    prim_numero = float(primeiro_numero)
    visor_calculadora.delete(0, END)

def click_subtracao():
    primeiro_numero = visor_calculadora.get()
    global prim_numero
    global operacao
    operacao = "subtracao"
    prim_numero = float(primeiro_numero)
    visor_calculadora.delete(0, END)

def click_soma():
    primeiro_numero = visor_calculadora.get()
    global prim_numero
    global operacao
    operacao = "soma"
    prim_numero = float(primeiro_numero)
    visor_calculadora.delete(0, END)

def click_ponto():
    visor_calculadora.insert(END, ".")

def limpar_visor():
    visor_calculadora.delete(0, END)

def click_botao(number):
    valor_atual = visor_calculadora.get()
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, str(valor_atual) + str(number))

#Tela onde é mostrado os valores inseridos e resultados#
visor_calculadora = Entry(interface_calculadora, relief="sunken", fg="black", font= "Times 15 bold", width=32)
visor_calculadora.grid(row=0, column=0, columnspan=5, ipady=8, ipadx=0)

#Botões usados na calculadora#
botao_9 = Button(interface_calculadora, text="9", height=4, width=10, relief="groove", bg="darkgrey", command=lambda: click_botao(9))
botao_9.grid(row=1, column=0)

botao_8 = Button(interface_calculadora, text="8", height=4, width=10, relief="groove", bg="darkgrey", command=lambda: click_botao(8))
botao_8.grid(row=1, column=1)

botao_7 = Button(interface_calculadora, text="7", height=4, width=10, relief="groove", bg="darkgrey", command=lambda: click_botao(7))
botao_7.grid(row=1, column=2)

botao_6 = Button(interface_calculadora, text="6", height=4, width=10, relief="groove", bg="darkgrey", command=lambda: click_botao(6))
botao_6.grid(row=2, column=0)

botao_5 = Button(interface_calculadora, text="5", height=4, width=10, relief="groove", bg="darkgrey", command=lambda: click_botao(5))
botao_5.grid(row=2, column=1)

botao_4 = Button(interface_calculadora, text="4", height=4, width=10, relief="groove", bg="darkgrey", command=lambda: click_botao(4))
botao_4.grid(row=2, column=2)

botao_3 = Button(interface_calculadora, text="3", height=4, width=10, relief="groove", bg="darkgrey", command=lambda: click_botao(3))
botao_3.grid(row=3, column=0)

botao_2 = Button(interface_calculadora, text="2", height=4, width=10, relief="groove", bg="darkgrey", command=lambda: click_botao(2))
botao_2.grid(row=3, column=1)

botao_1 = Button(interface_calculadora, text="1", height=4, width=10, relief="groove", bg="darkgrey", command=lambda: click_botao(1))
botao_1.grid(row=3, column=2)

botao_0 = Button(interface_calculadora, text="0", height=4, width=10, relief="groove", bg="darkgrey", command=lambda: click_botao(0))
botao_0.grid(row=4, column=1)

botao_limpar = Button(interface_calculadora, text="C", height=4, width=10, bg="red", command=limpar_visor)
botao_limpar.grid(row=4, column=0)

botao_igual = Button(interface_calculadora, text="=", height=4, width=45, bg="RoyalBlue1", command=click_igual)
botao_igual.grid(row=5, column=0, columnspan=4)

botao_soma = Button(interface_calculadora, text="+", height=4, width=10, bg="grey", command=click_soma)
botao_soma.grid(row=1, column=3)

botao_subtracao = Button(interface_calculadora, text="-", height=4, width=10, bg="grey", command=click_subtracao)
botao_subtracao.grid(row=2, column=3)

botao_multiplicacao = Button(interface_calculadora, text="x", height=4, width=10, bg="grey", command=click_multiplicacao)
botao_multiplicacao.grid(row=3, column=3)

botao_divisao = Button(interface_calculadora, text="/", height=4, width=10, bg="grey", command=click_divisao)
botao_divisao.grid(row=4, column=3)

botao_ponto = Button(interface_calculadora, text=".", height=4, width=10, bg="grey", command=click_ponto)
botao_ponto.grid(row=4, column=2)

#Propriedades da janela principal#
interface_calculadora.iconbitmap(r"C:\Users\rbsnc\PycharmProjects\main\Source/pixil-frame-0.ico")
interface_calculadora.title("Ian Calculator's")
interface_calculadora.geometry("320x400")
interface_calculadora.resizable(False, False)
interface_calculadora.mainloop()
