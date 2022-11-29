#P.Kiviorg
#21.11.2022
#Kontrolltöö
#4. PANK

hoius = int(input("Sisestage summa millega soovite alustada hoiust: "))
lisa = int(input("Sisestage summa mida soovite iga kuu lisada hoiusele: "))
intress = int(input("Sisestage intressimäär aastas: "))
ykskuu = intress/100/12+1
tulu = 0

for i in range(10):
    for i in range(12):
        kasum = (hoius+lisa)*ykskuu
        tulu = kasum-hoius-lisa+tulu
        hoius = kasum

print(f"Kontoseis 10. aastal: {round(hoius, 2)}")
print(f"Intressidest saadud tulu: {round(tulu,2)}")
