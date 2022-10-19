#P.Kiviorg
#17.10.2022
#Harjutus 4
import random

#ruut
a,b = 10,20
if a==b:
    print(f"{a} ja {b} teevad kokku ruudu")
else:
    print(f"{a} ja {b} ei tee kokku ruutu")

a = int(input("Number 1: "))
b = int(input("Number 2: "))
tehe = input("Vali tehe (+ - * /): ")

#kalkulaator
if tehe=="+":
    vastus = a + b
elif tehe=="-":
    vastus= a - b
elif tehe=="*":
    vastus= a * b
elif tehe=="/":
    vastus= a / b
else:
    vastus = "n/a"
print(f"{a}{tehe}{b}={vastus}")

#juubel
sp = "5.6.2000"
print("Juubel") if 2022-int(sp.split(".")[2])%5==0 else print("Ei ole juubel")

#soodustus
hind = float(input("Sisesta toote hind: "))
if hind>10:
    print("Soodustus 20%")
else:
    print("Soodustus 10%")

#jalka meeskond
sugu = input("Sisesta oma sugu (mees või naine): ")
if sugu=="mees":
    vanus = int(input("Sisesta oma vanus: "))
    if 16<=vanus<=18:
        print("sobid meeskonda")
    elif vanus<16:
        print("tõmba nahhui tatt")
    elif vanus>18:
        print("goodbye boomer")
    else:
        print("mine ära")
else:
    print("mine ära")

#tärnid
print()
for i in range (5):
    print("* "*5)

print()
x=1
for i in range (5):
    print("* "*x)
    x+=1
    
print()
y=5
for i in range (5):
    print("* "*y)
    y-=1

#loto
for i in range (5):
    print(random.randint(0,9),end="")
print()

#paaris paaritu
for i in range (1,101):
    if i%2==0:
        print(f"{i} on paaris")
    else:
        print(f"{i} on paaritu")

#5 korrutus tabel
arv = 5
for i in range (1,11):
    print(f"{arv} x {i} = {arv*i}")

#viisikud
for i in range (1,101):
    if i%5==0:
        print(i)

#mäng
loop = 1

while loop==1:
    x=random.randint(1,5)
    for i in range (3):
        arva=int(input("Arva arv 1-5: "))
        if arva==x:
            print("tubli")
            break
        else:
            print("proovi uuesti loll luud")
    loop=0

#pank
kontoraha = 10000
intress = 0.05 #5%
aastad = 6
x=0
for i in range (aastad):
    print(f"sul on raha olnud pangas {x} aastat")
    print (f"arvel on {kontoraha}")
    kontoraha+=kontoraha*intress
    x+=1

#ruutude ja kuupide tabel
number=1
for i in range (1,11):
    print(number,end="  ")
    print(number**2,end="  ")
    print(number**3,end="  ")
    print()
    number+=1
