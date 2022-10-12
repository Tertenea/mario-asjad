#P.Kiviorg
#12.10.2022
#Harjutus 2
import math
import random
a=random.randint(1,15)
b=random.randint(1,15)
c=random.randint(1,15)

p=a+b+c
print("Kolmnurga ümbermõõt on ",p)

pitsa=12.90
jootraha=pitsa*1.1
maksa=jootraha/3
print("\nIgaüks peab maksma ",maksa,"€")

spd=29.9
spdmin=spd/60
kaugus=spdmin*24
print("\nRulluisutaja jõuab 24 minutiga ",round(kaugus,2)," kilomeetri kaugusele")

a=16
b=9
c=math.sqrt(a*a+b*b)
print("\nKolmnurga hüpotenuus on ",c)

minut=int(input("\nSisesta aeg minutites: "))
tund=minut/60
print("See on ",tund," tundi")

kmnd=int(input("\nSisesta arv kümnendsüsteemis: "))
kaks=bin(kmnd)
kuus=hex(kmnd)
print("See arv 2nd süsteemis on: ",kaks," ja 16nd süsteemis: ",kuus)

kyts=float(input("\nSisesta tangitud kütuse kogus liitrites: "))
maa=float(input("Sistesta läbitud vahemaa kilomeetrites: "))
kytssada=kyts/maa*100
print("Saja kilomeetri kohta kulub keskmiselt ",round(kytssada,2)," liitrit kütust")
