#importanto bibliotecas
from tkinter import *
from tkinter import ttk

#color / cores
color1 = "#0d0d0d"  #BLACK / PRETO
color2 = "#feffff"  # WHITE / BRANCO
color3 = "#38576b"  # DARKER BLUE / AZUL MAIS ESCURO
color4 = "#ECEFF1"  # CINZA
color5 = "#FFAB40"  # ORANGE / LARANJA


#inicio / start
janela = Tk()
janela.title('CALCULADORA')
janela.geometry('235x318')
janela.config(bg=color1)

#tela de resultado /  result screen
frame_tela = Frame(janela, width=235, height=50, bg=color3)
frame_tela.grid(row=0, column=0)

#corpo é onde será atribuido os botões
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#botões / Buttons
b1 = Button(frame_corpo, text='C', width = 11, height = 2,bg=color4, font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)

b2 = Button(frame_corpo, text='%', width = 5, height = 2,bg=color4,font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b2.place(x=119, y=0)

b3= Button(frame_corpo, text='/', width = 5, height = 2,bg = color5, fg = color2,font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b3.place(x=177, y=0)

 

janela.mainloop()
