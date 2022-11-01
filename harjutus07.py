#P.Kiviorg
#01.11.2022
#Harjutus 7
import math
def kuup(a):
    print(f"Kuubi ruumala on {a**3}")
    
def kera(r):
    print(f"Kera ruumala on {round(4/3*math.pi*r**3)}")
    
def koonus(r, h):
    print(f"Koonuse ruumala on {round(math.pi*r**2*h/3)}")
    
def silinder(r, h):
    print(f"Silindri ruumala on {round(math.pi*r**2*h)}")




loop = 1
while loop == 1:
    print("-----RUUMALA-----")
    valik = int(input("1. Kuup\n2. Kera\n3. Koonus\n4. Silinder\n5. Välju\nVali 1-5: "))
    if valik == 1:
        a = int(input("Sisesta kuubi üks külg: "))
        kuup(a)
    elif valik == 2:
        r = int(input("Sisesta kera raadius: "))
        kera(r)
    elif valik == 3:
        r = int(input("Sisestage koonuse raadius: "))
        h = int(input("Sisestage koonuse kõrgus: "))
        koonus(r, h)
    elif valik == 4:
        r = int(input("Sisestage silindri raadius: "))
        h = int(input("Sisestage silindri kõrgus: "))        
        silinder()
    elif valik == 5:
        print("Programm sulgub")
        loop = 0
    else:
        print("Vigane sisestus või valik puudub")
    




def tervita(nimi="lambi jorss",keel="ge"):
    if keel=="et":
        print(f"Tsau {nimi}")
    elif keel=="en":
        print(f"Hey {nimi}")
    else:
        print(f"Hallo {nimi}")
    
tervita()
tervita("Mario", "en")
tervita("Mario", "et")
