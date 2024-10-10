import customtkinter as ctk

ctk.set_appearance_mode("dark")

numero1 = ''
dividir = False
multiplica = False
diminui = False
somar = False


def click(num):
    tamanho_texto = len(e.get())
    e.insert(tamanho_texto,num)

def divisao():
    global numero1
    global dividir
    dividir = True
    numero1 = e.get()
    tamanho_texto = len(e.get())
    e.delete(0, tamanho_texto)


def multiplicar():
    global numero1
    global multiplica
    multiplica = True
    numero1 = e.get()
    tamanho_texto = len(e.get())
    e.delete(0, tamanho_texto)

def subtracao():
    global numero1
    global diminui
    diminui = True
    numero1 = e.get()
    tamanho_texto = len(e.get())
    e.delete(0, tamanho_texto)

def soma():
    global numero1
    global somar
    somar = True
    numero1 = e.get()
    tamanho_texto = len(e.get())
    e.delete(0, tamanho_texto)

def igual():
    global dividir
    global multiplica
    global diminui
    global somar
    numero2 = e.get()

    if dividir == True:
        tamanho_texto = len(e.get())
        e.delete(0, tamanho_texto)
        e.insert(0,(int(numero1))/(int(numero2)))
        dividir = False
    if multiplica == True:
        tamanho_texto = len(e.get())
        e.delete(0, tamanho_texto)
        e.insert(0,int(numero1)*int(numero2))
        multiplica = False
    if diminui == True:
        tamanho_texto = len(e.get())
        e.delete(0, tamanho_texto)
        e.insert(0,int(numero1)-int(numero2))
        diminui = False
    if somar == True:
        tamanho_texto = len(e.get())
        e.delete(0, tamanho_texto)
        e.insert(0,int(numero1)+int(numero2))
        somar = False
    


def deletar():
    tamanho_texto = len(e.get())
    e.delete(0, tamanho_texto)

# configurando janela
root = ctk.CTk()
root.title('Calculadora')
root.geometry('408x355')
root.resizable(False,False)
root.configure(bg='#D8D8D8')

# Screen
e = ctk.CTkEntry(root, width=306,height=71 ,border_width=4 ,fg_color='#fff' ,font=('futura',25,'bold') ,bg_color='#003DC0', justify='center', text_color='#003DC0')
e.place(x=0, y=0)
# Operações
divisao_button = ctk.CTkButton(root,
                        text='÷',
                        font=('futura',16,'bold'),
                        text_color='#003DC0',
                        width=102,
                        height=71,
                        corner_radius=0,
                        bg_color='blue',
                        fg_color='#fff',
                        command=divisao)

divisao_button.place(x=306.5,y=0)

multiplicar_button = ctk.CTkButton(root,
                        text='X',
                        font=('futura',16,'bold'),
                        text_color='#003DC0',
                        width=102,
                        height=71,
                        corner_radius=0,
                        bg_color='blue',
                        fg_color='#fff',
                        command=multiplicar)

multiplicar_button.place(x=306.5,y=71)

subtracao_button = ctk.CTkButton(root,
                        text='-',
                        font=('futura',16,'bold'),
                        text_color='#003DC0',
                        width=102,
                        height=71,
                        corner_radius=0,
                        bg_color='blue',
                        fg_color='#fff',
                        command=subtracao)

subtracao_button.place(x=306.5,y=142)

soma_button = ctk.CTkButton(root,
                        text='+',
                        font=('futura',16,'bold'),
                        text_color='#003DC0',
                        width=102,
                        height=71,
                        corner_radius=0,
                        bg_color='blue',
                        fg_color='#fff',
                        command=soma)

soma_button.place(x=306.5,y=213)

igual_button = ctk.CTkButton(root,
                        text='=',
                        font=('futura',16,'bold'),
                        text_color='#003DC0',
                        width=102,
                        height=71,
                        corner_radius=0,
                        bg_color='blue',
                        fg_color='#fff',
                        command=igual)

igual_button.place(x=306.5,y=284)


# Primeira fileira

um_button = ctk.CTkButton(root,
                        text='1',
                        font=('futura',12,'bold'),
                        text_color='#003DC0',
                        width=102,
                        height=71,
                        corner_radius=0,
                        bg_color='blue',
                        fg_color='#fff',
                        command=lambda: click(1))
um_button.place(x=0,y=71)


dois_button = ctk.CTkButton(root,
                        text='2',
                        font=('futura',12,'bold'),
                        text_color='#003DC0',
                        width=102,
                        height=71,
                        corner_radius=0,
                        bg_color='blue',
                        fg_color='#fff',
                        command=lambda: click(2))
dois_button.place(x=102,y=71)

tres_button = ctk.CTkButton(root,
                        text='3',
                        font=('futura',12,'bold'),
                        text_color='#003DC0',
                        width=102,
                        height=71,
                        corner_radius=0,
                        bg_color='blue',
                        fg_color='#fff',
                        command=lambda: click(3))
tres_button.place(x=204,y=71)

# segunda fileira

quatro_button = ctk.CTkButton(root,
                        text='4',
                        font=('futura',12,'bold'),
                        text_color='#003DC0',
                        width=102,
                        height=71,
                        corner_radius=0,
                        bg_color='blue',
                        fg_color='#fff',
                        command=lambda: click(4))
quatro_button.place(x=0,y=142)

cinco_button = ctk.CTkButton(root,
                        text='5',
                        font=('futura',12,'bold'),
                        text_color='#003DC0',
                        width=102,
                        height=71,
                        corner_radius=0,
                        bg_color='blue',
                        fg_color='#fff',
                        command=lambda: click(5))
cinco_button.place(x=102,y=142)

seis_button = ctk.CTkButton(root,
                        text='6',
                        font=('futura',12,'bold'),
                        text_color='#003DC0',
                        width=102,
                        height=71,
                        corner_radius=0,
                        bg_color='blue',
                        fg_color='#fff',
                        command=lambda: click(6))
seis_button.place(x=204,y=142)

# terceira fileira

sete_button = ctk.CTkButton(root,
                        text='7',
                        font=('futura',12,'bold'),
                        text_color='#003DC0',
                        width=102,
                        height=71,
                        corner_radius=0,
                        bg_color='blue',
                        fg_color='#fff',
                        command=lambda: click(7))
sete_button.place(x=0,y=213)

oito_button = ctk.CTkButton(root,
                        text='8',
                        font=('futura',12,'bold'),
                        text_color='#003DC0',
                        width=102,
                        height=71,
                        corner_radius=0,
                        bg_color='blue',
                        fg_color='#fff',
                        command=lambda: click(8))
oito_button.place(x=102,y=213)

nove_button = ctk.CTkButton(root,
                        text='9',
                        font=('futura',12,'bold'),
                        text_color='#003DC0',
                        width=102,
                        height=71,
                        corner_radius=0,
                        bg_color='blue',
                        fg_color='#fff',
                        command=lambda: click(9))
nove_button.place(x=204,y=213)


# quarta fileira

zero_button = ctk.CTkButton(root,
                        text='0',
                        font=('futura',12,'bold'),
                        text_color='#003DC0',
                        width=204,
                        height=71,
                        corner_radius=0,
                        bg_color='blue',
                        fg_color='#fff',
                        command=lambda: click(0))
zero_button.place(x=0,y=284)

del_button = ctk.CTkButton(root,
                        text='C',
                        font=('futura',12,'bold'),
                        text_color='#003DC0',
                        width=102,
                        height=71,
                        corner_radius=0,
                        bg_color='blue',
                        fg_color='#fff',
                        command=deletar)
del_button.place(x=204,y=284)



root.mainloop()