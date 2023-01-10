from tkinter import *

nimi = input('Sisesta oma täis nimi: ')
ryhm = input('Sisesta oma rühm: ')
aasta = int(input('Sisesta praegune aasta: '))

aken = Tk()
aken.title('Tervitus')
aken.iconbitmap('favicon.ico')
aken.configure(background = 'orange')
aken.resizable(0, 0)
Label(aken, text = f'Nimi: {nimi}', font = 'Tahoma 16 bold italic', fg = 'pink', bg = 'orange', pady = 10, padx = 30).pack()
Label(aken, text = f'Rühm: {ryhm}', font = 'Tahoma 16 bold italic', fg = 'pink', bg = 'orange', pady = 10, padx = 30).pack()
Label(aken, text = aasta, font = 'Tahoma 16 bold italic', fg = 'pink', bg = 'orange', pady = 10, padx = 30).pack()

aken.mainloop()
