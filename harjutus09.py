#P.Kiviorg
#01.11.2022
#Harjutus 7
import datetime
import locale

isik = int(input("Sisesta oma isikukood: "))
x = isik.split()






aeg = datetime.datetime.now()
d = aeg.strftime("%d. %B %Y")
print(d)
locale.setlocale(locale.LC_ALL, "et_EE")
d = aeg.strftime("%d. %B %Y")
print(d)
