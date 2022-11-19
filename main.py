#importanto bibliotecas
from tkinter import *
from tkinter import ttk

#color / cores
color1 = "#0d0d0d"  #BLACK / PRETO
color2 = "#feffff"  # WHITE / BRANCO
color3 = "#121317"  # lLEAD  / CHUMBO
color4 = "#ECEFF1"  # CINZA
color5 = "#FFAB40"  # ORANGE / LARANJA


#inicio / start
janela = Tk()
janela.title('CALCULADORA')
janela.geometry('235x305')
janela.config(bg=color1)

#tela de resultado /  result screen
frame_tela = Frame(janela, width=235, height=50, bg=color3)
frame_tela.grid(row=0, column=0)

#corpo é onde será atribuido os botões
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)


#criando label
app_label = Label(frame_tela, text='123456789', width=16, height = 2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg = color3, fg = color2)
app_label.place(x=0,y=0)
#botões / Buttons
b1 = Button(frame_corpo, text='C', width = 11, height = 2,bg=color4, font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(frame_corpo, text='%', width = 5, height = 2,bg=color4,font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b2.place(x=119, y=0)
b3= Button(frame_corpo, text='/', width = 5, height = 2,bg = color5, fg = color2,font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b3.place(x=178, y=0)

b4 = Button(frame_corpo, text='7', width = 5, height = 2,bg=color4, font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b4.place(x=0.5, y=51)
b5 = Button(frame_corpo, text='8', width = 5, height = 2,bg=color4,font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b5.place(x=59.5, y=51)
b6= Button(frame_corpo, text='9', width = 5, height = 2,bg = color4,font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b6.place(x=119, y=51)
b7= Button(frame_corpo, text='*', width = 5, height = 2,bg = color5, fg = color2,font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b7.place(x=178, y=51)

b8 = Button(frame_corpo, text='4', width = 5, height = 2,bg=color4, font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b8.place(x=0.5, y=102)
b9= Button(frame_corpo, text='5', width = 5, height = 2,bg=color4,font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b9.place(x=59.5, y=102)
b10= Button(frame_corpo, text='6', width = 5, height = 2,bg = color4,font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b10.place(x=119, y=102)
b11= Button(frame_corpo, text='-', width = 5, height = 2,bg = color5, fg = color2,font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b11.place(x=178, y=102)

b12 = Button(frame_corpo, text='1', width = 5, height = 2,bg=color4, font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b12.place(x=0.5, y=153)
b13 = Button(frame_corpo, text='2', width = 5, height = 2,bg=color4,font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b13.place(x=59.5, y=153)
b14= Button(frame_corpo, text='3', width = 5, height = 2,bg = color4,font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b14.place(x=119, y=153)
b15= Button(frame_corpo, text='+', width = 5, height = 2,bg = color5, fg = color2,font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b15.place(x=178, y=153)

b16 = Button(frame_corpo, text='0', width = 11, height = 2,bg=color4, font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b16.place(x=0, y=204)
b17 = Button(frame_corpo, text='.', width = 5, height = 2,bg=color4,font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b17.place(x=119, y=204)
b18 = Button(frame_corpo, text='=', width = 5, height = 2,bg = color5, fg = color2,font=('Ivy 13 bold'),relief = RAISED, overrelief=RIDGE)
b18.place(x=178, y=204)








janela.mainloop()
