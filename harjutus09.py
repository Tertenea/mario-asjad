#P.Kiviorg
#01.11.2022
#Harjutus 7
import datetime
import locale

isik = input("Sisesta oma isikukood: ")
x = (datetime.date(int("20"+isik[1:3]), int(isik[3:5]), int(isik[5:7])))
print(x)


aeg = datetime.datetime.now()
d = aeg.strftime("%d. %B %Y")
print(d)
locale.setlocale(locale.LC_ALL, "et_EE")
d = aeg.strftime("%d. %B %Y")
print(d)
