from tkinter import *

tela = Tk()

tela.title('CALCULADORA')
tela.geometry('200x300')

def abre_parentese():
    print('(')

def fecha_parentese():
    print(')')






button_c = Button(tela, text = 'C')
button_c.grid(column = 0, row = 0)

button_p1 = Button(tela, text = '(', command=abre_parentese)
button_p1.grid(column = 1, row = 0)

button_p2 = Button(tela, text = ')',command=fecha_parentese)
button_p2.grid(column = 2, row = 0)

button_div = Button(tela, text = '/')
button_div.grid(column = 3, row = 0)

button_7 = Button(tela, text = '7')
button_7.grid(column = 0, row = 1)

button_8 = Button(tela, text = '8')
button_8.grid(column = 1 ,row = 1)

button_9 = Button(tela, text = '9')
button_9.grid(column = 2 ,row = 1)

button_mult = Button(tela, text = '*')
button_mult.grid(column = 3 ,row = 1)

button_4 = Button(tela, text = '4')
button_4.grid(column = 0 ,row = 2)

button_5 = Button(tela, text = '5')
button_5.grid(column = 1,row = 2)

button_6 = Button(tela, text = '6')
button_6.grid(column = 2,row = 2)

button_sub= Button(tela, text = '-')
button_sub.grid(column = 3,row = 2)

button_1 = Button(tela, text = '1')
button_1.grid(column = 0 ,row = 3)

button_4 = Button(tela, text = '2')
button_4.grid(column = 1 ,row = 3)

button_3 = Button(tela, text = '3')
button_3.grid(column = 2 ,row = 3)

button_soma = Button(tela, text = '+')
button_soma.grid(column = 3 ,row = 3)

button_0 = Button(tela, text = '0')
button_0.grid(column = 0 ,row = 4)

button_pct = Button(tela, text = '%')
button_pct.grid(column = 1 ,row = 4)

button_vir = Button(tela, text = ',')
button_vir.grid(column = 2,row = 4)

button_rst= Button(tela, text = '=')
button_rst.grid(column = 3 ,row = 4)






tela.mainloop()
