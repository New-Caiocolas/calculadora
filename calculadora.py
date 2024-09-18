from tkinter import *

numero1 = ''
dividir = False
multiplica = False
diminui = False
somar = False


def click(num):
    e.insert(END, num)

def divisao():
    global numero1
    global dividir
    dividir = True
    numero1 = e.get()
    e.delete(0, END)


def multiplicar():
    global numero1
    global multiplica
    multiplica = True
    numero1 = e.get()
    e.delete(0, END)

def subtracao():
    global numero1
    global diminui
    diminui = True
    numero1 = e.get()
    e.delete(0, END)

def soma():
    global numero1
    global somar
    somar = True
    numero1 = e.get()
    e.delete(0, END)

def igual():
    global dividir
    global multiplica
    global diminui
    global somar
    numero2 = e.get()

    if dividir == True:
        e.delete(0, END)
        e.insert(0,(int(numero1))/(int(numero2)))
        dividir = False
    if multiplica == True:
        e.delete(0, END)
        e.insert(0,int(numero1)*int(numero2))
        multiplica = False
    if diminui == True:
        e.delete(0, END)
        e.insert(0,int(numero1)-int(numero2))
        diminui = False
    if somar == True:
        e.delete(0, END)
        e.insert(0,int(numero1)+int(numero2))
        somar = False
    


def deletar():
    e.delete(0, END)

# configurando janela
root = Tk()
root.title('Calculadora')
root.geometry('408x355')
root.maxsize(width='408', height='355')
root.minsize(width='408', height='355')
root.configure(bg='#D8D8D8')

# Screen
e = Entry(root, width=15 ,borderwidth=4 ,relief=FLAT ,fg='#003DC0' ,font=('futura',25,'bold') ,bg='#fff', justify='center')
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)

# Operações
divisao_button = Button(root,
                        text='÷',
                        font=('futura',12,'bold'),
                        padx=41,
                        pady=20,
                        bg='#003DC0',
                        fg='#fff',
                        relief=FLAT,
                        justify='center',
                        activebackground='#0033A3',
                        activeforeground='#fff',
                        command=divisao)

divisao_button.grid(row=0, column=4)

multiplicar_button = Button(root,
                        text='X',
                        font=('futura',12,'bold'),
                        padx=42,
                        pady=20,
                        bg='#003DC0',
                        fg='#fff',
                        relief=FLAT,
                        justify='center',
                        activebackground='#0033A3',
                        activeforeground='#fff',
                        command=multiplicar)

multiplicar_button.grid(row=1, column=4)

subtracao_button = Button(root,
                        text='-',
                        font=('futura',12,'bold'),
                        padx=45,
                        pady=20,
                        bg='#003DC0',
                        fg='#fff',
                        relief=FLAT,
                        justify='center',
                        activebackground='#0033A3',
                        activeforeground='#fff',
                        command=subtracao)

subtracao_button.grid(row=2, column=4)

soma_button = Button(root,
                        text='+',
                        font=('futura',12,'bold'),
                        padx=43,
                        pady=20,
                        bg='#003DC0',
                        fg='#fff',
                        relief=FLAT,
                        justify='center',
                        activebackground='#0033A3',
                        activeforeground='#fff',
                        command=soma)

soma_button.grid(row=3, column=4)

igual_button = Button(root,
                        text='=',
                        font=('futura',12,'bold'),
                        padx=43,
                        pady=20,
                        bg='#003DC0',
                        fg='#fff',
                        relief=FLAT,
                        justify='center',
                        activebackground='#0033A3',
                        activeforeground='#fff',
                        command=igual)

igual_button.grid(row=4, column=4)

# Primeira fileira

um_button = Button(root,
                        text='1',
                        font=('futura',12,'bold'),
                        padx=40,
                        pady=20,
                        bg='#003DC0',
                        fg='#fff',
                        relief=FLAT,
                        justify='center',
                        activebackground='#0033A3',
                        activeforeground='#fff',
                        command=lambda: click(1))

um_button.grid(row=1, column=1)

dois_button = Button(root,
                        text='2',
                        font=('futura',12,'bold'),
                        padx=40,
                        pady=20,
                        bg='#003DC0',
                        fg='#fff',
                        relief=FLAT,
                        justify='center',
                        activebackground='#0033A3',
                        activeforeground='#fff',
                        command=lambda: click(2))

dois_button.grid(row=1, column=2)

tres_button = Button(root,
                        text='3',
                        font=('futura',12,'bold'),
                        padx=42,
                        pady=20,
                        bg='#003DC0',
                        fg='#fff',
                        relief=FLAT,
                        justify='center',
                        activebackground='#0033A3',
                        activeforeground='#fff',
                        command=lambda: click(3))

tres_button.grid(row=1, column=3)

# segunda fileira

quatro_button = Button(root,
                        text='4',
                        font=('futura',12,'bold'),
                        padx=40,
                        pady=20,
                        bg='#003DC0',
                        fg='#fff',
                        relief=FLAT,
                        justify='center',
                        activebackground='#0033A3',
                        activeforeground='#fff',
                        command=lambda: click(4))

quatro_button.grid(row=2, column=1)

cinco_button = Button(root,
                        text='5',
                        font=('futura',12,'bold'),
                        padx=40,
                        pady=20,
                        bg='#003DC0',
                        fg='#fff',
                        relief=FLAT,
                        justify='center',
                        activebackground='#0033A3',
                        activeforeground='#fff',
                        command=lambda: click(5))

cinco_button.grid(row=2, column=2)

seis_button = Button(root,
                        text='6',
                        font=('futura',12,'bold'),
                        padx=42,
                        pady=20,
                        bg='#003DC0',
                        fg='#fff',
                        relief=FLAT,
                        justify='center',
                        activebackground='#0033A3',
                        activeforeground='#fff',
                        command=lambda: click(6))

seis_button.grid(row=2, column=3)

# terceira fileira

sete_button = Button(root,
                        text='7',
                        font=('futura',12,'bold'),
                        padx=40,
                        pady=20,
                        bg='#003DC0',
                        fg='#fff',
                        relief=FLAT,
                        justify='center',
                        activebackground='#0033A3',
                        activeforeground='#fff',
                        command=lambda: click(7))

sete_button.grid(row=3, column=1)

oito_button = Button(root,
                        text='8',
                        font=('futura',12,'bold'),
                        padx=40,
                        pady=20,
                        bg='#003DC0',
                        fg='#fff',
                        relief=FLAT,
                        justify='center',
                        activebackground='#0033A3',
                        activeforeground='#fff',
                        command=lambda: click(8))

oito_button.grid(row=3, column=2)

nove_button = Button(root,
                        text='9',
                        font=('futura',12,'bold'),
                        padx=42,
                        pady=20,
                        bg='#003DC0',
                        fg='#fff',
                        relief=FLAT,
                        justify='center',
                        activebackground='#0033A3',
                        activeforeground='#fff',
                        command=lambda: click(9))

nove_button.grid(row=3, column=3)

# quarta fileira

zero_button = Button(root,
                        text='0',
                        font=('futura',12,'bold'),
                        padx=91,
                        pady=20,
                        bg='#003DC0',
                        fg='#fff',
                        relief=FLAT,
                        justify='center',
                        activebackground='#0033A3',
                        activeforeground='#fff',
                        command=lambda: click(0))

zero_button.grid(row=4, column=1, columnspan=2)

del_button = Button(root,
                        text='C',
                        font=('futura',12,'bold'),
                        padx=41,
                        pady=20,
                        bg='#003DC0',
                        fg='#fff',
                        relief=FLAT,
                        justify='center',
                        activebackground='#0033A3',
                        activeforeground='#fff',
                        command=deletar)

del_button.grid(row=4, column=3)




root.mainloop()