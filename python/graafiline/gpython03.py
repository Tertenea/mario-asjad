from tkinter import *

aken = Tk()
aken.title('Tervitus')
aken.iconbitmap('favicon.ico')
aken.configure(background = 'orange')
aken.resizable(0, 0)
Label(aken, text = 'Nimi: Peeter Kiviorg', font = 'Tahoma 16 bold italic', fg = 'pink', bg = 'orange', pady = 10, padx = 30).pack()
Label(aken, text = 'Rühm: IT22', font = 'Tahoma 16 bold italic', fg = 'pink', bg = 'orange', pady = 10, padx = 30).pack()
Label(aken, text = '2023', font = 'Tahoma 16 bold italic', fg = 'pink', bg = 'orange', pady = 10, padx = 30).pack()

aken.mainloop()
