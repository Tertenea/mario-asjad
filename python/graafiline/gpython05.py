#P.Kiviorg
#11.01.2023
#tkinter ülesanne 5
from tkinter import *

def arvuta():
    hind = float(sisestus.get())
    kmaks = var.get()
    
    vastus = hind*kmaks
    text2.config(text=f'{vastus:.2f}€')
    vastus2 = hind+vastus
    text3.config(text=f'{vastus2:.2f}€')
    

aken = Tk()
aken.title('Käibemaksukalkulaator')
aken.geometry('300x230')
aken.resizable(0, 0)

nupp = Button(aken, text = 'Ok', width = 4, font = 'Tahoma 12', command = arvuta)
nupp.grid(row = 7, column = 1, padx = 2, pady = 2, sticky = 'e')

joon = Label(aken, text = '_________________________________________', font = 'Tahoma 10', padx = 2, pady = 2)
joon.grid(row = 4, column = 0, columnspan = 2)

text = Label(aken, text = 'Käibemaks:', font = 'Tahoma 12', padx = 4, pady = 4)
text.grid(row = 5, column = 0, sticky = 'w')
text2 = Label(aken, text = '0.00€', font = 'Tahoma 12', padx = 4, pady = 4)
text2.grid(row = 5, column = 1)

text = Label(aken, text = 'Hind käibemaksuga:', font = 'Tahoma 12', padx = 4, pady = 4)
text.grid(row = 6, column = 0, sticky = 'w')
text3 = Label(aken, text = '0.00€', font = 'Tahoma 12', padx = 4, pady = 4)
text3.grid(row = 6, column = 1)

var = DoubleVar()
silt2 = Label(aken, text = 'Käibemaksumäär: ', font = 'Tahoma 12', padx = 4, pady = 4)
silt2.grid(row = 2, sticky = 'w')
valik1 = Radiobutton(aken, text = '9%', variable = var, value = 0.09, font = 'Tahoma 12', padx = 4, pady = 4)
valik1.grid(row = 2, column = 1)
valik2 = Radiobutton(aken, text = '20%', variable = var, value = 0.2, font = 'Tahoma 12', padx = 4, pady = 4)
valik2.grid(row = 3, column = 1)

silt = Label(aken, text = 'Hind käibemaksuta: ', font = 'Tahoma 12', padx = 4, pady = 4)
silt.grid(row = 1, sticky = 'w')

sisestus = Entry(aken)
sisestus.grid(row = 1, column = 1)

aken.mainloop()
